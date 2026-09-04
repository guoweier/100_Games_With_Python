# --- IMPORT --- #
import pygame
import random
import sys, os

# --- CONFIG --- #
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

pygame.init()
pygame.display.set_caption("SOLITAIRE")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


BG = (33, 168, 72)
WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
RED = (200, 40, 40)
GOLD = (220, 190, 60)
GRAY = (180, 180, 180)
DARK_GREEN = (10, 90, 35)
BLUE = (70, 130, 220)

CARD_WIDTH = 144
CARD_HEIGHT = 192
TABLEAU_GAP_X = 24
TABLEAU_FACE_DOWN_OFFSET = 8
TABLEAU_FACE_UP_OFFSET = 28

MENU_BAR_HEIGHT = 32

TOP_MARGIN = MENU_BAR_HEIGHT + 20
LEFT_MARGIN = 24

STOCK_POS = (LEFT_MARGIN, TOP_MARGIN)
WASTE_POS = (LEFT_MARGIN + CARD_WIDTH + 24, TOP_MARGIN)

FOUNDATION_START_X = SCREEN_WIDTH - LEFT_MARGIN - (CARD_WIDTH * 4 + TABLEAU_GAP_X * 3)
FOUNDATION_Y = TOP_MARGIN
FOUNDATION_POS = [(FOUNDATION_START_X + i * (CARD_WIDTH + TABLEAU_GAP_X), FOUNDATION_Y) for i in range(4)]

TABLEAU_Y = TOP_MARGIN + CARD_HEIGHT + 20
TABLEAU_XS = [LEFT_MARGIN + i * (CARD_WIDTH + TABLEAU_GAP_X) for i in range(7)]

FONT = pygame.font.SysFont("arial", 24)
SMALL_FONT = pygame.font.Font("assets/font/solitaire_font_bold.ttf", 12)

ASSETS_FOLDER = "assets"
SUIT_FILE_NAMES = {
    "♠︎": "spade",
    "♣︎": "club",
    "♥︎": "heart",
    "♦︎": "diamond"
}

SUITS = ["♠︎", "♣︎", "♥︎", "♦︎"]
RANKS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
SUIT_TO_COLOR = {
    "♠︎": "black",
    "♣︎": "black",
    "♥︎": "red",
    "♦︎": "red"
}

#### menu bar ####
MENU_BG = (225, 225, 225)
MENU_HOVER = (195, 215, 240)
MENU_TEXT = (20, 20, 20)
MENU_BORDER = (110, 110, 110)
DROPDOWN_BG = (245, 245, 245)

GAME_BUTTON_RECT = pygame.Rect(8, 0, 65, MENU_BAR_HEIGHT)
HELP_BUTTON_RECT = pygame.Rect(76, 0, 65, MENU_BAR_HEIGHT)

GAME_MENU_ITEMS = [
    "Deal",
    "undo",
    "Deck",
    "Options",
    "Exit"
]

DROPDOWN_X = GAME_BUTTON_RECT.x
DROPDOWN_Y = MENU_BAR_HEIGHT
DROPDOWN_WIDTH = 145
DROPDOWN_ITEM_HEIGHT = 30

#### Deck Window ####
DECK_WINDOW_WIDTH = 702
DECK_WINDOW_HEIGHT = 518
DECK_WINDOW_X = (SCREEN_WIDTH - DECK_WINDOW_WIDTH) // 2
DECK_WINDOW_Y = (SCREEN_HEIGHT - DECK_WINDOW_HEIGHT) // 2  

DECK_WINDOW_RECT = pygame.Rect(
    DECK_WINDOW_X,
    DECK_WINDOW_Y,
    DECK_WINDOW_WIDTH,
    DECK_WINDOW_HEIGHT
)

DECK_COLUMNS = 6
DECK_ROWS = 2
DECK_COUNT = 12
THUMBNAIL_W = 90
THUMBNAIL_H = 158

THUMBNAIL_START_X = 36
THUMBNAIL_START_Y = 76
THUMBNAIL_GAP_X = 18
THUMBNAIL_GAP_Y = 18

SELECTION_GAP = 2
SELECTION_BORDER_WIDTH = 4
SELECTION_COLOR = (0, 0, 175)

DECK_OK_BUTTON_RECT = pygame.Rect(DECK_WINDOW_X + 360, DECK_WINDOW_Y + 440, 150, 46)
DECK_CANCEL_BUTTON_RECT = pygame.Rect(DECK_WINDOW_X + 522, DECK_WINDOW_Y + 440, 150, 46)
DECK_OK_NORMAL_PATH = os.path.join(ASSETS_FOLDER, "ok1.png")
DECK_OK_CLICKED_PATH = os.path.join(ASSETS_FOLDER, "ok2.png")
DECK_CANCEL_NORMAL_PATH = os.path.join(ASSETS_FOLDER, "cancel1.png")
DECK_CANCEL_CLICKED_PATH = os.path.join(ASSETS_FOLDER, "cancel2.png")

DECK_CROSS_BUTTON_RECT = pygame.Rect(DECK_WINDOW_X + 658, DECK_WINDOW_Y + 10, 32, 28)
DECK_CROSS_NORMAL_PATH = os.path.join(ASSETS_FOLDER, "cross1.png")
DECK_CROSS_CLICKED_PATH = os.path.join(ASSETS_FOLDER, "cross2.png")

