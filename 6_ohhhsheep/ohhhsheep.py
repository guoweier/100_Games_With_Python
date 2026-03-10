# --- IMPORT PACKAGES --- #
import pygame
import math
import random
import os
import sys


# --- CONFIG --- #
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800

BG_FILE = "assets/background.png"
BGM_FILE = "music/disco.mp3"

# --- window1 --- #
START_TITLE_FILE = "assets/title.png"
START_BUTTON_FILE = "assets/button_start.png"
BUTTON_HOVER_SCALE = 1.08
BUTTON_HOVER_LERP = 0.25

SHEEP_FILES = ["assets/sheep1.png", "assets/sheep2.png", "assets/sheep3.png"]
SHEEP_FRAME_DURATION = 200


# --- window2&3 --- #
# level sign
LEVEL_LABEL_L1_FILE = "assets/levelsign1.png"
LEVEL_LABEL_L2_FILE = "assets/levelsign2.png"

# stack box
STACK_BOX_FILE = "assets/box.png"
STACK_BOX_W = 392
STACK_BOX_H = 106
STACK_BOX_MARGIN_BOTTON = 12
STACK_CAPACITY = 7 

# tiles
TILE_IMG_FILES_L1 = [f"assets/card{i}.png" for i in range(1,4)]
TILE_IMG_FILES_L2 = [f"assets/card{i}.png" for i in range(1,16)]
TILE_WIDTH = 48
TILE_HEIGHT = 60
N_TYPES_L1 = 3
TILES_PER_TYPE = 6

GRID_COLS = 3
GRID_ROWS = 3
LAYER_COUNT = 2

LAYER_OFFSET_X = 0
LAYER_OFFSET_Y = 6

# level 2
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

# trans board
TRANS_BOARD_FILE = "assets/hardashell.png"
TRANS_IN_MS = 500
TRANS_HOLD_MS = 450
TRANS_OUT_MS = 500
TRANS_BOARD_W, TRANS_BOARD_H = 350, 94

# --- window4 --- #
# restart button
RESTART_BUTTON_FILE = "assets/button_restart.png"
END_BUTTON_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 160)

# score board
END_WIN_FRAMES = [f"assets/win{i}.png" for i in range(1,34)]
END_LOSE_FRAMES = [f"assets/lose{i}.png" for i in range(1,5)]
END_BOARD_W, END_BOARD_H = 266, 226
END_ANIM_FRAMES_MS = 120

# --- CLASS --- #
class Tile:
    def __init__(self, id_, kind, layer, x, y, w, h):
        self.id = id_
        self.kind = kind
        self.layer = layer
        self.x = x 
        self.y = y 
        self.w = w
        self.h = h

        self.state = "spawning"
        self.draw_x = x 
        self.draw_y = float(- 120 - random.randint(0, 200))

        self.alive = True 

        self.stack_target_item = None
        self.fly_speed = 1400.0

        self.spawn_t = 0
        self.spawn_dur = 450 + random.randint(0,200)

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)
    
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

        if self.state == "board":
            self.draw_x = self.x
            self.draw_y = self.y 
        elif self.state == "flying":
            tx = float(self.stack_target_item.tx)
            ty = float(self.stack_target_item.ty)
            dx = tx - self.draw_x
            dy = ty - self.draw_y
            dist = (dx*dx + dy*dy) ** 0.5 
            step = self.fly_speed * dt_sec 
            if step >= dist:
                self.draw_x, self.draw_y = tx, ty
                self.alive = False 
                self.state = "box"
                self.stack_target_item.visible = True 
            else:
                self.draw_x += dx / dist * step 
                self.draw_y += dy / dist * step 

            


class StackItem:
    def __init__(self, kind, x, y, w, h):
        self.kind = kind 
        self.x, self.y = float(x), float(y)
        self.w = w
        self.h = h
        self.state = "normal"

        self.clear_dur = 220
        self.clear_t = 0

        self.tx, self.ty = float(x), float(y)

        self.visible = False 

        self.move_speed = 1200.0

    def update(self, dt):
        dt_sec = dt / 1000.0
        dx = self.tx - self.x 
        dy = self.ty - self.y 
        dist = (dx*dx + dy*dy) ** 0.5
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



