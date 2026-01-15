import pygame
import random
import math 
from collections import Counter

# --------- CONFIG ----------- #
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800

BGM_FILE = "music/disco.mp3"
BGM_VOLUME = 1.0

# ---- WINDOW1: ANIMATION ASSET CONFIG ---- #
ANIM_FRAME_FILES = ["assets/sheep1.png", "assets/sheep2.png", "assets/sheep3.png"]
ANIM_FRAME_DURATION = 200

BG_FILE = "assets/background.png"
START_TITLE_FILE = "assets/title.png"
START_BUTTON_FILE = "assets/button_start.png"

BUTTON_HOVER_SCALE = 1.08
BUTTON_HOVER_LERP = 0.25

# ---- TRANSITION ---- #
TRANS_BOARD_FILE = "assets/hardashell.png"
TRANS_BOARD_W, TRANS_BOARD_H = 350, 94
TRANS_IN_MS = 500
TRANS_HOLD_MS = 450
TRANS_OUT_MS = 500

# ---- WINDOW2&3: PLAY ---- #
# tiles
STACK_CAPACITY = 7
TILE_WIDTH = 48
TILE_HEIGHT = 60
TILE_IMG_FILES_L1 = [f"assets/card{i}.png" for i in range(1, 4)]
TILE_IMG_FILES_L2 = [f"assets/card{i}.png" for i in range(1, 16)]
N_TYPES_L1 = 3
N_TYPES_L2 = 15
TILES_PER_TYPE = 6

# stack box
STACK_BOX_FILE = "assets/box.png"
STACK_BOX_W = 392
STACK_BOX_H = 106
STACK_BOX_MARGIN_BOTTOM = 12

# layout
GRID_COLS = 3
GRID_ROWS = 3
LAYER_COUNT = 2

LEVEL2_LAYOUT = [
    # layer 0
    [(57, 95), (105, 95), (297, 95), (345, 95), 
     (57, 155), (345, 155), 
     (57, 215), (153, 215), (249, 215), (345, 215), 
     (153, 275), (249, 275), 
     (105, 365), (297, 365), 
     (153, 425), (249, 425), 
     (57, 485), (345, 485)],
    
    # layer 1
    [(129, 95), (273, 95),
     (57, 125), (345, 125),
     (57, 185), (345, 185),
     (177, 245), (225, 245),
     (129, 395), (273, 395),
     (57, 491), (345, 491)],

    # layer 2
    [(57, 95), (345, 95),
     (57, 155), (345, 155),
     (57, 215), (153, 215), (249, 215), (345, 215),
     (153, 215), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425),
     (57, 497), (345, 497)],

    # layer 3
    [(177, 245), (225, 245),
     (129, 395), (273, 395),
     (57, 503), (345, 503)],
    
    # layer 4
    [(153, 215), (249, 215),
     (153, 275), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425),
     (57, 509), (345, 509)],

    # layer 5
    [(177, 245), (225, 245),
     (129, 395), (273, 395),
     (57, 515), (345, 515)],

    # layer 6
    [(153, 215), (249, 215),
     (153, 275), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425),
     (57, 521), (345, 521)],
    
    # layer 7
    [(177, 245), (225, 245),
     (129, 395), (273, 395),
     (57, 527), (345, 527)],

    # layer 8
    [(153, 215), (249, 215),
     (153, 275), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425),
     (57, 533), (345, 533)],

    # layer 9
    [(177, 245), (225, 245),
     (129, 395), (273, 395),
     (57, 539), (345, 539)],

    # layer 10
    [(153, 215), (249, 215),
     (153, 275), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425),
     (57, 545), (345, 545)],

    # layer 11
    [(177, 245), (225, 245),
     (129, 395), (273, 395)],

    # layer 12
    [(153, 215), (249, 215),
     (153, 275), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425)],

    # layer 13
    [(177, 245), (225, 245),
     (129, 395), (273, 395)],

    # layer 14
    [(153, 215), (249, 215),
     (153, 275), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425)],

    # layer 15
    [(177, 245), (225, 245),
     (129, 395), (273, 395)],

    # layer 16
    [(153, 215), (249, 215),
     (153, 275), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425)],

    # layer 17
    [(177, 245), (225, 245),
     (129, 395), (273, 395)],

    # layer 18
    [(153, 215), (249, 215),
     (153, 275), (249, 275),
     (105, 365), (297, 365),
     (153, 425), (249, 425)],

    # layer 19
    [(129, 185), (177, 185), (225, 185), (273, 185),
     (129, 245), (177, 245), (225, 245), (273, 245),
     (177, 305), (225, 305),
     (81, 335), (129, 335), (273, 335), (321, 335),
     (81, 395), (129, 395), (177, 395), (225, 395), (273, 395), (321, 395),
     (129, 455), (177, 455), (225, 455), (273, 455)],

    # layer 20
    [(105, 155), (153, 155), (201, 155), (249, 155), (297, 155),
     (105, 215), (153, 215), (201, 215), (249, 215), (297, 215),
     (57, 305), (105, 305), (153, 305), (249, 305), (297, 305), (345, 305),
     (57, 365), (105, 365), (153, 365), (249, 365), (297, 365), (345, 365),
     (57, 425), (105, 425), (153, 425), (249, 425), (297, 425), (345, 425),
     (105, 485), (153, 485), (249, 485), (297, 485)],

    # layer 21
    [(81, 275), (129, 275), (177, 275), (225, 275), (273, 275), (321, 275),
     (129, 335), (177, 335), (225, 335), (273, 335),
     (177, 395), (225, 395),
     (177, 455), (225, 455),
     (177, 515), (225, 515)],

    # layer 22
    [(201, 305), 
     (201, 365),
     (201, 425),
     (201, 485)]
]

