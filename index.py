from includes.var import *
from classes.board import *
from classes.gameplay import *

class AI:
    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player

    def random_number (self, board):
        emptySquares = board.get_empty_tables()
        index = random.randrange(0, len(emptySquares))

        return emptySquares[index]

    def minimax_algo (self, board, maximizing):
        case = board.final_state()

        if case == 1:
            return 1, None
        
        if case == 2:
            return 2, None
        elif board.is_full():
            return 0, None
        
        if maximizing:
            maxEval = -100
            best_move = None
            empty_table = board.get_empty_tables()

            for (row, col) in empty_table:
                temporaryBoard = copy.deepcopy(board)
                temporaryBoard.marked_square(row, col, 1)
                eval = self.minimax_algo(temporaryBoard, False)[0]

                if eval > maxEval:
                    maxEval = eval
                    best_move = (row, col)
            return maxEval, best_move
        elif not maximizing:
            minEval = 100
            best_move = None;
            empty_table = board.get_empty_tables

            for (row, col) in empty_table:
                temporaryBoard = copy.deepcopy(board)
                temporaryBoard.marked_square(row, col, 1)
    
    def evaluate (self, mainBoard):
        if self.level == 0:
            eval = "random"
            move = self.random_number(mainBoard)
            print("AI has chosen to mark the square in position {} with an evaluation of {}".format(move, eval))
            return move

gameplay = Gameplay()
gameBoard = gameplay.board
ai = AI()

def move ():
    Board.marked_square(row, col, gameplay.player)
    gameplay.draw_figures(row, col)
    gameplay.next_turn()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            row = pos[1] // box
            col = pos[0] // box
            if gameBoard.empty_square(row, col) and gameplay.running:
                """ gameBoard.marked_square(row, col, gameplay.player)
                gameplay.draw_figures(row, col)
                gameplay.next_turn() """
                gameplay.make_move(row, col)
                if gameplay.is_over():
                    gameplay.running = False
    if gameplay.gamemode == "ai" and gameplay.player == ai.player and gameplay.running:
        print(ai.random_number(gameBoard))
        row, col = ai.evaluate(gameBoard)
        gameplay.make_move(col, row)

    pygame.display.update()
