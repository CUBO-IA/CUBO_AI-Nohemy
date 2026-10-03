import pygame
import random

# ============================================================
# INICIALIZACIÓN
# ============================================================

pygame.init()

# ============================================================
# CONFIGURACIÓN DE LA VENTANA
# ============================================================

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 720

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
FPS = 60


# ============================================================
# COLORES
# ============================================================

BACKGROUND = (12, 15, 24)
BOARD_BACKGROUND = (18, 22, 34)
GRID_COLOR = (35, 42, 58)

WHITE = (245, 247, 250)
LIGHT_GRAY = (160, 170, 185)

CYAN = (0, 220, 255)
BLUE = (60, 110, 255)
PURPLE = (170, 70, 240)
GREEN = (50, 220, 130)
YELLOW = (255, 210, 60)
ORANGE = (255, 145, 50)
RED = (240, 70, 80)


# ============================================================
# CONFIGURACIÓN DEL TABLERO
# ============================================================

BOARD_COLUMNS = 10
BOARD_ROWS = 20

BLOCK_SIZE = 30

BOARD_WIDTH = BOARD_COLUMNS * BLOCK_SIZE
BOARD_HEIGHT = BOARD_ROWS * BLOCK_SIZE

BOARD_X = 100
BOARD_Y = 90


# ============================================================
# PANEL
# ============================================================

PANEL_X = 470
PANEL_WIDTH = 330


# ============================================================
# FUENTES
# ============================================================

font_title = pygame.font.Font(None, 72)
font_section = pygame.font.Font(None, 32)
font_value = pygame.font.Font(None, 42)
font_small = pygame.font.Font(None, 24)
font_game_over = pygame.font.Font(None, 70)


# ============================================================
# PIEZAS
# ============================================================

PIECES = [

    # I
    {
        "shape": [
            [1, 1, 1, 1]
        ],
        "color": CYAN
    },

    # O
    {
        "shape": [
            [1, 1],
            [1, 1]
        ],
        "color": YELLOW
    },

    # T
    {
        "shape": [
            [0, 1, 0],
            [1, 1, 1]
        ],
        "color": PURPLE
    },

    # S
    {
        "shape": [
            [0, 1, 1],
            [1, 1, 0]
        ],
        "color": GREEN
    },

    # Z
    {
        "shape": [
            [1, 1, 0],
            [0, 1, 1]
        ],
        "color": RED
    },

    # J
    {
        "shape": [
            [1, 0, 0],
            [1, 1, 1]
        ],
        "color": BLUE
    },

    # L
    {
        "shape": [
            [0, 0, 1],
            [1, 1, 1]
        ],
        "color": ORANGE
    }
]


# ============================================================
# CREAR TABLERO
# ============================================================

def create_board():

    return [
        [None for _ in range(BOARD_COLUMNS)]
        for _ in range(BOARD_ROWS)
    ]


board = create_board()


# ============================================================
# CREAR PIEZA
# ============================================================

def create_piece():

    data = random.choice(PIECES)

    # Copiamos la matriz para no modificar la original
    shape = [row[:] for row in data["shape"]]

    piece = {
        "shape": shape,
        "color": data["color"],
        "x": BOARD_COLUMNS // 2 - len(shape[0]) // 2,
        "y": 0
    }

    return piece


# ============================================================
# COLISIÓN
# ============================================================

def check_collision(piece, board, offset_x=0, offset_y=0):

    shape = piece["shape"]

    for row_index, row in enumerate(shape):

        for column_index, cell in enumerate(row):

            if not cell:
                continue

            x = piece["x"] + column_index + offset_x
            y = piece["y"] + row_index + offset_y

            # Borde izquierdo / derecho
            if x < 0 or x >= BOARD_COLUMNS:
                return True

            # Suelo
            if y >= BOARD_ROWS:
                return True

            # No comprobamos fuera de la parte superior
            if y >= 0:

                if board[y][x] is not None:
                    return True

    return False


# ============================================================
# FIJAR PIEZA AL TABLERO
# ============================================================

