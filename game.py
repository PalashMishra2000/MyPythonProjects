class TicTacToe:
    def _init__(self):
        self.board = ['' for _ in range(9)] #using single list to rep 3x3 board
        self.current_winner = None #keep tracking winner
        
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
           #i = 0: self.board[0*3 : 1*3] → self.board[0:3] → [0, 1, 2]i = 1: self.board[1*3 : 2*3] → self.board[3:6] → [3, 4, 5]i = 2: self.board[2*3 : 3*3] → self.board[6:9] → [6, 7, 8] 
           print('| '+ '|'.join(row)+ ' |')
           
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+'|'.join(row) + ' |')
            
    def available_moves(self):
        moves = []
        for(i,spot) in enumerate(self.board):
            if spot == '':
                moves.append(i)
        return moves
    