# offset for layer1 to overlap layer0
LAYER_OFFSET_X = 0
LAYER_OFFSET_Y = 6

# level sign
LEVEL_LABEL_L1_FILE = "assets/levelsign1.png"
LEVEL_LABEL_L2_FILE = "assets/levelsign2.png"
LEVEL_LABEL_Y = 18


# --- WINDOW4: END --- #
MAX_LEVEL = 2
END_TITLE_Y = 140
END_BUTTON_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 160)
RESTART_BUTTON_FILE = "assets/button_restart.png"

END_BOARD_W, END_BOARD_H = 266, 226
END_WIN_FRAMES = [f"assets/win{i}.png" for i in range(1,34)]
END_LOSE_FRAMES = [f"assets/lose{i}.png" for i in range(1,5)]
END_ANIM_FRAMES_MS = 90

# -------- CLASS --------- #
class Tile:
    def __init__(self, id_, kind, layer, x, y, w, h):
        self.id = id_
        self.kind = kind
        self.layer = layer
        self.x = x
        self.y = y

        self.draw_x = float(x)
        self.draw_y = float(-120 - random.randint(0, 200))

        self.w = w
        self.h = h
        self.alive = True

        self.spawn_t = 0
        self.spawn_dur = 450 + random.randint(0, 200)
        
        self.state = "spawning"
        self.stack_target_item = None 
        self.fly_speed = 1400.0

    def rect(self):
        return pygame.Rect(int(self.draw_x), int(self.draw_y), self.w, self.h)
    
    def start_fly_to_stack(self, target_stack_item):
        self.state = "flying"
        self.stack_target_item = target_stack_item
    
    def update(self, dt):
        dt_sec = dt / 1000.0
        if self.state == "spawning":
            if self.spawn_t < self.spawn_dur:
                self.spawn_t += dt
                t = min(1.0, self.spawn_t / self.spawn_dur)
                t = 1 - (1 - t) ** 3
                self.draw_x = self.x
                self.draw_y = (1 - t) * (-120) + t * self.y
            else:
                self.draw_x = self.x
                self.draw_y = self.y
                self.state = "board"
        elif self.state == "board":
            self.draw_x = self.x
            self.draw_y = self.y
        elif self.state == "flying":
            # fly toward the reserved stack slot target
            tx = float(self.stack_target_item.tx)
            ty = float(self.stack_target_item.ty)
            
            dx = tx - self.draw_x
            dy = ty - self.draw_y
            dist = (dx*dx + dy*dy) ** 0.5

            if dist < 2.0:
                # arrived
                self.draw_x, self.draw_y = tx, ty
                self.alive = False
                self.state = "dead"
                # reveal the reserved stack item now
                self.stack_target_item.visible = True
                self.stack_target_item.just_arrived = True 
            else:
                step = self.fly_speed * dt_sec
                if step >= dist:
                    self.draw_x, self.draw_y = tx, ty
                else:
                    self.draw_x += dx / dist * step
                    self.draw_y += dy / dist * step 