def lock_piece(piece, board):

    shape = piece["shape"]

    for row_index, row in enumerate(shape):

        for column_index, cell in enumerate(row):

            if not cell:
                continue

            x = piece["x"] + column_index
            y = piece["y"] + row_index

            if 0 <= y < BOARD_ROWS:
                board[y][x] = piece["color"]


# ============================================================
# ELIMINAR LÍNEAS
# ============================================================

def clear_lines(board):

    new_board = []

    lines = 0

    for row in board:

        if all(cell is not None for cell in row):

            lines += 1

        else:

            new_board.append(row)

    # Agregar filas vacías arriba
    while len(new_board) < BOARD_ROWS:

        new_board.insert(
            0,
            [None for _ in range(BOARD_COLUMNS)]
        )

    return new_board, lines


# ============================================================
# ROTAR PIEZA
# ============================================================

def rotate_piece(piece):

    old_shape = piece["shape"]

    # Rotación 90 grados
    new_shape = [
        list(row)
        for row in zip(*old_shape[::-1])
    ]

    old_x = piece["x"]

    piece["shape"] = new_shape

    # Si la rotación genera una colisión,
    # intentamos devolver la pieza a su posición anterior.
    if check_collision(piece, board):

        piece["shape"] = old_shape
        piece["x"] = old_x


# ============================================================
# DIBUJAR BLOQUE
# ============================================================

def draw_block(x, y, color):

    pixel_x = BOARD_X + x * BLOCK_SIZE
    pixel_y = BOARD_Y + y * BLOCK_SIZE

    # Bloque principal
    pygame.draw.rect(
        screen,
        color,
        (
            pixel_x + 2,
            pixel_y + 2,
            BLOCK_SIZE - 4,
            BLOCK_SIZE - 4
        ),
        border_radius=5
    )

    # Brillo superior
    pygame.draw.line(
        screen,
        tuple(min(c + 50, 255) for c in color),
        (pixel_x + 5, pixel_y + 5),
        (pixel_x + BLOCK_SIZE - 6, pixel_y + 5),
        2
    )


# ============================================================
# DIBUJAR TABLERO
# ============================================================

def draw_board():

    pygame.draw.rect(
        screen,
        BOARD_BACKGROUND,
        (
            BOARD_X,
            BOARD_Y,
            BOARD_WIDTH,
            BOARD_HEIGHT
        ),
        border_radius=8
    )

    # Cuadrícula
    for column in range(BOARD_COLUMNS + 1):

        x = BOARD_X + column * BLOCK_SIZE

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (x, BOARD_Y),
            (x, BOARD_Y + BOARD_HEIGHT)
        )

    for row in range(BOARD_ROWS + 1):

        y = BOARD_Y + row * BLOCK_SIZE

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (BOARD_X, y),
            (BOARD_X + BOARD_WIDTH, y)
        )

    # Bloques fijados
    for row in range(BOARD_ROWS):

        for column in range(BOARD_COLUMNS):

            color = board[row][column]

            if color is not None:

                draw_block(
                    column,
                    row,
                    color
                )

    # Borde
    pygame.draw.rect(
        screen,
        (70, 80, 100),
        (
            BOARD_X,
            BOARD_Y,
            BOARD_WIDTH,
            BOARD_HEIGHT
        ),
        width=3,
        border_radius=8
    )


# ============================================================
# DIBUJAR PIEZA ACTUAL
# ============================================================

def draw_piece(piece):

    shape = piece["shape"]

    for row_index, row in enumerate(shape):

        for column_index, cell in enumerate(row):

            if cell:

                x = piece["x"] + column_index
                y = piece["y"] + row_index

                if y >= 0:

                    draw_block(
                        x,
                        y,
                        piece["color"]
                    )


# ============================================================
# TEXTO
# ============================================================

def draw_text(
    text,
    font,
    color,
    x,
    y,
    center=False
):

    surface = font.render(
        text,
        True,
        color
    )

    if center:

        rect = surface.get_rect(
            center=(x, y)
        )

    else:

        rect = surface.get_rect(
            topleft=(x, y)
        )

    screen.blit(
        surface,
        rect
    )