DECK_WINDOW_PATH = os.path.join(ASSETS_FOLDER, "deck.png")
CARD_FRONT_FOLDER = os.path.join(ASSETS_FOLDER, "card")
CARD_BACK_FOLDER = os.path.join(ASSETS_FOLDER, "back")

CARD_BACK_FILES = [f"back_{i+1}.png" for i in range(12)]

FOUNDATION_PATH = os.path.join(ASSETS_FOLDER, "foundation.png")
STOCK_PATH = os.path.join(ASSETS_FOLDER, "stock.png")

#### Option Window ####
OPTION_WINDOW_WIDTH = 684
OPTION_WINDOW_HEIGHT = 438
OPTION_WINDOW_X = (SCREEN_WIDTH - OPTION_WINDOW_WIDTH) // 2
OPTION_WINDOW_Y = (SCREEN_HEIGHT - OPTION_WINDOW_HEIGHT) // 2

OPTION_WINDOW_RECT = pygame.Rect(
    OPTION_WINDOW_X,
    OPTION_WINDOW_Y,
    OPTION_WINDOW_WIDTH,
    OPTION_WINDOW_HEIGHT
)

OPTION_OK_BUTTON_RECT = pygame.Rect(OPTION_WINDOW_X + 342, OPTION_WINDOW_Y + 360, 150, 46)
OPTION_CANCEL_BUTTON_RECT = pygame.Rect(OPTION_WINDOW_X + 504, OPTION_WINDOW_Y + 360, 150, 46)
OPTION_OK_NORMAL_PATH = os.path.join(ASSETS_FOLDER, "ok1.png")
OPTION_OK_CLICKED_PATH = os.path.join(ASSETS_FOLDER, "ok2.png")
OPTION_CANCEL_NORMAL_PATH = os.path.join(ASSETS_FOLDER, "cancel1.png")
OPTION_CANCEL_CLICKED_PATH = os.path.join(ASSETS_FOLDER, "cancel2.png")

OPTION_CROSS_BUTTON_RECT = pygame.Rect(OPTION_WINDOW_X + 642, OPTION_WINDOW_Y + 10, 32, 28)
OPTION_CROSS_NORMAL_PATH = os.path.join(ASSETS_FOLDER, "cross1.png")
OPTION_CROSS_CLICKED_PATH = os.path.join(ASSETS_FOLDER, "cross2.png")

OPTION_WINDOW_PATH1 = os.path.join(ASSETS_FOLDER, "option1.png")
OPTION_WINDOW_PATH2 = os.path.join(ASSETS_FOLDER, "option2.png")

## Draw One/Three ##
DRAW_ONE_CLICK_RECT = pygame.Rect(OPTION_WINDOW_X + 74, OPTION_WINDOW_Y + 130, 12, 12)
DRAW_THREE_CLICK_RECT = pygame.Rect(OPTION_WINDOW_X + 74, OPTION_WINDOW_Y + 188, 12, 12)
DRAW_ONE_DOT_POS = (OPTION_WINDOW_X + 76, OPTION_WINDOW_Y + 132)
DRAW_THREE_DOT_POS = (OPTION_WINDOW_X + 76, OPTION_WINDOW_Y + 190)
OPTION_DOT_SIZE = 8
WASTE_CARD_OFFSET_X = 24
OPTION_DOT_PATH = os.path.join(ASSETS_FOLDER, "option_dot.png")

## Timed Game ##
OPTION_CHECK_PATH = os.path.join(ASSETS_FOLDER, "option_check.png")
TIMING_CLICK_RECT = pygame.Rect(OPTION_WINDOW_X + 34, OPTION_WINDOW_Y + 268, 18, 18)
TIMING_CHECK_POS = (OPTION_WINDOW_X + 36, OPTION_WINDOW_Y + 270)




# --- CLASS --- #
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = False
        self.rect = pygame.Rect(0,0, CARD_WIDTH, CARD_HEIGHT)

    @property
    def color(self):
        return SUIT_TO_COLOR[self.suit]
    
    @property
    def value(self):
        return RANKS.index(self.rank) + 1
    
    def draw(self, surface, x, y, current_back_index, selected=False):
        self.rect.topleft = (x,y)
        
        if self.face_up:
            image = CARD_IMAGES[(self.suit, self.rank)]
        else:
            image = CARD_BACK_IMAGES[current_back_index]

        surface.blit(image, self.rect)

        if selected:
            pygame.draw.rect(surface, (0,0,175), self.rect, width=4)




# --- FUNCTIONS --- #
def load_slot_image(path):
    try:
        image = pygame.image.load(path).convert_alpha()
    except (pygame.error, FileNotFoundError) as error:
        raise RuntimeError (f"Could not load slot image: {path}") from error

    return pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))


def load_card_images():
    images = {}

    for suit in SUITS:
        for rank in RANKS:
            filename = f"{SUIT_FILE_NAMES[suit]}{rank}.png"
            path = os.path.join(CARD_FRONT_FOLDER, filename)

            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))

            images[(suit, rank)] = image 
        
    return images

def load_card_back_images():
    images = []
    for filename in CARD_BACK_FILES:
        path = os.path.join(CARD_BACK_FOLDER, filename)

        try:
            image = pygame.image.load(path).convert_alpha()
        except (pygame.error, FileNotFoundError) as error:
            raise RuntimeError(f"Could not load {path}") from error 
        
        image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
        images.append(image)
    
    return images 