class StackItem:
    def __init__(self, kind, x, y, w, h):
        self.kind = kind
        
        self.x, self.y = float(x), float(y)
        self.tx, self.ty = float(x), float(y)

        self.w = w
        self.h = h

        self.visible = True 
        self.state = "normal"
        self.clear_t = 0
        self.clear_dur = 220
        self.move_speed = 1200.0

        self.just_arrived = False 

    def update(self, dt):
        # dt in ms
        dt_sec = dt / 1000.0
        dx = self.tx - self.x
        dy = self.ty - self.y
        dist = (dx*dx+dy*dy) ** 0.5
        if dist > 0.5:
            step = self.move_speed * dt_sec
            if step >= dist:
                self.x, self.y = self.tx, self.ty 
            else:
                self.x += dx / dist * step 
                self.y += dy / dist * step 

        if self.state == "clearing":
            self.clear_t += dt 

    def is_clear_done(self):
        return self.state == "clearing" and self.clear_t >= self.clear_dur 

# ------------ HELPER FUNCTIONS ------------- #
def is_tile_blocked(tile, tiles):
    """Tile is blocked if any alive tile with higher layer overlapys it"""
    if not tile.alive or tile.state != "board":
        return True
    r = tile.rect()
    for other in tiles:
        if not other.alive or other.state != "board":
            continue
        if other.layer <= tile.layer:
            continue 
        if other.rect().colliderect(r):
            return True
    return False 

def is_tile_clickable(tile, tiles):
    return tile.alive and tile.state == "board" and not is_tile_blocked(tile, tiles)

def find_clicked_tile(mx, my, tiles):
    """Return the TOPMOST alive tile under the mouse, if any"""
    candidates = []
    for t in tiles:
        if t.alive and t.state == "board" and t.rect().collidepoint(mx, my):
            candidates.append(t)
    if not candidates:
        return None
    # choose the one with highest layer
    candidates.sort(key=lambda t: t.layer, reverse=True)
    return candidates[0]

def load_images_scaled(paths, size):
    out = []
    for p in paths:
        img = pygame.image.load(p).convert_alpha()
        if img.get_width() != size[0] or img.get_height() != size[1]:
            img = pygame.transform.smoothscale(img, size)
        out.append(img)
    return out 

def darken_surface(surf, amount=90, radius=6):
    s = surf.copy()
    w,h = s.get_size()
    alpha = max(0, min(255, amount))
    dark = pygame.Surface((w,h), pygame.SRCALPHA)
    pygame.draw.rect(dark, (0,0,0,alpha), (0,0,w,h), border_radius=radius)
    s.blit(dark, (0,0))
    return s 

def reset_level(level, n_types):
    if level == 1:
        tiles = generate_tiles(n_types)
    elif level == 2:
        tiles = generate_tiles_from_layout(LEVEL2_LAYOUT, n_types)
    else:
        tiles = generate_tiles(n_types)
    
    stack_items = []
    return tiles, stack_items

def is_level_cleared(tiles, stack_items):
    # no alive tiles
    any_tile_alive = any(t.alive for t in tiles)
    # include both bisible and reserved stack items
    any_stack_present = (visible_stack_count(stack_items) > 0)
    return (not any_tile_alive) and (not any_stack_present)