# ============================================================
# TÍTULO
# ============================================================

def draw_title():

    draw_text(
        "TETRIS",
        font_title,
        WHITE,
        BOARD_X + BOARD_WIDTH // 2,
        45,
        center=True
    )


# ============================================================
# TARJETA
# ============================================================

def draw_card(
    x,
    y,
    width,
    height,
    title,
    value,
    color
):

    pygame.draw.rect(
        screen,
        (22, 27, 40),
        (
            x,
            y,
            width,
            height
        ),
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        (45, 53, 70),
        (
            x,
            y,
            width,
            height
        ),
        width=2,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        color,
        (
            x,
            y,
            5,
            height
        ),
        border_radius=3
    )

    draw_text(
        title,
        font_section,
        LIGHT_GRAY,
        x + 25,
        y + 15
    )

    draw_text(
        str(value),
        font_value,
        color,
        x + 25,
        y + 50
    )


# ============================================================
# PANEL
# ============================================================

def draw_panel(score, lines, level, next_piece):

    draw_card(
        PANEL_X,
        100,
        PANEL_WIDTH,
        100,
        "SCORE",
        score,
        CYAN
    )

    draw_card(
        PANEL_X,
        215,
        PANEL_WIDTH,
        100,
        "LINES",
        lines,
        GREEN
    )

    draw_card(
        PANEL_X,
        330,
        PANEL_WIDTH,
        100,
        "LEVEL",
        level,
        YELLOW
    )

    # --------------------------------------------------------
    # NEXT
    # --------------------------------------------------------

    next_x = PANEL_X
    next_y = 455
    next_width = PANEL_WIDTH
    next_height = 180

    pygame.draw.rect(
        screen,
        (22, 27, 40),
        (
            next_x,
            next_y,
            next_width,
            next_height
        ),
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        (45, 53, 70),
        (
            next_x,
            next_y,
            next_width,
            next_height
        ),
        width=2,
        border_radius=10
    )

    draw_text(
        "NEXT",
        font_section,
        LIGHT_GRAY,
        next_x + 25,
        next_y + 15
    )

    # Dibujar siguiente pieza
    shape = next_piece["shape"]
    color = next_piece["color"]

    block_size = 25

    shape_width = len(shape[0]) * block_size
    shape_height = len(shape) * block_size

    start_x = next_x + (next_width - shape_width) // 2
    start_y = next_y + 85 - shape_height // 2

    for row_index, row in enumerate(shape):

        for column_index, cell in enumerate(row):

            if cell:

                x = start_x + column_index * block_size
                y = start_y + row_index * block_size

                pygame.draw.rect(
                    screen,
                    color,
                    (
                        x,
                        y,
                        block_size - 2,
                        block_size - 2
                    ),
                    border_radius=4
                )


# ============================================================
# CONTROLES
# ============================================================

def draw_controls():

    draw_text(
        "← →  Mover",
        font_small,
        LIGHT_GRAY,
        BOARD_X,
        705
    )

    draw_text(
        "↓  Bajar",
        font_small,
        LIGHT_GRAY,
        BOARD_X + 140,
        705
    )

    draw_text(
        "↑  Rotar",
        font_small,
        LIGHT_GRAY,
        BOARD_X + 250,
        705
    )

    draw_text(
        "SPACE  Caída",
        font_small,
        LIGHT_GRAY,
        BOARD_X + 370,
        705
    )


# ============================================================
# GAME OVER
# ============================================================

def draw_game_over():

    # Oscurecer tablero
    overlay = pygame.Surface(
        (BOARD_WIDTH, BOARD_HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 180)
    )

    screen.blit(
        overlay,
        (BOARD_X, BOARD_Y)
    )

    draw_text(
        "GAME OVER",
        font_game_over,
        RED,
        BOARD_X + BOARD_WIDTH // 2,
        BOARD_Y + BOARD_HEIGHT // 2 - 30,
        center=True
    )

    draw_text(
        "Presiona ENTER para reiniciar",
        font_small,
        WHITE,
        BOARD_X + BOARD_WIDTH // 2,
        BOARD_Y + BOARD_HEIGHT // 2 + 35,
        center=True
    )