def load_deck_window_image():
    try:
        image = pygame.image.load(DECK_WINDOW_PATH).convert_alpha()
    except (pygame.error, FileNotFoundError) as error:
        raise RuntimeError(f"Could not load{DECK_WINDOW_PATH}") from error
    
    return pygame.transform.scale(image, (DECK_WINDOW_WIDTH, DECK_WINDOW_HEIGHT))


def load_button_image(path, button_w, button_h):
    try:
        image = pygame.image.load(path).convert_alpha()
    except (pygame.error, FileNotFoundError) as error:
        raise RuntimeError(f"Cound not load button image: {path}") from error

    return pygame.transform.scale(image, (button_w, button_h))
    

def get_deck_thumbnail_rect(index):
    row = index // DECK_COLUMNS
    column = index % DECK_COLUMNS

    x = (DECK_WINDOW_X + THUMBNAIL_START_X + column * (THUMBNAIL_W + THUMBNAIL_GAP_X))
    y = (DECK_WINDOW_Y + THUMBNAIL_START_Y + row * (THUMBNAIL_H + THUMBNAIL_GAP_Y))

    return pygame.Rect(x, y, THUMBNAIL_W, THUMBNAIL_H)

def get_deck_thumbnail_at_pos(mouse_pos):
    for index in range(DECK_COUNT):
        thumbnail_rect = (get_deck_thumbnail_rect(index))
        if thumbnail_rect.collidepoint(mouse_pos):
            return index 
    return None

def draw_selected_deck_outline(selected_index):
    thumbnail_rect = get_deck_thumbnail_rect(selected_index)
    total_extension = (SELECTION_GAP + SELECTION_BORDER_WIDTH)
    outline_rect = thumbnail_rect.inflate(total_extension * 2, total_extension * 2)
    pygame.draw.rect(screen, SELECTION_COLOR, outline_rect, width=SELECTION_BORDER_WIDTH)

def load_option_window_image():
    try:
        image = pygame.image.load(OPTION_WINDOW_PATH1).convert_alpha()
    except (pygame.error, FileNotFoundError) as error:
        raise RuntimeError(f"Could not load option window: {OPTION_WINDOW_PATH1}") from error
    return pygame.transform.scale(image, (OPTION_WINDOW_WIDTH, OPTION_WINDOW_HEIGHT))


def get_game_menu_item_rect(index):
    return pygame.Rect(DROPDOWN_X, DROPDOWN_Y + index * DROPDOWN_ITEM_HEIGHT, DROPDOWN_WIDTH, DROPDOWN_ITEM_HEIGHT)

def get_game_menu_item_at_pos(mouse_pos):
    for index, item in enumerate(GAME_MENU_ITEMS):
        item_rect = get_game_menu_item_rect(index)
        if item_rect.collidepoint(mouse_pos):
            return item
    return None