def ease_out_cubic(t):
    return 1 - (1 - t) ** 3

# --------- LEVEL GENERATION ------------ #
def generate_tiles(n_types):
    """
    layout:
    - layer0: 3x3 grid, center tile at screen center
    - layer1: 3x3 grid, offset slightly (y+6), drawn above layer0
    """
    kinds = []
    total_positions = 18
    per_type = total_positions // n_types 
    if per_type == 0:
        kinds = [i % n_types for i in range(total_positions)]
    else:
        for k in range(n_types):
            kinds.extend([k] * per_type)
        random.shuffle(kinds)

    positions = []

    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2

    x_offsets = [-2, 0, 2]
    y_offsets = [-2, 0, 2]

    # layer 0
    for oy in y_offsets:
        for ox in x_offsets:
            x = center_x + ox * TILE_WIDTH - TILE_WIDTH // 2
            y = center_y + oy * TILE_HEIGHT - TILE_HEIGHT // 2
            positions.append((0,x,y))

    # layer 1
    for oy in y_offsets:
        for ox in x_offsets:
            x = center_x + ox * TILE_WIDTH - TILE_WIDTH // 2 + LAYER_OFFSET_X
            y = center_y + oy * TILE_HEIGHT - TILE_HEIGHT // 2 + LAYER_OFFSET_Y
            positions.append((1,x,y))

    # ensure 
    positions = positions[:len(kinds)]

    tiles = []
    for i, kind in enumerate(kinds):
        layer, x, y = positions[i]
        tiles.append(Tile(i, kind, layer, x, y, TILE_WIDTH, TILE_HEIGHT))

    return tiles 

def generate_tiles_from_layout(layout_layers, n_types):
    tiles = []
    idx = 0
    for layer, positions in enumerate(layout_layers):
        for (x, y) in positions:
            kind = idx % n_types
            tiles.append(Tile(
                idx,
                kind,
                layer,
                x,
                y,
                TILE_WIDTH,
                TILE_HEIGHT
            ))
            idx += 1
    return tiles

# ---- STACK ---- #
def layout_stack_items(stack_items, first_x, first_y):
    for i, it in enumerate(stack_items):
        it.tx = first_x + i * TILE_WIDTH
        it.ty = first_y

def reserve_stack_slot_grouped(stack_items, kind, first_x, first_y):
    # find insertion point
    insert_at = visible_stack_count(stack_items)
    for i in range(visible_stack_count(stack_items)-1, -1, -1):
        if stack_items[i].visible and stack_items[i].state == "normal" and stack_items[i].kind == kind:
            insert_at = i + 1
            break
    # create reserved item (invisible until the tile arrives)
    spawn_x = first_x + visible_stack_count(stack_items) * TILE_WIDTH
    spawn_y = first_y
    reserved = StackItem(kind, spawn_x, spawn_y, TILE_WIDTH, TILE_HEIGHT)
    reserved.visible = False

    stack_items.insert(insert_at, reserved)
    layout_stack_items(stack_items, first_x, first_y)

    return reserved

def start_clear_if_any_triple(stack_items):
    i = 0
    changed = False
    while i < visible_stack_count(stack_items):
        # skip clearing items when scanning
        if (not stack_items[i].visible) or stack_items[i].state != "normal":
            i += 1
            continue
        k = stack_items[i].kind
        j = i
        while j < visible_stack_count(stack_items) and stack_items[j].visible and stack_items[j].kind == k and stack_items[j].state == "normal":
            j += 1
        run_len = j - i 
        if run_len >= 3:
            # mark exactly 3 to clear
            for t in stack_items[i:i+3]:
                t.state = "clearing"
                t.clear_t = 0
            changed = True 
            # skip past this run
            i = j
        else:
             i = j 
    return changed
    
def update_stack_and_cleanup(stack_items, dt, first_x, first_y):
    for it in stack_items:
        it.update(dt)
    # remove done-clearing
    before = visible_stack_count(stack_items)
    stack_items[:] = [it for it in stack_items if not it.is_clear_done()]
    removed = (visible_stack_count(stack_items) != before)
    if removed:
        layout_stack_items(stack_items, first_x, first_y)
    return removed

