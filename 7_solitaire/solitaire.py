# --- IMPORT --- #
import pygame
import random
import sys

# --- CONFIG --- #
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

pygame.init()
pygame.display.set_caption("SOLITAIRE")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


BG = (20, 120, 50)
WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
RED = (200, 40, 40)
GOLD = (220, 190, 60)
GRAY = (180, 180, 180)
DARK_GREEN = (10, 90, 35)
BLUE = (70, 130, 220)

CARD_WIDTH = 120
CARD_HEIGHT = 160
TABLEAU_GAP_X = 20
TABLEAU_FACE_DOWN_OFFSET = 8
TABLEAU_FACE_UP_OFFSET = 30

TOP_MARGIN = 30
LEFT_MARGIN = 20
STOCK_POS = (LEFT_MARGIN, TOP_MARGIN)
WASTE_POS = (LEFT_MARGIN + CARD_WIDTH + 20, TOP_MARGIN)

FOUNDATION_START_X = SCREEN_WIDTH - LEFT_MARGIN - (CARD_WIDTH * 4 + 20 * 3)
FOUNDATION_Y = TOP_MARGIN
FOUNDATION_POS = [(FOUNDATION_START_X + i * (CARD_WIDTH + 20), FOUNDATION_Y) for i in range(4)]

TABLEAU_Y = TOP_MARGIN + CARD_HEIGHT + 50
TABLEAU_XS = [LEFT_MARGIN + i * (CARD_WIDTH + TABLEAU_GAP_X) for i in range(7)]

FONT = pygame.font.SysFont("arial", 24)
SMALL_FONT = pygame.font.SysFont("arial", 18)

SUITS = ["♠︎", "♣︎", "♥︎", "♦︎"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUIT_TO_COLOR = {
    "♠︎": "black",
    "♣︎": "black",
    "♥︎": "red",
    "♦︎": "red"
}


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
    
    def draw(self, surface, x, y, selected=False):
        self.rect.topleft = (x,y)
        
        if self.face_up:
            pygame.draw.rect(surface, WHITE, self.rect, border_radius=8)
            pygame.draw.rect(surface, BLUE if selected else BLACK, self.rect, 2, border_radius=8)

            text_color = RED if self.color == "red" else BLACK
            top_text = FONT.render(f"{self.rank}{self.suit}", True, text_color)
            surface.blit(top_text, (x+8, y+8))

            bottom_text = FONT.render(f"{self.rank}{self.suit}", True, text_color)
            bottom_rot = pygame.transform.rotate(bottom_text, 180)
            surface.blit(bottom_rot, (x + CARD_WIDTH - bottom_rot.get_width() - 8, y + CARD_HEIGHT - bottom_rot.get_height() - 8))
        else:
            pygame.draw.rect(surface, (30,60,140), self.rect, border_radius=8)
            pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=8)

            for i in range(6):
                pygame.draw.line(surface, (180, 220, 255), (x + 10, y +15 + i * 18), (x + CARD_WIDTH - 10, y + 5 + i * 18), 2)



# --- FUNCTIONS --- #
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
        return card.rank == "K"
    
    top_card = target_column[-1]
    if not top_card.face_up:
        return False 
    
    return top_card.value == card.value + 1 and top_card.color != card.color

def can_place_on_foundation(card, foundation):
    if not foundation:
        return card.rank == "A"
    
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

def waste_rect():
    return pygame.Rect(WASTE_POS[0], WASTE_POS[1], CARD_WIDTH, CARD_HEIGHT)


def recycle_waste_to_stock(stock, waste):
    while waste:
        card = waste.pop()
        card.face_up = False
        stock.insert(0, card)

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


def draw_game(tableau, foundations, stock, waste, drag_info):
    screen.fill(BG)

    # stock
    if stock:
        pygame.draw.rect(screen, (30,60,140), stock_rect(), border_radius=8)
        pygame.draw.rect(screen, BLACK, stock_rect(), 2, border_radius=8)
    else:
        draw_empty_slot(*STOCK_POS, "Stock")

    # waste
    if waste:
        waste[-1].draw(screen, *WASTE_POS, selected=False)
    else:
        draw_empty_slot(*WASTE_POS, "Waste")

    # foundation
    for i in range(4):
        x, y = FOUNDATION_POS[i]
        if foundations[i]:
            foundations[i][-1].draw(screen, x, y, selected=False)
        else:
            draw_empty_slot(x,y, "A")

    # tableau
    positions = get_card_draw_positions(tableau)
    for col_idx, column in enumerate(tableau):
        x = TABLEAU_XS[col_idx]
        if not column:
            draw_empty_slot(x, TABLEAU_Y, "K")
        for card in column:
            cx, cy = positions[card]
            card.draw(screen, cx, cy, selected=False)
    
    # dragging cards
    if drag_info is not None:
        cards = drag_info["cards"]
        drag_x = drag_info["draw_x"]
        drag_y = drag_info["draw_y"]

        for i, card in enumerate(cards):
            y = drag_y + i * TABLEAU_FACE_UP_OFFSET
            card.draw(screen, drag_x, y, selected=False)

    # win text
    if all(len(f) == 13 for f in foundations):
        text = FONT.render("You Win!", True, GOLD)
        screen.blit(text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))

    pygame.display.flip()



# --- MAIN --- #
def main():
    tableau, foundations, stock, waste = deal_new_game()
    drag_info = None
    
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

                # click to flip top card
                hit = get_tableau_card_at_pos(tableau, mouse_pos)
                if hit: 
                    col_idx, card_idx, card = hit
                    if card_idx == len(tableau[col_idx]) - 1 and not card.face_up:
                        card.face_up = True
                        continue
                    
                # click stock
                if stock_rect().collidepoint(mouse_pos):
                    if stock:
                        card = stock.pop()
                        card.face_up = True
                        waste.append(card)
                    else:
                        recycle_waste_to_stock(stock, waste)
                
                # drag from waste
                if waste_rect().collidepoint(mouse_pos) and waste:
                    card = waste[-1]
                    mouse_x, mouse_y = mouse_pos
                    offset_x = mouse_x - WASTE_POS[0]
                    offset_y = mouse_y - WASTE_POS[1]

                    drag_info = {
                        "cards": [card],
                        "source": ["waste"],
                        "offset_x": offset_x,
                        "offset_y": offset_y,
                        "draw_x": WASTE_POS[0],
                        "draw_y": WASTE_POS[1]
                    }
                    remove_drag_card(tableau, waste, drag_info)

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
                if drag_info is not None:
                    mx, my = event.pos
                    drag_info["draw_x"] = mx - drag_info["offset_x"]
                    drag_info["draw_y"] = my - drag_info["offset_y"]

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drag_info is not None:
                    dropped = try_drop_drag(tableau, foundations, waste, drag_info, event.pos)

                    if not dropped:
                        restore_drag_cards(tableau, waste, drag_info)

                    drag_info = None

                    
        draw_game(tableau, foundations, stock, waste, drag_info)




if __name__ == "__main__":
    main()