def draw_menu_bar(game_menu_open):
    mouse_pos = pygame.mouse.get_pos()
    menu_bar_rect = pygame.Rect(0, 0, SCREEN_WIDTH, MENU_BAR_HEIGHT)
    pygame.draw.rect(screen, MENU_BG, menu_bar_rect)
    pygame.draw.line(screen, MENU_BORDER, (0, MENU_BAR_HEIGHT - 1), (SCREEN_WIDTH, MENU_BAR_HEIGHT - 1))
    if (GAME_BUTTON_RECT.collidepoint(mouse_pos) or game_menu_open):
        pygame.draw.rect(screen, MENU_HOVER, GAME_BUTTON_RECT)
    if HELP_BUTTON_RECT.collidepoint(mouse_pos):
        pygame.draw.rect(screen, MENU_HOVER, HELP_BUTTON_RECT)
    game_text = SMALL_FONT.render("Game", True, MENU_TEXT)
    help_text = SMALL_FONT.render("Help", True, MENU_TEXT)
    screen.blit(game_text, (GAME_BUTTON_RECT.x + 10, GAME_BUTTON_RECT.centery - game_text.get_height() // 2 + 3))
    screen.blit(help_text, (HELP_BUTTON_RECT.x + 10, HELP_BUTTON_RECT.centery - help_text.get_height() // 2 + 3))
    if game_menu_open:
        draw_game_dropdown()

def draw_game_dropdown():
    mouse_pos = pygame.mouse.get_pos()
    dropdown_height = (len(GAME_MENU_ITEMS) * DROPDOWN_ITEM_HEIGHT)
    dropdown_rect = pygame.Rect(DROPDOWN_X, DROPDOWN_Y, DROPDOWN_WIDTH, dropdown_height)
    pygame.draw.rect(screen, (245, 245, 245), dropdown_rect)
    pygame.draw.rect(screen, MENU_BORDER, dropdown_rect, width=1)
    for index, item in enumerate(GAME_MENU_ITEMS):
        item_rect = get_game_menu_item_rect(index)
        if item_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, MENU_HOVER, item_rect)
        item_text = SMALL_FONT.render(item, True, MENU_TEXT)
        screen.blit(item_text, (item_rect.x + 12, item_rect.centery - item_text.get_height() // 2 + 3))

## deck window ##
def draw_deck_buttons(pressed_deck_button):
    mouse_pos = pygame.mouse.get_pos()
    ok_is_pressed = pressed_deck_button == "ok" and DECK_OK_BUTTON_RECT.collidepoint(mouse_pos)
    cancel_is_pressed = pressed_deck_button == "cancel" and DECK_CANCEL_BUTTON_RECT.collidepoint(mouse_pos)
    cross_is_pressed = pressed_deck_button == "cross" and DECK_CROSS_BUTTON_RECT.collidepoint(mouse_pos)
    ok_image = DECK_OK_CLICKED_IMAGE if ok_is_pressed else DECK_OK_NORMAL_IMAGE
    cancel_image = DECK_CANCEL_CLICKED_IMAGE if cancel_is_pressed else DECK_CANCEL_NORMAL_IMAGE
    cross_image = DECK_CROSS_CLICKED_IMAGE if cross_is_pressed else DECK_CROSS_NORMAL_IMAGE

    screen.blit(ok_image, DECK_OK_BUTTON_RECT.topleft)
    screen.blit(cancel_image, DECK_CANCEL_BUTTON_RECT.topleft)
    screen.blit(cross_image, DECK_CROSS_BUTTON_RECT.topleft)

def draw_deck_window(pending_back_index, pressed_deck_button):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 110))
    screen.blit(overlay, (0, 0))
    screen.blit(DECK_WINDOW_IMAGE, (DECK_WINDOW_X, DECK_WINDOW_Y))
    draw_selected_deck_outline(pending_back_index)
    draw_deck_buttons(pressed_deck_button)

## option window ##
def draw_option_buttons(pressed_option_button):
    mouse_pos = pygame.mouse.get_pos()
    ok_pressed = pressed_option_button == "ok" and OPTION_OK_BUTTON_RECT.collidepoint(mouse_pos)
    cancel_pressed = pressed_option_button == "cancel" and OPTION_CANCEL_BUTTON_RECT.collidepoint(mouse_pos)
    cross_pressed = pressed_option_button == "cross" and OPTION_CROSS_BUTTON_RECT.collidepoint(mouse_pos)
    ok_image = OPTION_OK_CLICKED_IMAGE if ok_pressed else OPTION_OK_NORMAL_IMAGE
    cancel_image = OPTION_CANCEL_CLICKED_IMAGE if cancel_pressed else OPTION_CANCEL_NORMAL_IMAGE
    cross_image = OPTION_CROSS_CLICKED_IMAGE if cross_pressed else OPTION_CROSS_NORMAL_IMAGE

    screen.blit(ok_image, OPTION_OK_BUTTON_RECT.topleft)
    screen.blit(cancel_image, OPTION_CANCEL_BUTTON_RECT.topleft)
    screen.blit(cross_image, OPTION_CROSS_BUTTON_RECT.topleft)

def draw_draw_count_option(pending_draw_count):
    if pending_draw_count == 1:
        dot_pos = DRAW_ONE_DOT_POS
    elif pending_draw_count == 3:
        dot_pos = DRAW_THREE_DOT_POS
    else:
        return
    screen.blit(OPTION_DOT_IMAGE, dot_pos)

def start_timer(timer_started, timer_running, timer_segment_start):
    if not timer_started:
        timer_started = True
        timer_running = True
        timer_segment_start = pygame.time.get_ticks()
    return (timer_started, timer_running, timer_segment_start)

def pause_timer(timer_started, timer_running, timer_accumulated_ms, timer_segment_start):
    if timer_started and timer_running:
        now = pygame.time.get_ticks()
        timer_accumulated_ms += now - timer_segment_start
        timer_running = False
    return (timer_running, timer_accumulated_ms)

def resume_timer(timer_started, timer_running, timer_segment_start):
    if timer_started and not timer_running:
        timer_running = True
        timer_segment_start = pygame.time.get_ticks()
    return (timer_running, timer_segment_start)

def get_elapsed_seconds(timer_started, timer_running, timer_accumulated_ms, timer_segment_start):
    if not timer_started:
        return 0
    total_ms = timer_accumulated_ms
    if timer_running:
        total_ms += pygame.time.get_ticks() - timer_segment_start
    return total_ms // 1000


def draw_option_window(pressed_option_button, pending_draw_count, pending_show_timing):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 110))
    screen.blit(overlay, (0, 0))
    screen.blit(OPTION_WINDOW_IMAGE, (OPTION_WINDOW_X, OPTION_WINDOW_Y))
    # draw 1/3
    draw_draw_count_option(pending_draw_count)
    # timer
    if pending_show_timing:
        screen.blit(OPTION_CHECK_IMAGE, TIMING_CHECK_POS)
    # ok and cancel buttons
    draw_option_buttons(pressed_option_button)


def create_deck():
    deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def deal_new_game():
    deck = create_deck()
    tableau = [[] for _ in range(7)]
    foundations = [[] for _ in range(4)]
    #stock = []
    waste = []

    # 7 tableau: col0 -> 1, col1 -> 2, ... col6 -> 7
    for col in range(7):
        for row in range(col + 1):
            card = deck.pop()
            tableau[col].append(card)
            if row == col:
                card.face_up = True
    stock = deck
    return tableau, foundations, stock, waste

def can_place_on_tableau(card, target_column):
    if not target_column:
        return card.rank == "13"
    
    top_card = target_column[-1]
    if not top_card.face_up:
        return False 
    
    return top_card.value == card.value + 1 and top_card.color != card.color

def can_place_on_foundation(card, foundation):
    if not foundation:
        return card.rank == "1"
    
    top_card = foundation[-1]
    return (top_card.suit == card.suit and card.value == top_card.value + 1)

def get_card_draw_positions(tableau):
    positions = {}
    for col_idx, column in enumerate(tableau):
        x = TABLEAU_XS[col_idx]
        y = TABLEAU_Y
        for card in column:
            positions[card] = [x,y]
            if card.face_up:
                y += TABLEAU_FACE_UP_OFFSET
            else:
                y += TABLEAU_FACE_DOWN_OFFSET
    return positions

def get_tableau_card_at_pos(tableau, mouse_pos):
    positions = get_card_draw_positions(tableau)

    for col_idx in range(7):
        column = tableau[col_idx]
        for i in range(len(column) - 1, -1, -1):
            card = column[i]
            x, y = positions[card]
            rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
            if rect.collidepoint(mouse_pos):
                return col_idx, i, card
    return None

def get_foundation_at_pos(mouse_pos):
    for i, (x,y) in enumerate(FOUNDATION_POS):
        rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        if rect.collidepoint(mouse_pos):
            return i
    return None 

def get_tableau_column_at_pos(mouse_pos):
    mx, my = mouse_pos
    for col_idx, x in enumerate(TABLEAU_XS):
        rect = pygame.Rect(x, TABLEAU_Y, CARD_WIDTH, SCREEN_HEIGHT - TABLEAU_Y - 20)
        if rect.collidepoint((mx, my)):
            return col_idx
    return None

def stock_rect():
    return pygame.Rect(STOCK_POS[0], STOCK_POS[1], CARD_WIDTH, CARD_HEIGHT)

def waste_rect(waste, draw_count, waste_visible_count):
    if not waste:
        return pygame.Rect(WASTE_POS[0], WASTE_POS[1], CARD_WIDTH, CARD_HEIGHT)
    # draw one
    if draw_count == 1:
        visible_count = 1
    # draw three
    else:
        visible_count = min(waste_visible_count, len(waste))
    if visible_count <= 0:
        return pygame.Rect(WASTE_POS[0], WASTE_POS[1], 0, 0)
    x = WASTE_POS[0] + (visible_count - 1) * WASTE_CARD_OFFSET_X
    return pygame.Rect(x, WASTE_POS[1], CARD_WIDTH, CARD_HEIGHT)


def recycle_waste_to_stock(stock, waste):
    while waste:
        card = waste.pop()
        card.face_up = False
        #stock.insert(0, card)
        stock.append(card)

def draw_empty_slot(x, y, label=""):
    rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
    pygame.draw.rect(screen, DARK_GREEN, rect, border_radius=8)
    pygame.draw.rect(screen, GRAY, rect, 2, border_radius=8)
    if label:
        txt = SMALL_FONT.render(label, True, GRAY)
        screen.blit(txt, (x+8, y+8))


def remove_drag_card(tableau, waste, drag_info):
    if drag_info is None:
        return
    
    source = drag_info["source"]

    if source[0] == "tableau":
        col_idx = source[1]
        strart_idx = source[2]
        del tableau[col_idx][strart_idx:]

    elif source[0] == "waste":
        waste.pop()

def restore_drag_cards(tableau, waste, drag_info):
    if drag_info is None:
        return
    
    cards = drag_info["cards"]
    source = drag_info["source"]

    if source[0] == "tableau":
        col_idx = source[1]
        tableau[col_idx].extend(cards)

    elif source[0] == "waste":
        waste.append(cards[0])

def try_drop_drag(tableau, foundations, waste, drag_info, mouse_pos):
    if drag_info is None:
        return
    
    cards = drag_info["cards"]
    first_card = cards[0]

    foundation_idx = get_foundation_at_pos(mouse_pos)
    if foundation_idx is not None:
        if len(cards) == 1 and can_place_on_foundation(first_card, foundations[foundation_idx]):
            foundations[foundation_idx].append(first_card)
            return True
        
    target_col = get_tableau_column_at_pos(mouse_pos)
    if target_col is not None:
        if can_place_on_tableau(first_card, tableau[target_col]):
            tableau[target_col].extend(cards)
            return True
    
    return False

def draw_waste(waste, draw_count, waste_visible_count, current_back_index):
    if not waste:
        return

    # draw one
    if draw_count == 1:
        waste[-1].draw(screen, WASTE_POS[0], WASTE_POS[1], current_back_index)
        return
    # draw three
    if waste_visible_count <= 0:
        return
    
    visible_count = min(waste_visible_count, len(waste))
    visible_cards = waste[-visible_count:]
    for index, card in enumerate(visible_cards):
        x = WASTE_POS[0] + index * WASTE_CARD_OFFSET_X
        y = WASTE_POS[1]
        card.draw(screen, x, y, current_back_index)

def draw_timer(show_timing, elapsed_time):
    if not show_timing:
        return
    timer_text = SMALL_FONT.render(f"Time: {elapsed_time}", True, (0,0,0))
    timer_rect = timer_text.get_rect()
    timer_rect.bottomright = (SCREEN_WIDTH - 15, SCREEN_HEIGHT - 10)
    screen.blit(timer_text, timer_rect)


def draw_game(tableau, foundations, stock, waste, drag_info, 
              current_back_index, pending_back_index, 
              game_menu_open, deck_window_open, pressed_deck_button, option_window_open, pressed_option_button, 
              draw_count, pending_draw_count, waste_visible_count,
              show_timing, elapsed_time, pending_show_timing):
    screen.fill(BG)

    # stock
    if stock:
        screen.blit(CARD_BACK_IMAGES[current_back_index], STOCK_POS)
    else:
        screen.blit(STOCK_IMAGE, STOCK_POS)

    # waste
    draw_waste(waste, draw_count, waste_visible_count, current_back_index)

    # foundation
    for i in range(4):
        x, y = FOUNDATION_POS[i]
        if foundations[i]:
            foundations[i][-1].draw(screen, x, y, current_back_index, selected=False)
        else:
            screen.blit(FOUNDATION_IMAGE, (x,y))

    # tableau
    positions = get_card_draw_positions(tableau)
    for col_idx, column in enumerate(tableau):
        x = TABLEAU_XS[col_idx]
        for card in column:
            cx, cy = positions[card]
            card.draw(screen, cx, cy, current_back_index, selected=False)
    
    # dragging cards
    if drag_info is not None:
        cards = drag_info["cards"]
        drag_x = drag_info["draw_x"]
        drag_y = drag_info["draw_y"]

        for i, card in enumerate(cards):
            y = drag_y + i * TABLEAU_FACE_UP_OFFSET
            card.draw(screen, drag_x, y, current_back_index, selected=False)

    # win text
    if all(len(f) == 13 for f in foundations):
        text = FONT.render("You Win!", True, GOLD)
        screen.blit(text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))

    # draw timer
    draw_timer(show_timing, elapsed_time)

    # draw menu bar
    draw_menu_bar(game_menu_open)
    if deck_window_open:
        draw_deck_window(pending_back_index, pressed_deck_button)
    if option_window_open:
        draw_option_window(pressed_option_button, pending_draw_count, pending_show_timing)

    pygame.display.flip()

