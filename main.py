import math
import random
import tkinter as tk
from dataclasses import dataclass


TILE_SIZE = 32
WORLD_WIDTH = 64
WORLD_HEIGHT = 24
SKY_HEIGHT = 8
HOTBAR_SIZE = 5
CANVAS_WIDTH = 960
CANVAS_HEIGHT = 640
GRAVITY = 0.45
MOVE_SPEED = 0.55
JUMP_SPEED = -7.8
MAX_FALL_SPEED = 8
ATTACK_RANGE = 52


BLOCKS = {
    "grass": {"color": "#5FA14B", "solid": True, "drops": "grass"},
    "dirt": {"color": "#8A5A36", "solid": True, "drops": "dirt"},
    "stone": {"color": "#6D7480", "solid": True, "drops": "stone"},
    "wood": {"color": "#8C6239", "solid": True, "drops": "wood"},
    "leaf": {"color": "#2F8F46", "solid": True, "drops": "leaf"},
}


ITEM_COLORS = {
    "grass": "#7BCB5B",
    "dirt": "#B47040",
    "stone": "#98A0AB",
    "wood": "#B58045",
    "leaf": "#4DBB5B",
}


@dataclass
class Entity:
    x: float
    y: float
    width: int
    height: int
    color: str
    vx: float = 0.0
    vy: float = 0.0
    on_ground: bool = False
    health: int = 5
    direction: int = 1

    def center(self):
        return self.x + self.width / 2, self.y + self.height / 2


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2D 我的世界")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg="#87CEEB",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.keys = set()
        self.mouse_world = (0, 0)
        self.selected_slot = 0
        self.inventory = {
            "grass": 10,
            "dirt": 25,
            "stone": 12,
            "wood": 8,
            "leaf": 6,
        }
        self.hotbar = ["dirt", "grass", "stone", "wood", "leaf"]
        self.message = "A/D 移动, W 跳跃, 左键挖掘, 右键建造, J 攻击, 1-5 切换物品"
        self.message_timer = 240

        self.world = [[None for _ in range(WORLD_WIDTH)] for _ in range(WORLD_HEIGHT)]
        self.generate_world()

        self.player = Entity(7 * TILE_SIZE, 4 * TILE_SIZE, 24, 42, "#2B2D42", health=10)
        self.player_spawn = (self.player.x, self.player.y)
        self.enemies = []
        self.spawn_initial_enemies()

        self.camera_x = 0
        self.camera_y = 0
        self.attack_cooldown = 0
        self.enemy_spawn_timer = 240
        self.game_over = False

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)
        self.root.bind("<Button-1>", self.on_left_click)
        self.root.bind("<Button-3>", self.on_right_click)
        self.root.bind("<Motion>", self.on_mouse_move)
        self.root.bind("<MouseWheel>", self.on_mouse_wheel)

        self.game_loop()

    def generate_world(self):
        heights = []
        ground_level = SKY_HEIGHT + 6
        current = ground_level
        for _ in range(WORLD_WIDTH):
            current += random.choice([-1, 0, 0, 1])
            current = max(SKY_HEIGHT + 4, min(WORLD_HEIGHT - 6, current))
            heights.append(current)

        for x, top in enumerate(heights):
            for y in range(top, WORLD_HEIGHT):
                if y == top:
                    self.world[y][x] = "grass"
                elif y < top + 3:
                    self.world[y][x] = "dirt"
                else:
                    self.world[y][x] = "stone"

        for _ in range(9):
            trunk_x = random.randint(2, WORLD_WIDTH - 3)
            top = heights[trunk_x]
            if top - 4 < 1:
                continue
            for offset in range(1, 4):
                self.world[top - offset][trunk_x] = "wood"
            leaf_y = top - 4
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    tx = trunk_x + dx
                    ty = leaf_y + dy
                    if 0 <= tx < WORLD_WIDTH and 0 <= ty < WORLD_HEIGHT:
                        if self.world[ty][tx] is None:
                            self.world[ty][tx] = "leaf"

    def spawn_initial_enemies(self):
        for index in range(4):
            self.enemies.append(
                Entity(
                    (18 + index * 7) * TILE_SIZE,
                    3 * TILE_SIZE,
                    24,
                    38,
                    "#C44536",
                    health=4,
                )
            )

    def on_key_press(self, event):
        key = event.keysym.lower()
        self.keys.add(key)
        if key in {"1", "2", "3", "4", "5"}:
            self.selected_slot = int(key) - 1
        elif key == "j":
            self.player_attack()
        elif key == "r" and self.game_over:
            self.respawn_player()

    def on_key_release(self, event):
        key = event.keysym.lower()
        self.keys.discard(key)

    def on_mouse_move(self, event):
        self.mouse_world = (event.x + self.camera_x, event.y + self.camera_y)

    def on_mouse_wheel(self, event):
        direction = -1 if event.delta < 0 else 1
        self.selected_slot = (self.selected_slot + direction) % HOTBAR_SIZE

    def on_left_click(self, event):
        if self.game_over:
            return
        world_x = event.x + self.camera_x
        world_y = event.y + self.camera_y
        self.mine_block(world_x, world_y)

    def on_right_click(self, event):
        if self.game_over:
            return
        world_x = event.x + self.camera_x
        world_y = event.y + self.camera_y
        self.place_block(world_x, world_y)

    def game_loop(self):
        self.update()
        self.draw()
        self.root.after(16, self.game_loop)

    def update(self):
        if self.message_timer > 0:
            self.message_timer -= 1

        if self.game_over:
            return

        self.handle_player_input()
        self.apply_physics(self.player)

        for enemy in list(self.enemies):
            self.update_enemy(enemy)

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        self.enemy_spawn_timer -= 1
        if self.enemy_spawn_timer <= 0 and len(self.enemies) < 7:
            self.spawn_enemy_near_player()
            self.enemy_spawn_timer = 300

        self.camera_x = max(
            0,
            min(
                int(self.player.x - CANVAS_WIDTH / 2),
                WORLD_WIDTH * TILE_SIZE - CANVAS_WIDTH,
            ),
        )
        self.camera_y = max(
            0,
            min(
                int(self.player.y - CANVAS_HEIGHT / 2),
                WORLD_HEIGHT * TILE_SIZE - CANVAS_HEIGHT,
            ),
        )

    def handle_player_input(self):
        moving_left = "a" in self.keys or "left" in self.keys
        moving_right = "d" in self.keys or "right" in self.keys

        self.player.vx = 0
        if moving_left:
            self.player.vx -= MOVE_SPEED * TILE_SIZE / 2
            self.player.direction = -1
        if moving_right:
            self.player.vx += MOVE_SPEED * TILE_SIZE / 2
            self.player.direction = 1

        if ("w" in self.keys or "up" in self.keys or "space" in self.keys) and self.player.on_ground:
            self.player.vy = JUMP_SPEED
            self.player.on_ground = False

    def apply_physics(self, entity):
        entity.vy = min(entity.vy + GRAVITY, MAX_FALL_SPEED)
        entity.x += entity.vx
        self.resolve_horizontal(entity)
        entity.y += entity.vy
        self.resolve_vertical(entity)

    def resolve_horizontal(self, entity):
        if entity.vx == 0:
            return
        left = int(entity.x // TILE_SIZE)
        right = int((entity.x + entity.width - 1) // TILE_SIZE)
        top = int(entity.y // TILE_SIZE)
        bottom = int((entity.y + entity.height - 1) // TILE_SIZE)
        for ty in range(top, bottom + 1):
            for tx in range(left, right + 1):
                if self.is_solid(tx, ty):
                    if entity.vx > 0:
                        entity.x = tx * TILE_SIZE - entity.width
                    else:
                        entity.x = (tx + 1) * TILE_SIZE
                    entity.vx = 0
                    return

    def resolve_vertical(self, entity):
        entity.on_ground = False
        left = int(entity.x // TILE_SIZE)
        right = int((entity.x + entity.width - 1) // TILE_SIZE)
        top = int(entity.y // TILE_SIZE)
        bottom = int((entity.y + entity.height - 1) // TILE_SIZE)
        for ty in range(top, bottom + 1):
            for tx in range(left, right + 1):
                if self.is_solid(tx, ty):
                    if entity.vy > 0:
                        entity.y = ty * TILE_SIZE - entity.height
                        entity.on_ground = True
                    else:
                        entity.y = (ty + 1) * TILE_SIZE
                    entity.vy = 0
                    return

        if entity.y > WORLD_HEIGHT * TILE_SIZE:
            if entity is self.player:
                self.damage_player(10)
            else:
                entity.health = 0

    def update_enemy(self, enemy):
        dx = self.player.x - enemy.x
        if abs(dx) < TILE_SIZE * 10:
            enemy.direction = 1 if dx > 0 else -1
        else:
            if random.random() < 0.02:
                enemy.direction *= -1

        enemy.vx = enemy.direction * 2
        if enemy.on_ground and random.random() < 0.015:
            enemy.vy = -6.5

        self.apply_physics(enemy)

        if self.entities_touch(enemy, self.player):
            self.damage_player(1)
            enemy.vx *= -1

        if enemy.health <= 0:
            self.enemies.remove(enemy)
            self.show_message("击败怪物了")

    def player_attack(self):
        if self.attack_cooldown > 0 or self.game_over:
            return

        self.attack_cooldown = 18
        px, py = self.player.center()
        hit_enemy = False
        for enemy in self.enemies:
            ex, ey = enemy.center()
            distance = math.hypot(ex - px, ey - py)
            facing = (ex - px) * self.player.direction >= -10
            if distance <= ATTACK_RANGE and facing:
                enemy.health -= 2
                enemy.vx = self.player.direction * 6
                enemy.vy = -3
                hit_enemy = True

        if hit_enemy:
            self.show_message("攻击命中")
        else:
            self.show_message("挥空了")

    def damage_player(self, amount):
        if self.game_over:
            return
        self.player.health -= amount
        self.show_message(f"受到 {amount} 点伤害")
        if self.player.health <= 0:
            self.player.health = 0
            self.game_over = True
            self.show_message("你被击败了，按 R 复活")

    def respawn_player(self):
        self.player.x, self.player.y = self.player_spawn
        self.player.vx = 0
        self.player.vy = 0
        self.player.health = 10
        self.game_over = False
        self.show_message("已复活")

    def spawn_enemy_near_player(self):
        offset_tiles = random.choice([-12, -10, 10, 12])
        spawn_x = max(2, min(WORLD_WIDTH - 3, int(self.player.x // TILE_SIZE) + offset_tiles))
        enemy = Entity(spawn_x * TILE_SIZE, 2 * TILE_SIZE, 24, 38, "#C44536", health=4)
        self.enemies.append(enemy)

    def mine_block(self, world_x, world_y):
        tx = int(world_x // TILE_SIZE)
        ty = int(world_y // TILE_SIZE)

        if not self.in_bounds(tx, ty):
            return

        block = self.world[ty][tx]
        if block is None:
            self.show_message("这里没有方块")
            return

        player_cx, player_cy = self.player.center()
        distance = math.hypot(tx * TILE_SIZE + TILE_SIZE / 2 - player_cx, ty * TILE_SIZE + TILE_SIZE / 2 - player_cy)
        if distance > TILE_SIZE * 4:
            self.show_message("离得太远，挖不到")
            return

        self.world[ty][tx] = None
        drop = BLOCKS[block]["drops"]
        self.inventory[drop] = self.inventory.get(drop, 0) + 1
        self.show_message(f"获得 {drop} x1")

    def place_block(self, world_x, world_y):
        tx = int(world_x // TILE_SIZE)
        ty = int(world_y // TILE_SIZE)

        if not self.in_bounds(tx, ty):
            return
        if self.world[ty][tx] is not None:
            self.show_message("这个位置已经有方块")
            return

        selected_item = self.hotbar[self.selected_slot]
        if self.inventory.get(selected_item, 0) <= 0:
            self.show_message("背包里没有这个方块")
            return

        player_cx, player_cy = self.player.center()
        distance = math.hypot(tx * TILE_SIZE + TILE_SIZE / 2 - player_cx, ty * TILE_SIZE + TILE_SIZE / 2 - player_cy)
        if distance > TILE_SIZE * 4:
            self.show_message("离得太远，放不了")
            return

        future_left = tx * TILE_SIZE
        future_top = ty * TILE_SIZE
        if self.rect_overlap(
            future_left,
            future_top,
            TILE_SIZE,
            TILE_SIZE,
            self.player.x,
            self.player.y,
            self.player.width,
            self.player.height,
        ):
            self.show_message("不能把自己卡进方块里")
            return

        self.world[ty][tx] = selected_item
        self.inventory[selected_item] -= 1
        self.show_message(f"放置了 {selected_item}")

    def draw(self):
        self.canvas.delete("all")
        self.draw_background()
        self.draw_world()
        self.draw_entities()
        self.draw_crosshair()
        self.draw_ui()

    def draw_background(self):
        self.canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill="#89CFF0", outline="")
        self.canvas.create_oval(40, 40, 120, 120, fill="#FFD166", outline="")
        for cloud_x in (140, 360, 620):
            self.canvas.create_oval(cloud_x, 70, cloud_x + 90, 115, fill="#F8FAFC", outline="")
            self.canvas.create_oval(cloud_x + 35, 45, cloud_x + 125, 105, fill="#F8FAFC", outline="")

    def draw_world(self):
        start_x = max(0, self.camera_x // TILE_SIZE)
        end_x = min(WORLD_WIDTH, (self.camera_x + CANVAS_WIDTH) // TILE_SIZE + 2)
        start_y = max(0, self.camera_y // TILE_SIZE)
        end_y = min(WORLD_HEIGHT, (self.camera_y + CANVAS_HEIGHT) // TILE_SIZE + 2)

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                block = self.world[y][x]
                if block is None:
                    continue
                screen_x = x * TILE_SIZE - self.camera_x
                screen_y = y * TILE_SIZE - self.camera_y
                self.canvas.create_rectangle(
                    screen_x,
                    screen_y,
                    screen_x + TILE_SIZE,
                    screen_y + TILE_SIZE,
                    fill=BLOCKS[block]["color"],
                    outline="#2D2D2D",
                )
                if block == "grass":
                    self.canvas.create_rectangle(
                        screen_x,
                        screen_y,
                        screen_x + TILE_SIZE,
                        screen_y + 7,
                        fill="#7ED957",
                        outline="",
                    )

    def draw_entities(self):
        for enemy in self.enemies:
            self.draw_entity(enemy)

        self.draw_entity(self.player)

        if self.attack_cooldown > 12:
            px, py = self.player.center()
            reach_x = px - self.camera_x + self.player.direction * 32
            self.canvas.create_arc(
                reach_x - 28,
                py - self.camera_y - 30,
                reach_x + 28,
                py - self.camera_y + 30,
                start=300 if self.player.direction > 0 else 60,
                extent=120,
                style=tk.ARC,
                outline="#FFE66D",
                width=3,
            )

    def draw_entity(self, entity):
        x1 = entity.x - self.camera_x
        y1 = entity.y - self.camera_y
        x2 = x1 + entity.width
        y2 = y1 + entity.height
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=entity.color, outline="#111")
        eye_x = x2 - 8 if entity.direction > 0 else x1 + 8
        self.canvas.create_oval(eye_x - 3, y1 + 10, eye_x + 3, y1 + 16, fill="white", outline="")

    def draw_crosshair(self):
        mx = self.mouse_world[0] - self.camera_x
        my = self.mouse_world[1] - self.camera_y
        self.canvas.create_line(mx - 8, my, mx + 8, my, fill="#1F2937", width=2)
        self.canvas.create_line(mx, my - 8, mx, my + 8, fill="#1F2937", width=2)

    def draw_ui(self):
        self.canvas.create_rectangle(18, 16, 260, 44, fill="#000000", outline="", stipple="gray25")
        self.canvas.create_text(
            28,
            30,
            anchor="w",
            text=f"生命值: {self.player.health}/10   怪物: {len(self.enemies)}",
            fill="white",
            font=("Microsoft YaHei UI", 12, "bold"),
        )

        hotbar_width = HOTBAR_SIZE * 88
        base_x = (CANVAS_WIDTH - hotbar_width) // 2
        base_y = CANVAS_HEIGHT - 88
        for index, item in enumerate(self.hotbar):
            slot_x = base_x + index * 88
            selected = index == self.selected_slot
            self.canvas.create_rectangle(
                slot_x,
                base_y,
                slot_x + 74,
                base_y + 74,
                fill="#FFF8E7" if selected else "#E5E7EB",
                outline="#F59E0B" if selected else "#6B7280",
                width=4 if selected else 2,
            )
            self.canvas.create_rectangle(
                slot_x + 20,
                base_y + 14,
                slot_x + 54,
                base_y + 48,
                fill=ITEM_COLORS[item],
                outline="#374151",
            )
            self.canvas.create_text(
                slot_x + 37,
                base_y + 58,
                text=f"{index + 1}",
                fill="#111827",
                font=("Consolas", 10, "bold"),
            )
            self.canvas.create_text(
                slot_x + 37,
                base_y + 66,
                text=f"{item}:{self.inventory.get(item, 0)}",
                fill="#111827",
                font=("Consolas", 8),
            )

        inventory_text = " | ".join(f"{name}:{self.inventory.get(name, 0)}" for name in self.hotbar)
        self.canvas.create_rectangle(16, CANVAS_HEIGHT - 130, 530, CANVAS_HEIGHT - 98, fill="#000000", outline="", stipple="gray25")
        self.canvas.create_text(
            24,
            CANVAS_HEIGHT - 114,
            anchor="w",
            text=f"物品栏: {inventory_text}",
            fill="white",
            font=("Microsoft YaHei UI", 10),
        )

        if self.message_timer > 0:
            self.canvas.create_rectangle(16, 52, 590, 84, fill="#000000", outline="", stipple="gray25")
            self.canvas.create_text(
                28,
                68,
                anchor="w",
                text=self.message,
                fill="#F8FAFC",
                font=("Microsoft YaHei UI", 10),
            )

        if self.game_over:
            self.canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill="#000000", outline="", stipple="gray50")
            self.canvas.create_text(
                CANVAS_WIDTH / 2,
                CANVAS_HEIGHT / 2 - 20,
                text="你被击败了",
                fill="white",
                font=("Microsoft YaHei UI", 28, "bold"),
            )
            self.canvas.create_text(
                CANVAS_WIDTH / 2,
                CANVAS_HEIGHT / 2 + 20,
                text="按 R 复活继续",
                fill="#FDE68A",
                font=("Microsoft YaHei UI", 16),
            )

    def show_message(self, text):
        self.message = text
        self.message_timer = 180

    def is_solid(self, tx, ty):
        if not self.in_bounds(tx, ty):
            return False
        block = self.world[ty][tx]
        return block is not None and BLOCKS[block]["solid"]

    def in_bounds(self, tx, ty):
        return 0 <= tx < WORLD_WIDTH and 0 <= ty < WORLD_HEIGHT

    def entities_touch(self, a, b):
        return self.rect_overlap(a.x, a.y, a.width, a.height, b.x, b.y, b.width, b.height)

    @staticmethod
    def rect_overlap(ax, ay, aw, ah, bx, by, bw, bh):
        return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Game().run()