# --- FUNCTIONS --- #
if getattr(sys, "frozen", False):
    BASE_DIR = (
        getattr(sys, "_MEIPASS", None)
        or os.environ.get("RESOURCEPATH")
        or os.path.abspath(os.path.join(os.path.dirname(sys.executable), "..", "Resources"))
    )
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def resource_path(relative_path):
    return os.path.join(BASE_DIR, relative_path)


def load_images_scaled(paths, size):
    out = []
    for p in paths:
        img = pygame.image.load(resource_path(p)).convert_alpha()
        if img.get_width() != size[0] or img.get_height() != size[1]:
            img = pygame.transform.smoothscale(img, size)
        out.append(img)
    return out 

def generate_tiles(n_types):
    tiles = []
    total_positions = 18
    per_type = total_positions // n_types
    kinds = []
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
    positions = positions[:len(kinds)]
    for i, kind in enumerate(kinds):
        layer, x, y = positions[i]
        tiles.append(Tile(i, kind, layer, x, y, TILE_WIDTH, TILE_HEIGHT))

    return tiles 

def draw_tile(screen, tile, tile_images, tiles):
    if not tile.alive:
        return 
    img = tile_images[tile.kind % len(tile_images)]
    clickable = is_tile_clickable(tile, tiles)
    if not clickable and tile.state == "board":
        img = darken_suface(img, amount=110, radius=6)
    screen.blit(img, (int(tile.draw_x), int(tile.draw_y)))

def darken_suface(surf, amount=90, radius=6):
    s = surf.copy()
    w, h = s.get_size()
    alpha = max(0, min(255, amount))
    dark = pygame.Surface((w,h), pygame.SRCALPHA)
    pygame.draw.rect(dark, (0,0,0,alpha), (0,0,w,h), border_radius=radius)
    s.blit(dark, (0,0))
    return s 

def is_tile_clickable(tile, tiles):
    if not tile.alive or tile.state != "board":
        return False 
    r = tile.rect()
    for other in tiles:
        if not other.alive or other.state != "board":
            continue
        if other.layer <= tile.layer:
            continue
        if other.rect().colliderect(r):
            return False 
    return True  

def find_clicked_tiles(mx, my, tiles):
    candidates = []
    for t in tiles:
        if t.alive and t.rect().collidepoint(mx, my):
            candidates.append(t)
    if not candidates:
        return None 
    candidates.sort(key=lambda t: t.layer, reverse=True)
    return candidates[0]

def reserve_stack_slot_grouped(stack_items, kind, first_x, first_y):
    insert_at = visible_stack_count(stack_items)
    for i in range(visible_stack_count(stack_items)-1, -1, -1):
        if stack_items[i].visible and stack_items[i].kind == kind:
            insert_at = i +1
            break 
    spawn_x = first_x + visible_stack_count(stack_items) * TILE_WIDTH
    spawn_y = first_y 
    reserved = StackItem(kind, spawn_x, spawn_y, TILE_WIDTH, TILE_HEIGHT)
    stack_items.insert(insert_at, reserved)
    layout_stack_items(stack_items, first_x, first_y)
    return reserved 

def layout_stack_items(stack_items, first_x, first_y):
    for i, it in enumerate(stack_items):
        it.tx = first_x + i * TILE_WIDTH
        it.ty = first_y

def start_clear_if_any_triple(stack_items):
    i = 0
    while i < visible_stack_count(stack_items):
        if (not stack_items[i].visible) or stack_items[i].state != "normal":
            i += 1
            continue
        k = stack_items[i].kind
        j = i 
        while j < visible_stack_count(stack_items) and stack_items[j].visible and stack_items[j].kind == k and stack_items[j].state == "normal":
            j += 1
        run_len = j - i
        if run_len >= 3:
            for t in stack_items[i:i+3]:
                t.state = "clearing"
                t.clear_t = 0
        i = j 

