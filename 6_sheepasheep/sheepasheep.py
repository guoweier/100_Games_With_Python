import pygame
import random
import math 
from collections import Counter

# --------- CONFIG ----------- #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
STACK_CAPACITY = 7
TILE_WIDTH = 60
TILE_HEIGHT = 70
N_TYPES = 8
TILES_PER_TYPE = 9

# ---- ANIMATION ASSET CONFIG ---- #
ANIM_FRAME_FILES = ["assets/sheep1.png", "assets/sheep2.png", "assets/sheep3.png"]
ANIM_FRAME_DURATION = 200


# -------- TILE CLASS --------- #
class Tile:
    def __init__(self, id_, kind, layer, x, y, w, h):
        self.id = id_
        self.kind = kind
        self.layer = layer
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.alive = True
    
    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
    

# ------------ HELPER FUNCTIONS ------------- #
def is_tile_blocked(tile, tiles):
    """Tile is blocked if any alive tile with higher layer overlapys it"""
    if not tile.alive:
        return True
    r = tile.rect()
    for other in tiles:
        if not other.alive:
            continue
        if other.layer <= tile.layer:
            continue 
        if other.rect().colliderect(r):
            return True
    return False 

def is_tile_clickable(tile, tiles):
    return tile.alive and not is_tile_blocked(tile, tiles)

def find_clicked_tile(mx, my, tiles):
    """Return the TOPMOST alive tile under the mouse, if any"""
    candidates = []
    for t in tiles:
        if t.alive and t.rect().collidepoint(mx, my):
            candidates.append(t)
    if not candidates:
        return None
    # choose the one with highest layer
    candidates.sort(key=lambda t: t.layer, reverse=True)
    return candidates[0]

def eliminate_triples(stack):
    """Remove groups of 3 of same kind from stack"""
    counts = Counter(stack)
    changed = False
    for kind, cnt in list(counts.items()):
        while cnt >= 3:
            removed = 0
            new_stack = []
            for k in stack:
                if k == kind and removed < 3:
                    removed += 1
                else:
                    new_stack.append(k)
            stack[:] = new_stack
            changed = True
            cnt -= 3
    return changed 

def check_lose(stack):
    return len(stack) > STACK_CAPACITY

def check_win(tiles):
    return all(not t.alive for t in tiles)

# --------- LEVEL GENERATION ------------ #
def generate_tiles():
    """
    very simple layout:
    - base grid layer 0
    - some overlapping tiles at layer 1
    - a few at layer 2
    """
    # prepare kinds bag
    kinds = []
    for k in range(N_TYPES):
        kinds.extend([k] * TILES_PER_TYPE)
    random.shuffle(kinds)

    # define positions
    positions = []

    # layer 0: 6x3 grid
    for i in range(10):
        for j in range(5):
            x = 50 + i * (TILE_WIDTH + 5)
            y = 50 + j * (TILE_HEIGHT + 5)
            positions.append((0, x, y))
    
    # layer 1: smaller grid slightly shifted
    for i in range(8):
        for j in range(4):
            x = 80 + i * (TILE_WIDTH + 8)
            y = 80 + j * (TILE_HEIGHT + 8)
            positions.append((1, x, y))

    # layer 2: a few on top
    for i in range(5):
        for j in range(2):
            x = 140 + i * (TILE_WIDTH + 10)
            y = 140 + j * (TILE_HEIGHT + 10)
            positions.append((2, x, y))

    # ensure 
    positions = positions[:len(kinds)]

    tiles = []
    for i, kind in enumerate(kinds):
        layer, x, y = positions[i]
        tiles.append(Tile(i, kind, layer, x, y, TILE_WIDTH, TILE_HEIGHT))

    return tiles 

# --------- DRAWING ----------- #
def get_kind_color(kind):
    # define some distinct colors
    palette = [
        (244, 67, 54),
        (33, 150, 243),
        (76, 175, 80),
        (255, 235, 59),
        (156, 39, 176),
        (255, 152, 0),
        (0, 188, 212),
        (121, 85, 72),
    ]
    return palette[kind % len(palette)]

def draw_tile(screen, tile, font, tiles):
    r = tile.rect()
    # slight shading if blocked
    clickable = is_tile_clickable(tile, tiles)
    base_color = get_kind_color(tile.kind)
    if clickable:
        color = base_color
    else:
        color = tuple(max(0, c-60) for c in base_color)
    pygame.draw.rect(screen, color, r, border_radius = 8)
    pygame.draw.rect(screen , (30, 30, 30), r, width=2, border_radius=8)
    # draw kind index as text
    text = font.render(str(tile.kind), True, (0,0,0))
    text_rect = text.get_rect(center=r.center)
    screen.blit(text, text_rect)