def restart_game():
    tableau, foundations, stock, waste = deal_new_game()
    waste_visible_count = 0
    drag_info = None

    timer_started = False
    timer_running = False
    timer_accumulated_ms = 0
    timer_segment_start = 0
    return (tableau, foundations, stock, waste, waste_visible_count, drag_info, timer_started, timer_running, timer_accumulated_ms, timer_segment_start)




#### LOAD IMAGES ####
CARD_IMAGES = load_card_images()
CARD_BACK_IMAGES = load_card_back_images()
FOUNDATION_IMAGE = load_slot_image(FOUNDATION_PATH)
STOCK_IMAGE = load_slot_image(STOCK_PATH)
## deck window ##
DECK_WINDOW_IMAGE = load_deck_window_image()
DECK_OK_NORMAL_IMAGE = load_button_image(DECK_OK_NORMAL_PATH, 150, 46)
DECK_OK_CLICKED_IMAGE = load_button_image(DECK_OK_CLICKED_PATH, 150, 46)
DECK_CANCEL_NORMAL_IMAGE = load_button_image(DECK_CANCEL_NORMAL_PATH, 150, 46)
DECK_CANCEL_CLICKED_IMAGE = load_button_image(DECK_CANCEL_CLICKED_PATH, 150, 46)
DECK_CROSS_NORMAL_IMAGE = load_button_image(DECK_CROSS_NORMAL_PATH, 32, 28)
DECK_CROSS_CLICKED_IMAGE = load_button_image(DECK_CROSS_CLICKED_PATH, 32, 28)
## option window ##
OPTION_WINDOW_IMAGE = load_option_window_image()
OPTION_OK_NORMAL_IMAGE = load_button_image(OPTION_OK_NORMAL_PATH, 150, 46)
OPTION_OK_CLICKED_IMAGE = load_button_image(OPTION_OK_CLICKED_PATH, 150, 46)
OPTION_CANCEL_NORMAL_IMAGE = load_button_image(OPTION_CANCEL_NORMAL_PATH, 150, 46)
OPTION_CANCEL_CLICKED_IMAGE = load_button_image(OPTION_CANCEL_CLICKED_PATH, 150, 46)
OPTION_CROSS_NORMAL_IMAGE = load_button_image(OPTION_CROSS_NORMAL_PATH, 32, 28)
OPTION_CROSS_CLICKED_IMAGE = load_button_image(OPTION_CROSS_CLICKED_PATH, 32, 28)
OPTION_DOT_IMAGE = load_button_image(OPTION_DOT_PATH, 8, 8)
OPTION_CHECK_IMAGE = load_button_image(OPTION_CHECK_PATH, 14, 14)