def draw_stack_box_and_stack(screen, stack_box_img, stack_items, tile_images):
    # stack box
    box_x = (SCREEN_WIDTH - STACK_BOX_W) // 2
    box_y = SCREEN_HEIGHT - STACK_BOX_H - STACK_BOX_MARGIN_BOTTON
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
            surf = pygame.transform.smoothscale(img, (w,h))
            cx = int(it.x + TILE_WIDTH / 2)
            cy = int(it.y + TILE_HEIGHT / 2)
            r = surf.get_rect(center=(cx,cy))
            screen.blit(surf, r)
        else:
            screen.blit(img, (int(it.x), int(it.y)))

def update_stack_and_cleanup(stack_items, first_x, first_y, dt):
    for it in stack_items:
        it.update(dt)

    before = visible_stack_count(stack_items)
    stack_items[:] = [it for it in stack_items if not it.is_clear_done()]
    removed = (visible_stack_count(stack_items) != before)
    if removed:
        layout_stack_items(stack_items, first_x, first_y)

def visible_stack_count(stack_items):
    return sum(1 for it in stack_items if it.visible)

def is_level_cleared(tiles, stack_items):
    any_tile_alive = any(t.alive for t in tiles)
    any_stack_present = (visible_stack_count(stack_items) > 0)
    return (not any_tile_alive) and (not any_stack_present)

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

def generate_tiles_from_layout(layout_layers, n_types):
    tiles = []
    idx = 0
    total_positions = sum(len(positions) for positions in layout_layers)
    total_triplets = total_positions // 3
    base_triplets = total_triplets // n_types
    extra_triplets = total_triplets % n_types
    triplets_per_kind = [base_triplets] * n_types
    extra_kinds = random.sample(range(n_types), extra_triplets) if extra_triplets > 0 else []
    for k in extra_kinds:
        triplets_per_kind[k] += 1 
    kinds = []
    for k, tcount in enumerate(triplets_per_kind):
        kinds.extend([k] * (tcount * 3))
    random.shuffle(kinds)
    for layer, positions in enumerate(layout_layers): 
        for (x,y) in positions:
            kind = kinds[idx]
            tiles.append(Tile(idx, kind, layer, x, y, TILE_WIDTH, TILE_HEIGHT))
            idx += 1 
    return tiles 


# --- MAIN LOOP --- #