def draw_stack(screen, stack, font):
    """Draw bottom stack as a row of small rectangles"""
    y = SCREEN_HEIGHT - 100
    x_start = 60
    gap = 10

    # slot background
    for i in range(STACK_CAPACITY):
        x = x_start + i * (TILE_WIDTH // 2 + gap)
        rect = pygame.Rect(x, y, TILE_WIDTH // 2, TILE_HEIGHT // 2)
        pygame.draw.rect(screen, (210, 210, 210), rect, border_radius=6)
        pygame.draw.rect(screen, (120, 120, 120), rect, 1, border_radius=6)
    
    # draw tiles in stack
    for idx, kind in enumerate(stack):
        x = x_start + idx * (TILE_WIDTH // 2 + gap)
        rect = pygame.Rect(x, y, TILE_WIDTH // 2, TILE_HEIGHT // 2)
        color = get_kind_color(kind)
        pygame.draw.rect(screen, color, rect, border_radius=6)
        pygame.draw.rect(screen, (40, 40, 40), rect, 1, border_radius=6)
        text = font.render(str(kind), True, (0,0,0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # draw label
    label = font.render(f"Stack ({len(stack)}/{STACK_CAPACITY})", True, (0,0,0))
    screen.blit(label, (x_start, y-30))

def load_animation_frames():
    frames = []
    for fname in ANIM_FRAME_FILES:
        img = pygame.image.load(fname).convert_alpha()
        frames.append(img)
    return frames
    
# ------------- MAIN LOOP ----------------- #
def main():
    pygame.init()
    pygame.display.set_caption("Sheep a sheep")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 20)

    anim_frames = load_animation_frames()
    anim_index = 0
    anim_timer = 0
    circle_angle = 0.0
    game_state = "start"

    button_width, button_height = 200, 60
    start_button_rect = pygame.Rect(
        (SCREEN_WIDTH - button_width) // 2,
        SCREEN_HEIGHT - 150,
        button_width, 
        button_height
    )

    tiles = generate_tiles()
    stack = []

    game_over = False 
    status_text = ""

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                if game_state == "start":
                    if start_button_rect.collidepoint(mx, my):
                        game_state = "play"
                        tiles = generate_tiles()
                        stack = []
                        game_over = False
                        status_text = ""
                elif game_state == "play":
                    if game_over:
                        tiles = generate_tiles()
                        stack = []
                        game_over = False
                        status_text = ""
                        continue

                    clicked = find_clicked_tile(mx, my, tiles)
                    if clicked and is_tile_clickable(clicked, tiles):
                        clicked.alive = False
                        stack.append(clicked.kind)
                        eliminate_triples(stack)

                        if check_lose(stack):
                            game_over = True
                            status_text = "You Lose!"
                        elif check_win(tiles):
                            game_over = True
                            status_text = "You Win!"

        # ------- DRAW --------- #
        screen.fill((240,240,240))
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
            center_y = SCREEN_HEIGHT // 2 + 20
            radius = 150
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
            title_text = font.render("Sheep a sheep", True, (0,0,0))
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 80))
            screen.blit(title_text, title_rect)

            # draw start button
            pygame.draw.rect(screen, (255,255,255), start_button_rect, border_radius=12)
            pygame.draw.rect(screen, (0,0,0), start_button_rect, 2, border_radius=12)
            btn_text = font.render("START", True, (0,0,0))
            btn_rect = btn_text.get_rect(center=start_button_rect.center)
            screen.blit(btn_text, btn_rect)
        
        elif game_state == "play":
            # draw tiles by layer
            if tiles:
                layers = sorted({t.layer for t in tiles})
                for layer in layers:
                    for t in tiles:
                        if t.alive and t.layer == layer:
                            draw_tile(screen, t, font, tiles)
            draw_stack(screen, stack, font)

            # draw top message
            title_text = font.render("Sheep a sheep", True, (0,0,0))
            screen.blit(title_text, (20,20))

            if status_text:
                st = font.render(status_text, True, (200,0,0))
                screen.blit(st, (20,50))

        pygame.display.flip()

    pygame.quit()

if __name__ in "__main__":
    main()