# --- MAIN --- #
def main():
    (tableau, foundations, stock, waste, waste_visible_count, drag_info, timer_started, timer_running, timer_accumulated_ms, timer_segment_start) = restart_game()
    drag_info = None

    game_menu_open = False
    deck_window_open = False
    option_window_open = False

    current_back_index = 0
    pending_back_index = 0

    pressed_deck_button = None
    pressed_option_button = None 

    # draw 1/3
    draw_count = 1
    pending_draw_count = 1

    # timing
    show_timing = True
    pending_show_timing = True
    timer_started = False
    timer_accumulated_ms = 0
    timer_segment_start = 0

    
    while True:
        clock.tick(60)

        # --- INPUT --- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    tableau, foundations, stock, waste = deal_new_game()
                    drag_info = None

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos

                # 1. deck window
                if deck_window_open:
                    clicked_thumbnail = get_deck_thumbnail_at_pos(mouse_pos)
                    if clicked_thumbnail is not None:
                        pending_back_index = clicked_thumbnail
                        continue

                    if DECK_OK_BUTTON_RECT.collidepoint(mouse_pos):
                        pressed_deck_button = "ok"
                        continue 

                    if DECK_CANCEL_BUTTON_RECT.collidepoint(mouse_pos):
                        pressed_deck_button = "cancel"
                        continue

                    if DECK_CROSS_BUTTON_RECT.collidepoint(mouse_pos):
                        pressed_deck_button = "cross"
                        continue

                    continue

                # 2. option window
                if option_window_open:
                    # draw one/three
                    if DRAW_ONE_CLICK_RECT.collidepoint(mouse_pos):
                        pending_draw_count = 1
                        continue

                    if DRAW_THREE_CLICK_RECT.collidepoint(mouse_pos):
                        pending_draw_count = 3
                        continue

                    # timer
                    if TIMING_CLICK_RECT.collidepoint(mouse_pos):
                        pending_show_timing = not pending_show_timing
                        continue

                    # ok/cancel/cross
                    if OPTION_OK_BUTTON_RECT.collidepoint(mouse_pos):
                        pressed_option_button = "ok"
                        continue

                    if OPTION_CANCEL_BUTTON_RECT.collidepoint(mouse_pos):
                        pressed_option_button = "cancel"
                        continue
                    
                    if OPTION_CROSS_BUTTON_RECT.collidepoint(mouse_pos):
                        pressed_option_button = "cross"
                        continue
                    # click the option circles
                    # prevent clicks from reaching the solitaire game
                    continue

                # 3. handle opened game dropdown
                if game_menu_open:
                    selected_item = get_game_menu_item_at_pos(mouse_pos)
                    if selected_item == "Deal":
                        (tableau, foundations, stock, waste, waste_visible_count, drag_info, timer_started, timer_running, timer_accumulated_ms, timer_segment_start) = restart_game()
                        drag_info = None
                        game_menu_open = False
                        continue

                    elif selected_item == "Undo":
                        print("Undo is not implemented yet")
                        game_menu_open = False
                        continue

                    elif selected_item == "Deck":
                        pending_back_index = current_back_index
                        # pause timer
                        (timer_running, timer_accumulated_ms) = pause_timer(timer_started, timer_running, timer_accumulated_ms, timer_segment_start)
                        pressed_deck_button = None
                        deck_window_open = True
                        game_menu_open = False
                        continue

                    elif selected_item == "Options":
                        pending_draw_count = draw_count
                        pending_show_timing = show_timing
                        # pause timer before opening modal
                        (timer_running, timer_accumulated_ms) = pause_timer(timer_started, timer_running, timer_accumulated_ms, timer_segment_start)

                        option_window_open = True
                        pressed_option_button = None
                        game_menu_open = False
                        drag_info = None
                        continue

                    elif selected_item == "Exit":
                        pygame.quit()
                        sys.exit()

                    # click game again to close dropdown menu
                    if GAME_BUTTON_RECT.collidepoint(mouse_pos):
                        game_menu_open = False
                        continue

                    #game_menu_open = False
                    continue

                # 4. handle the top bar
                if GAME_BUTTON_RECT.collidepoint(mouse_pos):
                    game_menu_open = True
                    drag_info = None
                    continue

                if HELP_BUTTON_RECT.collidepoint(mouse_pos):
                    print("Help Menu is not implemented yet")
                    drag_info = None
                    continue

                if mouse_pos[1] < MENU_BAR_HEIGHT:
                    continue


                # 5. click to flip top card
                hit = get_tableau_card_at_pos(tableau, mouse_pos)
                if hit: 
                    col_idx, card_idx, card = hit
                    if card_idx == len(tableau[col_idx]) - 1 and not card.face_up:
                        card.face_up = True
                        continue
                    
                # click stock
                if stock_rect().collidepoint(mouse_pos):
                    if stock:
                        number_to_draw = min(draw_count, len(stock))
                        for _ in range(number_to_draw):
                            card = stock.pop()
                            card.face_up = True
                            waste.append(card)
                        waste_visible_count = number_to_draw
                        # first action
                        if not timer_started:
                            (timer_started, timer_running_timer_segment_start) = start_timer(timer_started, timer_running, timer_segment_start)
                    else:
                        recycle_waste_to_stock(stock, waste)
                        waste_visible_count = 0
                
                # drag from waste
                if waste_rect(waste, draw_count, waste_visible_count).collidepoint(mouse_pos) and waste:
                    card = waste[-1]
                    top_waste_rect = waste_rect(waste, draw_count, waste_visible_count)
                    card_x = top_waste_rect.x
                    card_y = top_waste_rect.y
                    mouse_x, mouse_y = mouse_pos

                    drag_info = {
                        "cards": [card],
                        "source": ("waste",),
                        "offset_x": mouse_x - card_x,
                        "offset_y": mouse_y - card_y,
                        "draw_x": card_x,
                        "draw_y": card_y,
                        "old_waste_visible_count": waste_visible_count
                    }
                    #remove_drag_card(tableau, waste, drag_info)
                    waste.pop()
                    if draw_count == 3:
                        waste_visible_count -= 1
                        # if last card of visible group, reveal one card beneath
                        if waste_visible_count == 0 and len(waste) > 0:
                            waste_visible_count = 1


                if hit:
                    col_idx, card_idx, card = hit

                    if card.face_up:
                        moving_cards = tableau[col_idx][card_idx:]
                        positions = get_card_draw_positions(tableau)
                        card_x, card_y = positions[card]
                        mouse_x, mouse_y = mouse_pos

                        drag_info = {
                            "cards": moving_cards.copy(),
                            "source": ("tableau", col_idx, card_idx),
                            "offset_x": mouse_x - card_x,
                            "offset_y": mouse_y - card_y,
                            "draw_x": card_x,
                            "draw_y": card_y
                        }
                        remove_drag_card(tableau, waste, drag_info)
                        continue
            
            elif event.type == pygame.MOUSEMOTION:
                if drag_info is not None and not game_menu_open and not deck_window_open and not option_window_open:
                    mx, my = event.pos
                    drag_info["draw_x"] = mx - drag_info["offset_x"]
                    drag_info["draw_y"] = my - drag_info["offset_y"]

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pos = event.pos

                # deck window mouse up
                if deck_window_open:
                    if pressed_deck_button == "ok" and DECK_OK_BUTTON_RECT.collidepoint(mouse_pos):
                        current_back_index = pending_back_index
                        (timer_running, timer_segment_start) = resume_timer(timer_started, timer_running, timer_segment_start)
                        deck_window_open = False
                    elif pressed_deck_button == "cancel" and DECK_CANCEL_BUTTON_RECT.collidepoint(mouse_pos):
                        pending_back_index = current_back_index
                        (timer_running, timer_segment_start) = resume_timer(timer_started, timer_running, timer_segment_start)
                        deck_window_open = False
                    elif pressed_deck_button == "cross" and DECK_CROSS_BUTTON_RECT.collidepoint(mouse_pos):
                        pending_back_index = current_back_index
                        (timer_running, timer_segment_start) = resume_timer(timer_started, timer_running, timer_segment_start)
                        deck_window_open = False

                    pressed_deck_button = None
                    continue

                # option window mouse down
                if option_window_open:
                    if pressed_option_button == "ok" and OPTION_OK_BUTTON_RECT.collidepoint(mouse_pos):
                        # draw 1/3
                        draw_mode_changed = pending_draw_count != draw_count
                        draw_count = pending_draw_count
                        # timer
                        show_timing = pending_show_timing

                        # if draw 1/3 changed, start new game
                        if draw_mode_changed:
                            (tableau, foundations, stock, waste, waste_visible_count, drag_info, timer_started, timer_running, timer_accumulated_ms, timer_segment_start) = restart_game()
                        # reset timer state
                        else:
                            (timer_running, timer_segment_start) = resume_timer(timer_started, timer_running, timer_segment_start)

                        option_window_open = False

                    elif pressed_option_button == "cancel" and OPTION_CANCEL_BUTTON_RECT.collidepoint(mouse_pos):
                        pending_draw_count = draw_count
                        pending_show_timing = show_timing
                        (timer_running, timer_segment_start) = resume_timer(timer_started, timer_running, timer_segment_start)
                        option_window_open = False

                    elif pressed_option_button == "cross" and OPTION_CROSS_BUTTON_RECT.collidepoint(mouse_pos):
                        pending_draw_count = draw_count
                        pending_show_timing = show_timing
                        (timer_running, timer_segment_start) = resume_timer(timer_started, timer_running, timer_segment_start)
                        option_window_open = False
                
                    pressed_option_button = None
                    continue
                    

                if drag_info is not None and not game_menu_open and not deck_window_open and not option_window_open:
                    dropped = try_drop_drag(tableau, foundations, waste, drag_info, event.pos)
                    source = drag_info["source"]

                    if not dropped:
                        if source[0] == "waste":
                            waste.append(drag_info["cards"][0])
                            waste_visible_count = drag_info["old_waste_visible_count"]
                        else:
                            restore_drag_cards(tableau, waste, drag_info)
                    else:
                        # timer
                        if not timer_started:
                            (timer_started, timer_running, timer_segment_start) = start_timer(timer_started, timer_running, timer_segment_start)
                            timer_started = True
                            timer_started_ticks = pygame.time.get_ticks()
                        # draw 1/3
                        if source[0] == "waste" and draw_count == 3:
                            if waste_visible_count == 0:
                                waste_visible_count = min(3, len(waste))
                        

                    drag_info = None

        # timer
        elapsed_time = get_elapsed_seconds(timer_started, timer_running, timer_accumulated_ms, timer_segment_start)
        
        draw_game(tableau, foundations, stock, waste, drag_info, 
                  current_back_index, pending_back_index, 
                  game_menu_open, deck_window_open, pressed_deck_button, option_window_open, pressed_option_button, 
                  draw_count, pending_draw_count, waste_visible_count,
                  show_timing, elapsed_time, pending_show_timing)



if __name__ == "__main__":
    main()