def main():
    pygame.init()
    pygame.display.set_caption("OHHH! SHEEP")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # import assets
    bg = pygame.image.load(resource_path(BG_FILE)).convert_alpha()

    pygame.mixer.init()
    pygame.mixer.music.load(resource_path(BGM_FILE))
    pygame.mixer.music.play(loops=-1)

    # --- window 1 --- #
    start_title = pygame.image.load(resource_path(START_TITLE_FILE)).convert_alpha()
    start_button_img = pygame.image.load(resource_path(START_BUTTON_FILE)).convert_alpha()
    start_button_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 140)
    btn_w, btn_h = start_button_img.get_size()
    btn_scale = 1.0

    sheep_frames = load_images_scaled(SHEEP_FILES, (100,100))

    # --- window 2&3 --- #
    # level signs 
    level_label_l1 = pygame.image.load(resource_path(LEVEL_LABEL_L1_FILE)).convert_alpha()
    level_label_l2 = pygame.image.load(resource_path(LEVEL_LABEL_L2_FILE)).convert_alpha()

    # stack box
    stack_box_img = pygame.image.load(resource_path(STACK_BOX_FILE)).convert_alpha()

    # tiles
    tile_images_l1 = load_images_scaled(TILE_IMG_FILES_L1, (TILE_WIDTH, TILE_HEIGHT))
    tile_images_l2 = load_images_scaled(TILE_IMG_FILES_L2, (TILE_WIDTH, TILE_HEIGHT))

    # trans board
    trans_board = pygame.image.load(resource_path(TRANS_BOARD_FILE)).convert_alpha()

    # --- window 4 --- #
    # restart button
    restart_button_img = pygame.image.load(resource_path(RESTART_BUTTON_FILE)).convert_alpha()
    restart_btn_w, restart_btn_h = restart_button_img.get_size()
    restart_btn_scale = 1.0

    # score board
    end_win_anim = load_images_scaled(END_WIN_FRAMES, (END_BOARD_W, END_BOARD_H))
    end_lose_anim = load_images_scaled(END_LOSE_FRAMES, (END_BOARD_W, END_BOARD_H))

    
    game_state = "start"
    circle_angle = 0.0
    sheep_index = 0
    sheep_timer = 0

    running = True
    while running:
        dt = clock.tick(60)

        # --- INPUT --- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                if game_state == "start":
                    cur_w = int(btn_w * btn_scale)
                    cur_h = int(btn_h * btn_scale) 
                    start_button_rect = pygame.Rect(0, 0, cur_w, cur_h)
                    start_button_rect.center = start_button_center
                    if start_button_rect.collidepoint(mx, my):
                        game_state = "play"
                        tiles = generate_tiles(N_TYPES_L1)
                        stack_items = []
                        level = 1
                        stack_resolving_full = False 
                        tile_images = tile_images_l1 
                        end_result = None 

                elif game_state == "play":
                    clicked = find_clicked_tiles(mx, my, tiles)
                    if clicked and is_tile_clickable(clicked, tiles):
                        box_x = (SCREEN_WIDTH - STACK_BOX_W) // 2
                        box_y = SCREEN_HEIGHT - STACK_BOX_H - STACK_BOX_MARGIN_BOTTON

                        first_x = box_x + 28
                        first_y = box_y + 16

                        reserved_item = reserve_stack_slot_grouped(stack_items, clicked.kind, first_x, first_y)
                        clicked.start_fly_to_stack(reserved_item)
                elif game_state == "end":
                    cur_w = int(restart_btn_w * restart_btn_scale)
                    cur_h = int(restart_btn_h * restart_btn_scale)
                    restart_rect = pygame.Rect(0,0,cur_w,cur_h)
                    restart_rect.center = END_BUTTON_CENTER
                    if restart_rect.collidepoint(mx, my):
                        game_state = "play"
                        level = 1
                        tile_images = tile_images_l1
                        tiles = generate_tiles(N_TYPES_L1)
                        stack_items = []
                        stack_resolving_full = False 
                        end_result = None 


        # --- DRAW --- #
        screen.blit(bg, (0,0))

        if game_state == "start":
            # title 
            title_rect = start_title.get_rect()
            title_rect.midtop = (SCREEN_WIDTH // 2, 25)
            screen.blit(start_title, title_rect)
            
            # sheep
            ## sheep run
            sheep_timer += dt
            if sheep_timer >= SHEEP_FRAME_DURATION:
                sheep_timer = 0
                sheep_index = (sheep_index+1) % len(sheep_frames)

            ## circle
            center_x = SCREEN_WIDTH // 2
            center_y = SCREEN_HEIGHT // 2
            radius = 140
            circle_speed = 0.0015
            num_sheep = 4
            angle_gap = 0.5
            base_angle = circle_angle
            circle_angle += circle_speed * dt

            for i in range(num_sheep):
                offset_index = i - (num_sheep - 1) / 2.0
                angle = base_angle + offset_index * angle_gap
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                frame_idx = (sheep_index + i) % len(sheep_frames)
                frame = sheep_frames[frame_idx]
                # direction
                norm_angle = angle % (2 * math.pi)
                if norm_angle <= math.pi:
                    frame = pygame.transform.flip(frame, True, False)

                frame_rect = frame.get_rect(center=(int(x), int(y)))
                screen.blit(frame, frame_rect)
            
            # start button
            mx, my = pygame.mouse.get_pos()
            base_rect = start_button_img.get_rect()
            base_rect.center = start_button_center
            hovering = base_rect.collidepoint(mx,my)

            target_scale = BUTTON_HOVER_SCALE if hovering else 1.0
            btn_scale += (target_scale - btn_scale) * BUTTON_HOVER_LERP
            if abs(target_scale - btn_scale) < 0.001:
                btn_scale = target_scale

            cur_w = int(btn_w * btn_scale)
            cur_h = int(btn_h * btn_scale)
            btn_surf = pygame.transform.smoothscale(start_button_img, (cur_w, cur_h))
            start_button_rect = btn_surf.get_rect(center = start_button_center)
            screen.blit(btn_surf, start_button_rect)

        elif game_state == "transition":
            transition_t += dt
            x = (SCREEN_WIDTH - TRANS_BOARD_W) // 2
            y_mid = (SCREEN_HEIGHT - TRANS_BOARD_H) // 2
            y_start = -TRANS_BOARD_H
            y_end = SCREEN_HEIGHT + 10

            if transition_t <= TRANS_IN_MS:
                p = transition_t / TRANS_IN_MS
                p = 1 - (1 - p) ** 3
                y = y_start + (y_mid - y_start) * p 
            elif transition_t <= TRANS_IN_MS + TRANS_HOLD_MS:
                y = y_mid 
            else:
                out_t = transition_t - (TRANS_IN_MS + TRANS_HOLD_MS)
                p = min(1.0, out_t / TRANS_OUT_MS)
                p = 1 - (1 - p) ** 3
                y = y_mid + (y_end - y_mid) * p 
            

            # level sign
            label_img = level_label_l1 if level == 1 else level_label_l2
            label_rect = label_img.get_rect(midtop=(SCREEN_WIDTH//2, 18))
            screen.blit(label_img, label_rect)

            # tiles
            for t in tiles:
                if t.alive:
                    t.update(dt)
            
            for t in tiles:
                if t.state in ("board", "spawning"):
                    draw_tile(screen, t, tile_images, tiles)

            # stack box
            draw_stack_box_and_stack(screen, stack_box_img, stack_items, tile_images)

            # trans board
            screen.blit(trans_board, (int(x), int(y)))
            
            if transition_t >= (TRANS_IN_MS + TRANS_HOLD_MS +TRANS_OUT_MS):
                transition_t = 0
                game_state = "play"

        elif game_state == "play":
            box_x = (SCREEN_WIDTH - STACK_BOX_W) // 2
            box_y = SCREEN_HEIGHT - STACK_BOX_H - STACK_BOX_MARGIN_BOTTON

            first_x = box_x + 28
            first_y = box_y + 16

            for t in tiles:
                if t.alive:
                    t.update(dt)
            
            update_stack_and_cleanup(stack_items, first_x, first_y, dt)

            if visible_stack_count(stack_items) == STACK_CAPACITY:
                any_clearing = any(it.visible and it.state == "clearing" for it in stack_items)
                if any_clearing or has_visible_triple(stack_items):
                    stack_resolving_full = True 
                    if not any_clearing:
                        start_clear_if_any_triple(stack_items)
                else:
                    game_state = "end"
                    end_result = "lose"
                    end_anim_timer = 0
                    end_anim_index = 0


            if stack_resolving_full:
                if visible_stack_count(stack_items) < STACK_CAPACITY:
                    stack_resolving_full = False 

            if is_level_cleared(tiles, stack_items):
                if level == 1:
                    level = 2
                    tiles = generate_tiles_from_layout(LEVEL2_LAYOUT, 15)
                    stack_items = []
                    tile_images = tile_images_l2
                    transition_t = 0
                    game_state = "transition"
                else:
                    game_state = "end"
                    end_result = "win"
                    end_anim_timer = 0
                    end_anim_index = 0
                

            start_clear_if_any_triple(stack_items)

            # level sign
            label_img = level_label_l1 if level == 1 else level_label_l2
            label_rect = label_img.get_rect(midtop=(SCREEN_WIDTH//2, 18))
            screen.blit(label_img, label_rect)

            # tiles
            for t in tiles:
                if t.state in ("board", "spawning"):
                    draw_tile(screen, t, tile_images, tiles)

            # stack box
            draw_stack_box_and_stack(screen, stack_box_img, stack_items, tile_images)
            
            # flying tiles
            for t in tiles:
                if t.alive and t.state == "flying":
                    draw_tile(screen, t, tile_images, tiles)


        elif game_state == "end":
            # restart button
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

            # score board
            frames = end_win_anim if end_result == "win" else end_lose_anim
            end_anim_timer += dt 
            if end_anim_timer >= END_ANIM_FRAMES_MS:
                end_anim_timer = 0
                end_anim_index = (end_anim_index + 1) % len(frames)
            board = frames[end_anim_index]
            board_rect = board.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(board, board_rect)

        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()