def visible_stack_count(stack_items):
    return sum(1 for it in stack_items if it.visible)

def has_visible_triple(stack_items):
    i = 0
    kinds = [it.kind for it in stack_items if it.visible and it.state == "normal"]
    while i < len(kinds):
        k = kinds[i]
        j = i
        while j < len(kinds) and kinds[j] == k:
            j += 1
        if (j - i) >= 3:
            return True
        i = j
    return False 

# --------- DRAWING ----------- #
def draw_tile(screen, tile, tile_images, tiles):
    if not tile.alive:
        return 
    img = tile_images[tile.kind % len(tile_images)]
    clickable = is_tile_clickable(tile, tiles)

    # darken blocked tiles
    if tile.state == "board" and not clickable:
        img = darken_surface(img, amount=110, radius=6)

    screen.blit(img, (int(tile.draw_x), int(tile.draw_y)))

def draw_stack_box_and_stack(screen, stack_box_img, stack_items, tile_images):
    box_x = (SCREEN_WIDTH - STACK_BOX_W) // 2
    box_y = SCREEN_HEIGHT - STACK_BOX_H - STACK_BOX_MARGIN_BOTTOM
    screen.blit(stack_box_img, (box_x, box_y))

    for it in stack_items:
        if not it.visible:
            continue
        img = tile_images[it.kind % len(tile_images)]

        if it.state == "clearing":
            p = min(1.0, it.clear_t / it.clear_dur)
            scale = max(0.05, 1.0 - p)
            w = int(TILE_WIDTH * scale)
            h = int(TILE_HEIGHT * scale)
            surf = pygame.transform.smoothscale(img, (w, h))
            cx = int(it.x + TILE_WIDTH / 2)
            cy = int(it.y + TILE_HEIGHT / 2)
            r = surf.get_rect(center=(cx, cy))
            screen.blit(surf, r)
        else:
            screen.blit(img, (int(it.x), int(it.y)))

def load_animation_frames():
    frames = []
    for fname in ANIM_FRAME_FILES:
        img = pygame.image.load(fname).convert_alpha()
        frames.append(img)
    return frames
    
