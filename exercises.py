class Game():
    board = {
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
}
    
    def __init__(self, turn = 'X', tie = False, winner = None, board = board ):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if (self.tie == True):
            print("Tie game!")
            return
        if (self.winner != None):
            print(f"{self.winner} wins the game!")
            return
        print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            for key, value in self.board.items():
                if key == move and self.board[key] is None:
                    self.board[key] = self.turn
                    return
            print("Invalid input, enter the cell again!")

    def check_for_winner(self):
        winning_combination = {
        '1':('a1','b1','c1'),
        '2':('a2','b2','c2'),
        '3':('a3','b3','c3'),
        '4':('a1','a2','a3'),
        '5':('b1','b2','b3'),
        '6':('c1','c2','c3'),
        '7':('a1','b2','c3'),
        '8':('c1','b2','a3')
        }
        for key, val in winning_combination.items():
            if (self.board[val[0]] and (self.board[val[0]] == self.board[val[1]] == self.board[val[2]])):
                self.winner = self.board[val[0]]
                return

    def check_for_tie(self):
        if (self.winner != None):
            return
        for key, val in self.board.items():
            if val == None:
                return
        self.tie = True

    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def play_game(self):
        print("Shall we play a game?")
        while True:
            self.render()
            if self.winner == None and self.tie == False:
                self.get_move()
                self.check_for_winner()
                self.check_for_tie()
                self.switch_turn()
            else:
                break
        

game_instance = Game()
game_instance.play_game()
