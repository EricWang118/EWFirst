import random
import tkinter as tk


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
TILE_WIDTH = 72
TILE_HEIGHT = 84
SLOT_LIMIT = 7
CARD_TYPES = [
    ("Yang", "#F2C14E"),
    ("Cao", "#6AB04A"),
    ("Ling", "#22A6B3"),
    ("Mao", "#EB4D4B"),
    ("Nai", "#F8A5C2"),
    ("Yun", "#A29BFE"),
    ("Hua", "#E056FD"),
    ("Guo", "#FF9F43"),
    ("Xing", "#7ED6DF"),
]


class Tile:
    def __init__(self, tile_id, kind, row, col, layer):
        self.tile_id = tile_id
        self.kind = kind
        self.row = row
        self.col = col
        self.layer = layer
        self.removed = False

    @property
    def x(self):
        return 120 + self.col * 86 + self.layer * 10

    @property
    def y(self):
        return 95 + self.row * 92 + self.layer * 10

    def contains(self, px, py):
        return self.x <= px <= self.x + TILE_WIDTH and self.y <= py <= self.y + TILE_HEIGHT


class SheepMatchGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sheep Match")
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bg="#FFF7E6",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.tiles = []
        self.slot_tiles = []
        self.message = "Click a free tile. Match 3 of the same kind to clear."
        self.game_state = "playing"
        self.score = 0
        self.level = 1
        self.history = []

        self.root.bind("<Button-1>", self.on_click)
        self.root.bind("<KeyPress-r>", self.on_restart)
        self.root.bind("<KeyPress-R>", self.on_restart)
        self.root.bind("<KeyPress-z>", self.on_undo)
        self.root.bind("<KeyPress-Z>", self.on_undo)

        self.setup_level()
        self.loop()

    def setup_level(self):
        self.tiles.clear()
        self.slot_tiles.clear()
        self.history.clear()
        self.game_state = "playing"

        layouts = {
            1: [6, 5, 4],
            2: [6, 6, 5, 4],
            3: [7, 6, 6, 5],
        }
        layers = layouts.get(self.level, [7, 7, 6, 5])

        positions = []
        for layer, size in enumerate(layers):
            for row in range(size):
                for col in range(size):
                    positions.append((row, col, layer))

        usable_tile_count = len(positions) - (len(positions) % 3)
        random.shuffle(positions)
        positions = positions[:usable_tile_count]

        triplet_count = usable_tile_count // 3
        kinds = [CARD_TYPES[index % len(CARD_TYPES)] for index in range(triplet_count) for _ in range(3)]
        random.shuffle(kinds)

        for tile_id, ((row, col, layer), kind) in enumerate(zip(positions, kinds)):
            self.tiles.append(Tile(tile_id, kind, row, col, layer))

        random.shuffle(self.tiles)
        self.message = f"Level {self.level} start. Press R to restart, Z to undo."

    def on_click(self, event):
        if self.game_state == "cleared":
            self.level += 1
            self.setup_level()
            return

        if self.game_state != "playing":
            return

        tile = self.find_clickable_tile(event.x, event.y)
        if tile is None:
            self.message = "No clickable tile here."
            return

        self.pick_tile(tile)

    def find_clickable_tile(self, x, y):
        candidates = []
        for tile in self.tiles:
            if tile.removed:
                continue
            if tile.contains(x, y):
                candidates.append(tile)

        candidates.sort(key=lambda item: item.layer, reverse=True)
        for tile in candidates:
            if not self.is_blocked(tile):
                return tile
        return None

    def pick_tile(self, tile):
        snapshot = (
            tile,
            list(self.slot_tiles),
            self.score,
            self.game_state,
        )
        self.history.append(snapshot)

        tile.removed = True
        self.slot_tiles.append(tile.kind)
        self.score += 10

        matched_name = self.resolve_matches()

        if all(item.removed for item in self.tiles):
            self.game_state = "cleared"
            self.message = "Level cleared. Click anywhere for next level."
        elif len(self.slot_tiles) >= SLOT_LIMIT:
            self.game_state = "failed"
            self.message = "Slots are full. Press R to restart."
        elif matched_name:
            self.message = f"Matched 3 x {matched_name}."
        else:
            self.message = f"Picked {tile.kind[0]}. Keep matching."

    def resolve_matches(self):
        counts = {}
        for kind in self.slot_tiles:
            counts[kind[0]] = counts.get(kind[0], 0) + 1

        for name, total in counts.items():
            if total >= 3:
                removed = 0
                new_slot = []
                for kind in self.slot_tiles:
                    if kind[0] == name and removed < 3:
                        removed += 1
                    else:
                        new_slot.append(kind)
                self.slot_tiles = new_slot
                self.score += 90
                return name
        return None

    def is_blocked(self, tile):
        for other in self.tiles:
            if other.removed or other.layer <= tile.layer:
                continue
            overlap = not (
                other.x > tile.x + TILE_WIDTH - 16
                or other.x + TILE_WIDTH - 16 < tile.x
                or other.y > tile.y + TILE_HEIGHT - 16
                or other.y + TILE_HEIGHT - 16 < tile.y
            )
            if overlap:
                return True
        return False

    def on_restart(self, _event=None):
        self.score = 0
        self.level = 1
        self.setup_level()

    def on_undo(self, _event=None):
        if self.game_state != "playing" or not self.history:
            self.message = "Undo is not available right now."
            return

        tile, previous_slots, previous_score, previous_state = self.history.pop()
        tile.removed = False
        self.slot_tiles = previous_slots
        self.score = previous_score
        self.game_state = previous_state
        self.message = "Undid the last move."

    def loop(self):
        self.draw()
        self.root.after(16, self.loop)

    def draw(self):
        self.canvas.delete("all")
        self.draw_background()
        self.draw_board()
        self.draw_slots()
        self.draw_ui()

    def draw_background(self):
        self.canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill="#FFF4D6", outline="")
        self.canvas.create_oval(-50, -60, 200, 180, fill="#FFD166", outline="")
        self.canvas.create_oval(710, 40, 900, 150, fill="#FFFFFF", outline="")
        self.canvas.create_oval(760, 10, 950, 120, fill="#FFFFFF", outline="")
        self.canvas.create_rectangle(50, 70, 910, 560, fill="#FFFDF7", outline="#E4C97B", width=4)

    def draw_board(self):
        for tile in sorted(self.tiles, key=lambda item: item.layer):
            if tile.removed:
                continue
            blocked = self.is_blocked(tile)
            self.draw_tile(tile.x, tile.y, tile.kind, blocked)

    def draw_tile(self, x, y, kind, blocked):
        name, color = kind
        shadow = "#D8C39B" if not blocked else "#B6A58D"
        fill = color if not blocked else "#CFC8BF"
        text_color = "#2D3436" if not blocked else "#7F8C8D"

        self.canvas.create_rectangle(x + 5, y + 7, x + TILE_WIDTH + 5, y + TILE_HEIGHT + 7, fill=shadow, outline="")
        self.canvas.create_rectangle(x, y, x + TILE_WIDTH, y + TILE_HEIGHT, fill="#FFF8EA", outline="#9C7C38", width=2)
        self.canvas.create_rectangle(x + 8, y + 8, x + TILE_WIDTH - 8, y + TILE_HEIGHT - 8, fill=fill, outline="")
        self.canvas.create_text(
            x + TILE_WIDTH / 2,
            y + TILE_HEIGHT / 2 - 6,
            text=name,
            fill=text_color,
            font=("Microsoft YaHei UI", 18, "bold"),
        )
        self.canvas.create_text(
            x + TILE_WIDTH / 2,
            y + TILE_HEIGHT - 18,
            text="FREE" if not blocked else "BLOCK",
            fill=text_color,
            font=("Consolas", 9, "bold"),
        )

    def draw_slots(self):
        self.canvas.create_text(
            100,
            595,
            anchor="w",
            text="Slots",
            fill="#7A5C1E",
            font=("Microsoft YaHei UI", 16, "bold"),
        )

        start_x = 180
        y = 610
        for index in range(SLOT_LIMIT):
            x = start_x + index * 92
            self.canvas.create_rectangle(x, y, x + 78, y + 90, fill="#FBF1D8", outline="#C8A96B", width=3)
            if index < len(self.slot_tiles):
                self.draw_slot_card(x + 3, y + 3, self.slot_tiles[index])

    def draw_slot_card(self, x, y, kind):
        name, color = kind
        self.canvas.create_rectangle(x, y, x + 72, y + 84, fill="#FFF8EA", outline="#9C7C38", width=2)
        self.canvas.create_rectangle(x + 8, y + 8, x + 64, y + 76, fill=color, outline="")
        self.canvas.create_text(
            x + 36,
            y + 38,
            text=name,
            fill="#2D3436",
            font=("Microsoft YaHei UI", 16, "bold"),
        )

    def draw_ui(self):
        self.canvas.create_rectangle(36, 18, 924, 58, fill="#FFFDF7", outline="#E4C97B", width=3)
        self.canvas.create_text(
            56,
            38,
            anchor="w",
            text=f"Sheep Match   Score: {self.score}   Level: {self.level}",
            fill="#6D4C13",
            font=("Microsoft YaHei UI", 15, "bold"),
        )
        self.canvas.create_text(
            36,
            575,
            anchor="w",
            text=self.message,
            fill="#6B4F1D",
            font=("Microsoft YaHei UI", 12),
        )

        self.canvas.create_text(
            735,
            610,
            anchor="w",
            text="Rules",
            fill="#7A5C1E",
            font=("Microsoft YaHei UI", 16, "bold"),
        )
        self.canvas.create_text(
            735,
            635,
            anchor="w",
            text="1. Only free top tiles can be clicked",
            fill="#6B4F1D",
            font=("Microsoft YaHei UI", 10),
        )
        self.canvas.create_text(
            735,
            658,
            anchor="w",
            text="2. Match 3 same tiles to clear",
            fill="#6B4F1D",
            font=("Microsoft YaHei UI", 10),
        )
        self.canvas.create_text(
            735,
            681,
            anchor="w",
            text="3. 7 tiles in slots means game over",
            fill="#6B4F1D",
            font=("Microsoft YaHei UI", 10),
        )

        if self.game_state == "failed":
            self.draw_overlay("Failed", "Press R to restart")
        elif self.game_state == "cleared":
            self.draw_overlay("Cleared", "Click anywhere for next level")

    def draw_overlay(self, title, subtitle):
        self.canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill="#000000", outline="", stipple="gray25")
        self.canvas.create_rectangle(260, 220, 700, 430, fill="#FFF8EA", outline="#E4C97B", width=5)
        self.canvas.create_text(
            WINDOW_WIDTH / 2,
            290,
            text=title,
            fill="#7A4F01",
            font=("Microsoft YaHei UI", 28, "bold"),
        )
        self.canvas.create_text(
            WINDOW_WIDTH / 2,
            345,
            text=subtitle,
            fill="#8C6C2A",
            font=("Microsoft YaHei UI", 16),
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    SheepMatchGame().run()
