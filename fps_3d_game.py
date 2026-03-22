import math
import random
import tkinter as tk
from dataclasses import dataclass


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
HALF_HEIGHT = SCREEN_HEIGHT // 2
FOV = math.pi / 3
HALF_FOV = FOV / 2
RAY_COUNT = 240
MAX_DEPTH = 18
WALL_STRIP_WIDTH = SCREEN_WIDTH / RAY_COUNT
MOVE_SPEED = 0.09
ROTATE_SPEED = 0.065
PLAYER_RADIUS = 0.22
PICKUP_RANGE = 1.25
GRENADE_SPEED = 0.2


WORLD_MAP = [
    "111111111111111111",
    "100000000010000001",
    "101111011010111101",
    "100001010000100001",
    "101101011110101101",
    "100101000000100001",
    "110101111011111101",
    "100100000010000001",
    "101111011110111101",
    "100000010000100001",
    "101111110111101101",
    "100010000100000001",
    "111111111111111111",
]


WEAPONS = {
    "Pistol": {
        "damage": 30,
        "cooldown": 18,
        "spread": 0.03,
        "pellets": 1,
        "ammo_use": 1,
        "ammo_pickup": 18,
        "label": "Pistol",
        "color": "#D6B25E",
    },
    "Rifle": {
        "damage": 20,
        "cooldown": 8,
        "spread": 0.018,
        "pellets": 1,
        "ammo_use": 1,
        "ammo_pickup": 28,
        "label": "Rifle",
        "color": "#78B3CE",
    },
    "Shotgun": {
        "damage": 14,
        "cooldown": 26,
        "spread": 0.12,
        "pellets": 6,
        "ammo_use": 1,
        "ammo_pickup": 10,
        "label": "Shotgun",
        "color": "#D9795F",
    },
}


PICKUP_TYPES = {
    "ammo": {"label": "Ammo", "color": "#F8D66D"},
    "grenade": {"label": "Grenade", "color": "#A3E635"},
    "medkit": {"label": "Medkit", "color": "#FB7185"},
}


@dataclass
class Enemy:
    x: float
    y: float
    health: int = 60
    speed: float = 0.03
    attack_cooldown: int = 0
    hurt_flash: int = 0


@dataclass
class Pickup:
    x: float
    y: float
    kind: str
    amount: int


@dataclass
class Grenade:
    x: float
    y: float
    angle: float
    timer: int = 70
    speed: float = GRENADE_SPEED