# ============================================================
# REINICIAR JUEGO
# ============================================================

def reset_game():

    global board

    board = create_board()

    current_piece = create_piece()
    next_piece = create_piece()

    return current_piece, next_piece


# ============================================================
# INICIO DEL JUEGO
# ============================================================

current_piece, next_piece = reset_game()

score = 0
lines = 0
level = 1

fall_timer = 0

game_over = False


# ============================================================
# BUCLE PRINCIPAL
# ============================================================

running = True

while running:

    # Tiempo transcurrido desde el último frame
    delta_time = clock.tick(FPS)

    # ========================================================
    # EVENTOS
    # ========================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            # ESC
            if event.key == pygame.K_ESCAPE:

                running = False

            # ------------------------------------------------
            # REINICIAR DESPUÉS DE GAME OVER
            # ------------------------------------------------

            if game_over:

                if event.key == pygame.K_RETURN:

                    current_piece, next_piece = reset_game()

                    score = 0
                    lines = 0
                    level = 1

                    fall_timer = 0

                    game_over = False

                continue

            # ------------------------------------------------
            # MOVER IZQUIERDA
            # ------------------------------------------------

            if event.key == pygame.K_LEFT:

                if not check_collision(
                    current_piece,
                    board,
                    -1,
                    0
                ):

                    current_piece["x"] -= 1

            # ------------------------------------------------
            # MOVER DERECHA
            # ------------------------------------------------

            elif event.key == pygame.K_RIGHT:

                if not check_collision(
                    current_piece,
                    board,
                    1,
                    0
                ):

                    current_piece["x"] += 1

            # ------------------------------------------------
            # BAJAR
            # ------------------------------------------------

            elif event.key == pygame.K_DOWN:

                if not check_collision(
                    current_piece,
                    board,
                    0,
                    1
                ):

                    current_piece["y"] += 1

                    score += 1

            # ------------------------------------------------
            # ROTAR
            # ------------------------------------------------

            elif event.key == pygame.K_UP:

                rotate_piece(
                    current_piece
                )

            # ------------------------------------------------
            # CAÍDA INSTANTÁNEA
            # ------------------------------------------------

            elif event.key == pygame.K_SPACE:

                while not check_collision(
                    current_piece,
                    board,
                    0,
                    1
                ):

                    current_piece["y"] += 1

                    score += 2

                lock_piece(
                    current_piece,
                    board
                )

                board, cleared = clear_lines(board)

                if cleared > 0:

                    score += cleared * 100

                    lines += cleared

                    level = lines // 10 + 1

                current_piece = next_piece
                next_piece = create_piece()

                if check_collision(
                    current_piece,
                    board
                ):

                    game_over = True

    # ========================================================
    # GRAVEDAD AUTOMÁTICA
    # ========================================================

    if not game_over:

        fall_timer += delta_time

        # Más nivel = más rápido
        fall_speed = max(
            100,
            600 - (level - 1) * 50
        )

        if fall_timer >= fall_speed:

            fall_timer = 0

            if not check_collision(
                current_piece,
                board,
                0,
                1
            ):

                current_piece["y"] += 1

            else:

                # Fijar pieza
                lock_piece(
                    current_piece,
                    board
                )

                # Eliminar líneas
                board, cleared = clear_lines(
                    board
                )

                if cleared > 0:

                    score += cleared * 100
                    lines += cleared
                    level = lines // 10 + 1

                # Siguiente pieza
                current_piece = next_piece
                next_piece = create_piece()

                # Comprobar Game Over
                if check_collision(
                    current_piece,
                    board
                ):

                    game_over = True

    # ========================================================
    # DIBUJAR
    # ========================================================

    screen.fill(
        BACKGROUND
    )

    draw_title()

    draw_board()

    if not game_over:

        draw_piece(
            current_piece
        )

    draw_panel(
        score,
        lines,
        level,
        next_piece
    )

    draw_controls()

    if game_over:

        draw_game_over()

    pygame.display.flip()


# ============================================================
# CERRAR PYGAME
# ============================================================

pygame.quit()