# ------------- MAIN LOOP ----------------- #
def main():
    pygame.init()
    pygame.display.set_caption("OHHH! SHEEP")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # music
    pygame.mixer.init()
    pygame.mixer.music.load(BGM_FILE)
    pygame.mixer.music.play(loops=-1)

    # assets
    bg = pygame.image.load(BG_FILE).convert_alpha()
    if bg.get_size() != (SCREEN_WIDTH, SCREEN_HEIGHT):
        bg = pygame.transform.smoothscale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    start_title = pygame.image.load(START_TITLE_FILE).convert_alpha()
    start_button_img = pygame.image.load(START_BUTTON_FILE).convert_alpha()
    btn_w, btn_h = start_button_img.get_size()
    start_button_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 140)
    btn_scale = 1.0

    tile_images_l1 = load_images_scaled(TILE_IMG_FILES_L1, (TILE_WIDTH, TILE_HEIGHT))
    tile_images_l2 = load_images_scaled(TILE_IMG_FILES_L2, (TILE_WIDTH, TILE_HEIGHT))
    stack_box_img = pygame.image.load(STACK_BOX_FILE).convert_alpha()
    if stack_box_img.get_width() != STACK_BOX_W or stack_box_img.get_height() != STACK_BOX_H:
        stack_box_img = pygame.transform.smoothscale(stack_box_img, (STACK_BOX_W, STACK_BOX_H))

    level_label_l1 = pygame.image.load(LEVEL_LABEL_L1_FILE).convert_alpha()
    level_label_l2 = pygame.image.load(LEVEL_LABEL_L2_FILE).convert_alpha()

    trans_board = pygame.image.load(TRANS_BOARD_FILE).convert_alpha()

    end_win_anim = load_images_scaled(END_WIN_FRAMES, (END_BOARD_W, END_BOARD_H))
    end_lose_anim = load_images_scaled(END_LOSE_FRAMES, (END_BOARD_W, END_BOARD_H))
    end_anim_idx = 0
    end_anim_timer = 0

    restart_button_img = pygame.image.load(RESTART_BUTTON_FILE).convert_alpha()
    restart_btn_w, restart_btn_h = restart_button_img.get_size()
    restart_btn_scale = 1.0

    anim_frames = load_animation_frames()
    anim_index = 0
    anim_timer = 0
    circle_angle = 0.0
    game_state = "start"

    def restart_game():
        nonlocal game_state, level, tiles, stack_items, game_over, status_text, end_result
        level = 1
        tile_images = tile_images_l1
        n_types = N_TYPES_L1
        tiles = generate_tiles(n_types)
        stack_items = []
        stack_resolving_full = False 
        game_over = False 
        status_text = ""
        end_result = None 
        game_state = "play"
        transition_active = False
        transition_t = 0
    
    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                if game_state == "start":
                    cur_w = int(btn_w * btn_scale)
                    cur_h = int(btn_h * btn_scale)
                    start_button_rect = pygame.Rect(0,0, cur_w, cur_h)
                    start_button_rect.center = start_button_center
                    if start_button_rect.collidepoint(mx, my):
                        game_state = "play"
                        level = 1
                        tile_images = tile_images_l1
                        n_types = N_TYPES_L1
                        tiles, stack_items = reset_level(level, n_types)
                        stack_resolving_full = False 
                        game_over = False
                        status_text = ""
                        end_result = None 
                        transition_active = False
                        transition_t = 0
                elif game_state == "transition":
                    pass
                elif game_state == "play":
                    if game_over:
                        continue              
                    clicked = find_clicked_tile(mx, my, tiles)
                    if clicked and is_tile_clickable(clicked, tiles):
                        # compute stack box anchor each frame or store globally
                        box_x = (SCREEN_WIDTH - STACK_BOX_W) // 2
                        box_y = SCREEN_HEIGHT - STACK_BOX_H - STACK_BOX_MARGIN_BOTTOM
                        first_x = box_x + 28
                        first_y = box_y + 16
                        # reserve an invisible stack slot and fly the tile to it
                        reserved_item = reserve_stack_slot_grouped(stack_items, clicked.kind, first_x, first_y)
                        clicked.start_fly_to_stack(reserved_item)
                elif game_state == "end":
                    cur_w = int(restart_btn_w * restart_btn_scale)
                    cur_h = int(restart_btn_h * restart_btn_scale)
                    restart_rect = pygame.Rect(0, 0, cur_w, cur_h)
                    restart_rect.center = END_BUTTON_CENTER

                    if restart_rect.collidepoint(mx, my):
                        restart_game()

        # ------- DRAW --------- #
        screen.blit(bg, (0,0))
        if game_state == "start":
            anim_timer += dt
            if anim_timer >= ANIM_FRAME_DURATION:
                anim_timer = 0
                anim_index = (anim_index+1) % len(anim_frames)
            # update circular motion angle
            # dt is in milliseconds, so this is radians per ms
            circle_speed = 0.0015
            circle_angle += circle_speed * dt 
            # 4 sheep running in a circle
            scale_factor = 1
            num_sheep = 4

            base_frame = anim_frames[0]
            base_rect = base_frame.get_rect()
            sheep_w = base_rect.width * scale_factor
            sheep_h = base_rect.height * scale_factor

            center_x = SCREEN_WIDTH // 2
            center_y = SCREEN_HEIGHT // 2
            radius = 140
            # all sheep are around this base angle
            base_angle = circle_angle
            # small angle gap between sheep
            angle_gap = 0.5
            # offset them around base_angle
            for i in range(num_sheep):
                offset_index = i - (num_sheep - 1) / 2.0
                angle = base_angle + offset_index * angle_gap
                # position on the circle
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                # sprite frame 
                frame_idx = (anim_index + i) % len(anim_frames)
                frame = anim_frames[frame_idx]
                frame_surf = pygame.transform.scale(frame, (int(sheep_w), int(sheep_h)))
                # direction logic
                norm_angle = angle % (2 * math.pi)
                # bottom half of circle: 0...pi, face right
                # top half of circle: pi...2pi, face left
                if norm_angle <= math.pi:
                    frame_surf = pygame.transform.flip(frame_surf, True, False)

                frame_rect = frame_surf.get_rect(center=(int(x), int(y)))
                screen.blit(frame_surf, frame_rect)

            # title
            title_rect = start_title.get_rect()
            title_rect.midtop = (SCREEN_WIDTH // 2, 25)
            screen.blit(start_title, title_rect)

            # hover effect for start button
            mx, my = pygame.mouse.get_pos()
            base_rect = start_button_img.get_rect()
            base_rect.center = start_button_center
            hovering = base_rect.collidepoint(mx, my)

            target_scale = BUTTON_HOVER_SCALE if hovering else 1.0
            btn_scale += (target_scale - btn_scale) * BUTTON_HOVER_LERP
            
            cur_w = int(btn_w * btn_scale)
            cur_h = int(btn_h * btn_scale)

            btn_surf = pygame.transform.smoothscale(start_button_img, (cur_w, cur_h))
            start_button_rect = btn_surf.get_rect(center=start_button_center)
            screen.blit(btn_surf, start_button_rect)
        
        elif game_state == "transition":
            transition_t += dt
            total_ms = TRANS_IN_MS + TRANS_HOLD_MS + TRANS_OUT_MS
            # update level2 underneath the transition board
            for t in tiles:
                if t.alive:
                    t.update(dt)
            x = (SCREEN_WIDTH - TRANS_BOARD_W) // 2
            y_start = -TRANS_BOARD_H
            y_mid = (SCREEN_HEIGHT - TRANS_BOARD_H) // 2
            y_end = SCREEN_HEIGHT + 10
            if transition_t <= TRANS_IN_MS:
                p = transition_t / TRANS_IN_MS
                p = ease_out_cubic(p)
                y = y_start + (y_mid - y_start) * p 
            elif transition_t <= TRANS_IN_MS + TRANS_HOLD_MS:
                y = y_mid
            else:
                out_t = transition_t - (TRANS_IN_MS + TRANS_HOLD_MS)
                p = min(1.0, out_t / TRANS_OUT_MS)
                p = ease_out_cubic(p)
                y = y_mid + (y_end - y_mid) * p 
            # --- draw --- #
            # --- draw level label --- #
            label_img = level_label_l1 if level == 1 else level_label_l2
            label_rect = label_img.get_rect(midtop=(SCREEN_WIDTH // 2, LEVEL_LABEL_Y))
            screen.blit(label_img, label_rect)
            # --- draw board tiles --- #
            layers = sorted({t.layer for t in tiles})
            for layer in layers:
                for t in tiles:
                    if t.alive and t.layer == layer and t.state in ("spawning", "board"):
                        draw_tile(screen, t, tile_images, tiles)
            # --- draw stack box and stack --- #
            draw_stack_box_and_stack(screen, stack_box_img, stack_items, tile_images)
            # --- draw flying tiles --- #
            for t in tiles:
                if t.alive and t.state == "flying":
                    draw_tile(screen, t, tile_images, tiles)
            # draw transition board
            screen.blit(trans_board, (int(x), int(y)))
            # when finished, load level 2
            if transition_t >= total_ms:
                transition_t = 0 
                game_state = "play"

        elif game_state == "play":
            # --- update anchor --- #
            box_x = (SCREEN_WIDTH - STACK_BOX_W) // 2
            box_y = SCREEN_HEIGHT - STACK_BOX_H - STACK_BOX_MARGIN_BOTTOM
            first_x = box_x + 28
            first_y = box_y + 16
            if not game_over:
                # --- update tiles --- #
                for t in tiles:
                    if t.alive:
                        t.update(dt)
                # --- update stack + cleanup --- #
                removed = update_stack_and_cleanup(stack_items, dt, first_x, first_y)
                if removed:
                    layout_stack_items(stack_items, first_x, first_y)
                # --- win/lose check --- #
                # did any tile just arrived into the stack this frame?
                arrived = any(it.visible and it.just_arrived for it in stack_items)
                if arrived:
                    for it in stack_items:
                        it.just_arrived = False 
                    # when stack becomes exactly full, try to clear if possible; otherwise lose immediately
                    if visible_stack_count(stack_items) == STACK_CAPACITY:
                        any_clearing = any(it.visible and it.state == "clearing" for it in stack_items)
                        if any_clearing or has_visible_triple(stack_items):
                            if not any_clearing:
                                start_clear_if_any_triple(stack_items)
                            stack_resolving_full = True 
                        else:
                            game_over = True
                            end_result = "lose"
                            game_state = "end"
                            end_anim_idx = 0
                            end_anim_timer = 0
                # if started resolving because stack was full, keep waiting until it frees up
                if stack_resolving_full:
                    if visible_stack_count(stack_items) < STACK_CAPACITY:
                        stack_resolving_full = False       
                # normal clearing
                if not stack_resolving_full:
                    start_clear_if_any_triple(stack_items)                    
                if (not game_over) and is_level_cleared(tiles, stack_items):
                    if level < MAX_LEVEL:
                        # preload level 2 now
                        level = 2
                        tile_images = tile_images_l2
                        n_types = N_TYPES_L2
                        tiles, stack_items = reset_level(level, n_types)
                        # reset per-level flags
                        stack_resolving_full = False 
                        game_over = False 
                        end_result = None 
                        # load transition state
                        game_state = "transition"
                        transition_t = 0
                    else:
                        # level2 win -> end screen
                        game_over = True
                        end_result = "win"
                        game_state = "end"
                        end_anim_idx = 0
                        end_anim_timer = 0

            # --- DRAW --- #
            # --- draw level label --- #
            label_img = level_label_l1 if level == 1 else level_label_l2
            label_rect = label_img.get_rect(midtop=(SCREEN_WIDTH // 2, LEVEL_LABEL_Y))
            screen.blit(label_img, label_rect)
            # --- draw board tiles --- #
            layers = sorted({t.layer for t in tiles})
            for layer in layers:
                for t in tiles:
                    if t.alive and t.layer == layer and t.state in ("board", "spawning"):
                        draw_tile(screen, t, tile_images, tiles)
            # --- draw stack box and stack --- #
            draw_stack_box_and_stack(screen, stack_box_img, stack_items, tile_images)
            # --- draw flying tiles --- #
            for t in tiles:
                if t.alive and t.state == "flying":
                    draw_tile(screen, t, tile_images, tiles)

        elif game_state == "end":
            frames = end_win_anim if end_result == "win" else end_lose_anim
            end_anim_timer += dt 
            if end_anim_timer >= END_ANIM_FRAMES_MS:
                end_anim_timer = 0
                end_anim_idx = (end_anim_idx + 1) % len(frames)
            
            board = frames[end_anim_idx]
            board_rect = board.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(board, board_rect)
            
            # hover effect for restart button
            mx, my = pygame.mouse.get_pos()
            base_rect = restart_button_img.get_rect()
            base_rect.center = END_BUTTON_CENTER
            hovering = base_rect.collidepoint(mx, my)

            target_scale = BUTTON_HOVER_SCALE if hovering else 1.0
            restart_btn_scale += (target_scale - restart_btn_scale) * BUTTON_HOVER_LERP

            cur_w = int(restart_btn_w * restart_btn_scale)
            cur_h = int(restart_btn_h * restart_btn_scale)
            btn_surf = pygame.transform.smoothscale(restart_button_img, (cur_w, cur_h))
            btn_rect = btn_surf.get_rect(center=END_BUTTON_CENTER)
            screen.blit(btn_surf, btn_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ in "__main__":
    main()