class Shooter3DGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("3D Shooter")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            bg="#08111F",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.keys = set()
        self.weapon_order = list(WEAPONS)
        self.menu_index = 0
        self.state = "menu"
        self.message = "Choose a weapon and start the mission"
        self.message_timer = 999999

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)

        self.reset_world(self.weapon_order[self.menu_index])
        self.game_loop()

    def reset_world(self, weapon_name):
        self.map_width = len(WORLD_MAP[0])
        self.map_height = len(WORLD_MAP)
        self.player_x = 2.5
        self.player_y = 2.5
        self.player_angle = 0.0
        self.player_health = 100
        self.kills = 0
        self.weapon_name = weapon_name
        self.ammo = 60
        self.grenades = 3
        self.fire_cooldown = 0
        self.damage_flash = 0
        self.spawn_timer = 420
        self.enemies = [
            Enemy(8.5, 3.5),
            Enemy(10.5, 6.5),
            Enemy(14.5, 9.5),
            Enemy(6.5, 10.5),
        ]
        self.pickups = []
        self.grenade_list = []

    def on_key_press(self, event):
        key = event.keysym.lower()
        self.keys.add(key)

        if self.state == "menu":
            if key in {"left", "a"}:
                self.menu_index = (self.menu_index - 1) % len(self.weapon_order)
            elif key in {"right", "d"}:
                self.menu_index = (self.menu_index + 1) % len(self.weapon_order)
            elif key in {"1", "2", "3"}:
                self.menu_index = min(len(self.weapon_order) - 1, int(key) - 1)
            elif key in {"return", "space"}:
                self.start_game()
            return

        if key == "space":
            self.fire_weapon()
        elif key == "g":
            self.throw_grenade()
        elif key == "e":
            self.collect_pickups()
        elif key == "r" and self.state in {"game_over", "victory"}:
            self.state = "menu"
            self.menu_index = self.weapon_order.index(self.weapon_name)
            self.message = "Back to menu. Pick a weapon to play again"
            self.message_timer = 999999

    def on_key_release(self, event):
        self.keys.discard(event.keysym.lower())

    def start_game(self):
        weapon_name = self.weapon_order[self.menu_index]
        self.reset_world(weapon_name)
        self.state = "playing"
        self.message = (
            f"Equipped {WEAPONS[weapon_name]['label']} | "
            "WASD move | Left Right turn | Space fire | G grenade | E pickup"
        )
        self.message_timer = 360

    def game_loop(self):
        self.update()
        self.draw()
        self.root.after(16, self.game_loop)

    def update(self):
        if self.state != "playing":
            return

        if self.message_timer > 0:
            self.message_timer -= 1
        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1
        if self.damage_flash > 0:
            self.damage_flash -= 1

        self.handle_input()
        self.update_enemies()
        self.update_grenades()
        self.spawn_timer -= 1
        if self.spawn_timer <= 0 and len(self.enemies) < 7:
            self.spawn_enemy()
            self.spawn_timer = 360

        if self.player_health <= 0:
            self.player_health = 0
            self.state = "game_over"
            self.message = "You were defeated. Press R to return to menu"
            self.message_timer = 999999

        if self.kills >= 12 and not self.enemies:
            self.state = "victory"
            self.message = "Area secured. Press R to return to menu"
            self.message_timer = 999999

    def handle_input(self):
        if "left" in self.keys:
            self.player_angle -= ROTATE_SPEED
        if "right" in self.keys:
            self.player_angle += ROTATE_SPEED

        forward = 0
        side = 0
        if "w" in self.keys:
            forward += MOVE_SPEED
        if "s" in self.keys:
            forward -= MOVE_SPEED
        if "a" in self.keys:
            side -= MOVE_SPEED
        if "d" in self.keys:
            side += MOVE_SPEED

        dx = math.cos(self.player_angle) * forward + math.cos(self.player_angle + math.pi / 2) * side
        dy = math.sin(self.player_angle) * forward + math.sin(self.player_angle + math.pi / 2) * side
        self.move_with_collision(dx, dy)

    def move_with_collision(self, dx, dy):
        new_x = self.player_x + dx
        new_y = self.player_y + dy
        if not self.is_wall(new_x, self.player_y):
            self.player_x = new_x
        if not self.is_wall(self.player_x, new_y):
            self.player_y = new_y

    def is_wall(self, x, y):
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            return True
        corners = [
            (x - PLAYER_RADIUS, y - PLAYER_RADIUS),
            (x + PLAYER_RADIUS, y - PLAYER_RADIUS),
            (x - PLAYER_RADIUS, y + PLAYER_RADIUS),
            (x + PLAYER_RADIUS, y + PLAYER_RADIUS),
        ]
        for px, py in corners:
            if WORLD_MAP[int(py)][int(px)] == "1":
                return True
        return False

    def fire_weapon(self):
        if self.state != "playing" or self.fire_cooldown > 0:
            return
        if self.ammo <= 0:
            self.set_message("Out of ammo. Defeat enemies and collect loot")
            return

        weapon = WEAPONS[self.weapon_name]
        self.fire_cooldown = weapon["cooldown"]
        self.ammo -= weapon["ammo_use"]
        hit_any = False

        for _ in range(weapon["pellets"]):
            shot_angle = self.player_angle + random.uniform(-weapon["spread"], weapon["spread"])
            distance, target = self.trace_enemy_hit(shot_angle)
            if target and distance < MAX_DEPTH:
                target.health -= weapon["damage"]
                target.hurt_flash = 5
                hit_any = True
                if target.health <= 0:
                    self.kill_enemy(target)

        if hit_any:
            self.set_message("Target hit")
        else:
            self.set_message("Shot missed")

    def trace_enemy_hit(self, angle):
        step = 0.05
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)
        depth = step

        while depth < MAX_DEPTH:
            x = self.player_x + cos_a * depth
            y = self.player_y + sin_a * depth
            if self.world_cell(x, y) == "1":
                return depth, None
            for enemy in self.enemies:
                if math.hypot(enemy.x - x, enemy.y - y) < 0.38:
                    return depth, enemy
            depth += step
        return MAX_DEPTH, None

    def throw_grenade(self):
        if self.state != "playing":
            return
        if self.grenades <= 0:
            self.set_message("No grenades left")
            return
        self.grenades -= 1
        self.grenade_list.append(Grenade(self.player_x, self.player_y, self.player_angle))
        self.set_message("Grenade thrown")

    def update_grenades(self):
        for grenade in list(self.grenade_list):
            next_x = grenade.x + math.cos(grenade.angle) * grenade.speed
            next_y = grenade.y + math.sin(grenade.angle) * grenade.speed
            if self.world_cell(next_x, next_y) == "1":
                grenade.timer = 0
            else:
                grenade.x = next_x
                grenade.y = next_y

            grenade.timer -= 1
            if grenade.timer <= 0:
                self.explode_grenade(grenade)
                self.grenade_list.remove(grenade)

    def explode_grenade(self, grenade):
        defeated = 0
        for enemy in list(self.enemies):
            distance = math.hypot(enemy.x - grenade.x, enemy.y - grenade.y)
            if distance <= 2.2:
                damage = max(0, int(85 - distance * 25))
                enemy.health -= damage
                enemy.hurt_flash = 8
                if enemy.health <= 0:
                    self.kill_enemy(enemy)
                    defeated += 1

        if math.hypot(self.player_x - grenade.x, self.player_y - grenade.y) <= 1.8:
            self.take_damage(28)

        if defeated:
            self.set_message(f"Explosion defeated {defeated} enemies")
        else:
            self.set_message("Explosion finished")

    def update_enemies(self):
        for enemy in list(self.enemies):
            if enemy.hurt_flash > 0:
                enemy.hurt_flash -= 1
            if enemy.attack_cooldown > 0:
                enemy.attack_cooldown -= 1

            dx = self.player_x - enemy.x
            dy = self.player_y - enemy.y
            distance = math.hypot(dx, dy)

            if distance > 0.7:
                move_x = dx / distance * enemy.speed
                move_y = dy / distance * enemy.speed
                next_x = enemy.x + move_x
                next_y = enemy.y + move_y
                if self.world_cell(next_x, enemy.y) != "1":
                    enemy.x = next_x
                if self.world_cell(enemy.x, next_y) != "1":
                    enemy.y = next_y
            elif enemy.attack_cooldown <= 0:
                self.take_damage(8)
                enemy.attack_cooldown = 45

    def take_damage(self, amount):
        self.player_health -= amount
        self.damage_flash = 6
        self.set_message(f"Took {amount} damage")

    def kill_enemy(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
        self.kills += 1
        self.drop_loot(enemy.x, enemy.y)

    def drop_loot(self, x, y):
        roll = random.random()
        if roll < 0.5:
            kind = "ammo"
            amount = WEAPONS[self.weapon_name]["ammo_pickup"]
        elif roll < 0.78:
            kind = "grenade"
            amount = 1
        else:
            kind = "medkit"
            amount = 20
        self.pickups.append(Pickup(x, y, kind, amount))
        self.set_message(f"Enemy dropped {PICKUP_TYPES[kind]['label']}. Move close and press E")

    def collect_pickups(self):
        collected = []
        for pickup in self.pickups:
            if math.hypot(self.player_x - pickup.x, self.player_y - pickup.y) <= PICKUP_RANGE:
                collected.append(pickup)

        if not collected:
            self.set_message("No loot nearby")
            return

        for pickup in collected:
            if pickup.kind == "ammo":
                self.ammo += pickup.amount
            elif pickup.kind == "grenade":
                self.grenades += pickup.amount
            elif pickup.kind == "medkit":
                self.player_health = min(100, self.player_health + pickup.amount)
            self.pickups.remove(pickup)

        labels = ", ".join(PICKUP_TYPES[item.kind]["label"] for item in collected)
        self.set_message(f"Picked up {labels}")

    def spawn_enemy(self):
        spawn_points = [
            (15.5, 2.5),
            (15.5, 10.5),
            (9.5, 8.5),
            (3.5, 11.0),
            (12.5, 5.5),
        ]
        random.shuffle(spawn_points)
        for sx, sy in spawn_points:
            if math.hypot(self.player_x - sx, self.player_y - sy) > 4 and self.world_cell(sx, sy) != "1":
                self.enemies.append(Enemy(sx, sy, health=70, speed=0.034))
                return

    def world_cell(self, x, y):
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            return "1"
        return WORLD_MAP[int(y)][int(x)]

    def cast_rays(self):
        wall_data = []
        start_angle = self.player_angle - HALF_FOV

        for ray in range(RAY_COUNT):
            ray_angle = start_angle + (ray / RAY_COUNT) * FOV
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            depth = 0.02

            while depth < MAX_DEPTH:
                x = self.player_x + cos_a * depth
                y = self.player_y + sin_a * depth
                if self.world_cell(x, y) == "1":
                    corrected_depth = depth * math.cos(self.player_angle - ray_angle)
                    corrected_depth = max(corrected_depth, 0.001)
                    wall_height = min(SCREEN_HEIGHT * 1.6, 820 / corrected_depth)
                    shade = max(25, min(190, int(220 - corrected_depth * 12)))
                    wall_data.append((corrected_depth, wall_height, shade))
                    break
                depth += 0.02
            else:
                wall_data.append((MAX_DEPTH, 0, 25))

        return wall_data

    def draw(self):
        self.canvas.delete("all")
        if self.state == "menu":
            self.draw_menu()
            return

        wall_data = self.cast_rays()
        self.draw_background()
        self.draw_walls(wall_data)
        self.draw_sprites(wall_data)
        self.draw_weapon()
        self.draw_hud()

        if self.damage_flash > 0:
            self.canvas.create_rectangle(
                0,
                0,
                SCREEN_WIDTH,
                SCREEN_HEIGHT,
                fill="#5A1111",
                outline="",
                stipple="gray25",
            )

        if self.state in {"game_over", "victory"}:
            self.draw_overlay()

    def draw_menu(self):
        self.canvas.create_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, fill="#07111E", outline="")
        self.canvas.create_rectangle(
            90,
            80,
            SCREEN_WIDTH - 90,
            SCREEN_HEIGHT - 80,
            fill="#11213A",
            outline="#3C5A86",
            width=4,
        )
        self.canvas.create_text(
            SCREEN_WIDTH / 2,
            140,
            text="3D Shooter Prototype",
            fill="#F8FAFC",
            font=("Segoe UI", 34, "bold"),
        )
        self.canvas.create_text(
            SCREEN_WIDTH / 2,
            200,
            text="Choose your starting weapon, clear enemies, and collect dropped gear",
            fill="#C9D7EE",
            font=("Segoe UI", 14),
        )

        card_w = 250
        gap = 40
        total_w = card_w * len(self.weapon_order) + gap * (len(self.weapon_order) - 1)
        base_x = (SCREEN_WIDTH - total_w) / 2

        for index, weapon_name in enumerate(self.weapon_order):
            x1 = base_x + index * (card_w + gap)
            y1 = 280
            x2 = x1 + card_w
            y2 = 500
            weapon = WEAPONS[weapon_name]
            selected = index == self.menu_index
            self.canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill="#1A2C48" if selected else "#0E1A2D",
                outline=weapon["color"] if selected else "#415A77",
                width=5 if selected else 2,
            )
            self.canvas.create_text(
                (x1 + x2) / 2,
                y1 + 42,
                text=weapon["label"],
                fill="white",
                font=("Segoe UI", 24, "bold"),
            )
            self.canvas.create_text(
                (x1 + x2) / 2,
                y1 + 94,
                text=f"Damage {weapon['damage']}",
                fill="#F8FAFC",
                font=("Segoe UI", 14),
            )
            self.canvas.create_text(
                (x1 + x2) / 2,
                y1 + 126,
                text=f"Rate {max(1, 35 - weapon['cooldown'])}",
                fill="#F8FAFC",
                font=("Segoe UI", 14),
            )
            self.canvas.create_text(
                (x1 + x2) / 2,
                y1 + 158,
                text=f"Spread {weapon['spread']:.2f}",
                fill="#F8FAFC",
                font=("Segoe UI", 14),
            )
            self.canvas.create_text(
                (x1 + x2) / 2,
                y1 + 206,
                text=f"Press {index + 1} to select",
                fill=weapon["color"],
                font=("Segoe UI", 12, "bold"),
            )

        self.canvas.create_text(
            SCREEN_WIDTH / 2,
            610,
            text="Left Right or A D to choose | Enter or Space to start",
            fill="#E6EDF7",
            font=("Segoe UI", 16),
        )

    def draw_background(self):
        self.canvas.create_rectangle(0, 0, SCREEN_WIDTH, HALF_HEIGHT, fill="#6FA9D7", outline="")
        self.canvas.create_rectangle(0, HALF_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, fill="#2C3D2F", outline="")
        for i in range(5):
            y = HALF_HEIGHT + i * 40
            self.canvas.create_line(0, y, SCREEN_WIDTH, y, fill="#36483B")

    def draw_walls(self, wall_data):
        for index, (_, wall_height, shade) in enumerate(wall_data):
            x1 = index * WALL_STRIP_WIDTH
            x2 = x1 + WALL_STRIP_WIDTH + 1
            top = HALF_HEIGHT - wall_height / 2
            bottom = HALF_HEIGHT + wall_height / 2
            color = f"#{shade:02x}{shade:02x}{max(20, shade - 35):02x}"
            self.canvas.create_rectangle(x1, top, x2, bottom, fill=color, outline=color)

    def draw_sprites(self, wall_data):
        sprites = []

        for enemy in self.enemies:
            data = self.project_sprite(enemy.x, enemy.y)
            if data:
                depth, screen_x, size = data
                color = "#F87171" if enemy.hurt_flash else "#BE123C"
                sprites.append(("enemy", depth, screen_x, size, color))

        for pickup in self.pickups:
            data = self.project_sprite(pickup.x, pickup.y)
            if data:
                depth, screen_x, size = data
                sprites.append(("pickup", depth, screen_x, size * 0.6, PICKUP_TYPES[pickup.kind]["color"]))

        for grenade in self.grenade_list:
            data = self.project_sprite(grenade.x, grenade.y)
            if data:
                depth, screen_x, size = data
                sprites.append(("grenade", depth, screen_x, size * 0.45, "#FBBF24"))

        sprites.sort(key=lambda item: item[1], reverse=True)

        for sprite_type, depth, screen_x, size, color in sprites:
            ray_index = int(screen_x / WALL_STRIP_WIDTH)
            if 0 <= ray_index < len(wall_data) and depth > wall_data[ray_index][0] + 0.08:
                continue

            y_bottom = HALF_HEIGHT + size / 2
            if sprite_type == "enemy":
                self.canvas.create_rectangle(
                    screen_x - size * 0.32,
                    y_bottom - size,
                    screen_x + size * 0.32,
                    y_bottom,
                    fill=color,
                    outline="#111827",
                    width=2,
                )
                self.canvas.create_oval(
                    screen_x - size * 0.12,
                    y_bottom - size * 0.85,
                    screen_x + size * 0.12,
                    y_bottom - size * 0.62,
                    fill="#FDE68A",
                    outline="",
                )
            elif sprite_type == "pickup":
                self.canvas.create_oval(
                    screen_x - size * 0.28,
                    y_bottom - size * 0.45,
                    screen_x + size * 0.28,
                    y_bottom,
                    fill=color,
                    outline="#0F172A",
                    width=2,
                )
            else:
                self.canvas.create_oval(
                    screen_x - size * 0.22,
                    y_bottom - size * 0.22,
                    screen_x + size * 0.22,
                    y_bottom + size * 0.22,
                    fill=color,
                    outline="#111827",
                    width=2,
                )

    def project_sprite(self, x, y):
        dx = x - self.player_x
        dy = y - self.player_y
        distance = math.hypot(dx, dy)
        if distance < 0.1:
            return None

        angle = math.atan2(dy, dx) - self.player_angle
        while angle > math.pi:
            angle -= math.tau
        while angle < -math.pi:
            angle += math.tau

        if abs(angle) > HALF_FOV + 0.35:
            return None

        screen_x = (angle + HALF_FOV) / FOV * SCREEN_WIDTH
        size = min(460, 520 / max(distance, 0.2))
        return distance, screen_x, size

    def draw_weapon(self):
        weapon = WEAPONS[self.weapon_name]
        sway = math.sin(self.fire_cooldown * 0.7) * 10 if self.fire_cooldown else 0
        base_y = SCREEN_HEIGHT - 120 + sway
        self.canvas.create_rectangle(
            SCREEN_WIDTH / 2 - 70,
            base_y - 30,
            SCREEN_WIDTH / 2 + 150,
            base_y + 100,
            fill=weapon["color"],
            outline="#111827",
            width=3,
        )
        self.canvas.create_rectangle(
            SCREEN_WIDTH / 2 + 30,
            base_y - 10,
            SCREEN_WIDTH / 2 + 210,
            base_y + 24,
            fill="#1F2937",
            outline="#111827",
            width=2,
        )
        self.canvas.create_text(
            SCREEN_WIDTH / 2 + 32,
            base_y + 60,
            anchor="w",
            text=weapon["label"],
            fill="#0F172A",
            font=("Segoe UI", 14, "bold"),
        )
        cross = "#F8FAFC" if self.fire_cooldown == 0 else "#FCA5A5"
        self.canvas.create_line(
            SCREEN_WIDTH / 2 - 12,
            HALF_HEIGHT,
            SCREEN_WIDTH / 2 + 12,
            HALF_HEIGHT,
            fill=cross,
            width=2,
        )
        self.canvas.create_line(
            SCREEN_WIDTH / 2,
            HALF_HEIGHT - 12,
            SCREEN_WIDTH / 2,
            HALF_HEIGHT + 12,
            fill=cross,
            width=2,
        )

    def draw_hud(self):
        self.canvas.create_rectangle(20, 18, 342, 144, fill="#09121F", outline="#37517C", width=2)
        self.canvas.create_text(36, 42, anchor="w", text=f"Health: {self.player_health}", fill="#F8FAFC", font=("Segoe UI", 15, "bold"))
        self.canvas.create_text(36, 72, anchor="w", text=f"Ammo: {self.ammo}", fill="#F8FAFC", font=("Segoe UI", 14))
        self.canvas.create_text(36, 100, anchor="w", text=f"Grenades: {self.grenades}", fill="#F8FAFC", font=("Segoe UI", 14))
        self.canvas.create_text(36, 128, anchor="w", text=f"Kills: {self.kills}", fill="#F8FAFC", font=("Segoe UI", 14))

        self.canvas.create_rectangle(
            SCREEN_WIDTH - 330,
            18,
            SCREEN_WIDTH - 18,
            116,
            fill="#09121F",
            outline="#37517C",
            width=2,
        )
        self.canvas.create_text(
            SCREEN_WIDTH - 314,
            42,
            anchor="w",
            text=f"Weapon: {WEAPONS[self.weapon_name]['label']}",
            fill="#F8FAFC",
            font=("Segoe UI", 14, "bold"),
        )
        self.canvas.create_text(
            SCREEN_WIDTH - 314,
            72,
            anchor="w",
            text="WASD move | Left Right turn",
            fill="#D9E4F5",
            font=("Segoe UI", 12),
        )
        self.canvas.create_text(
            SCREEN_WIDTH - 314,
            98,
            anchor="w",
            text="Space fire | G grenade | E pickup",
            fill="#D9E4F5",
            font=("Segoe UI", 12),
        )

        if self.message_timer > 0:
            self.canvas.create_rectangle(
                220,
                SCREEN_HEIGHT - 58,
                SCREEN_WIDTH - 220,
                SCREEN_HEIGHT - 18,
                fill="#0F172A",
                outline="#334155",
                width=2,
            )
            self.canvas.create_text(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 38,
                text=self.message,
                fill="#F8FAFC",
                font=("Segoe UI", 12),
            )

    def draw_overlay(self):
        self.canvas.create_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, fill="#020617", outline="", stipple="gray50")
        title = "Victory" if self.state == "victory" else "Mission Failed"
        sub = "The area is clear" if self.state == "victory" else "The enemy overran your position"
        self.canvas.create_text(SCREEN_WIDTH / 2, 280, text=title, fill="#F8FAFC", font=("Segoe UI", 34, "bold"))
        self.canvas.create_text(SCREEN_WIDTH / 2, 334, text=sub, fill="#CBD5E1", font=("Segoe UI", 16))
        self.canvas.create_text(
            SCREEN_WIDTH / 2,
            388,
            text="Press R to return to the weapon select screen",
            fill="#FDE68A",
            font=("Segoe UI", 15, "bold"),
        )

    def set_message(self, text):
        self.message = text
        self.message_timer = 180

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Shooter3DGame().run()
