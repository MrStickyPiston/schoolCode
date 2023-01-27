class GOL:
    def __init__(self):
        self.board = []
        self.length = int(input())
        self.height = int(input())

        for i in range(self.length):
            for i2 in range(self.height):
                self.board.append(0)

        self.board = [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def display(self):
        counter = 0
        render = ""
        print(self.board)

        for i in self.board:
            if i == 0:
                render += "██ "
            else:
                render += "░░ "

            counter += 1

            if counter == self.length:
                render += "\n"
                counter = 0
        print(render)

    def tick(self):
        counter = 0
        board = []
        for i in self.board:
            surrounding = 0
            try:
                surrounding += self.board[counter - 1 - self.length]
            except Exception:
                pass
            try:
                surrounding += self.board[counter - self.length]
            except Exception:
                pass
            try:
                surrounding += self.board[counter + 1 - self.length]
            except Exception:
                pass
            try:
                surrounding += self.board[counter - 1]
            except Exception:
                pass
            try:
                surrounding += self.board[counter + 1]
            except Exception:
                pass
            try:
                surrounding += self.board[counter - 1 + self.length]
            except Exception:
                pass
            try:
                surrounding += self.board[counter + self.length]
            except Exception:
                pass
            try:
                surrounding += self.board[counter + 1 + self.length]
            except Exception:
                pass

            match surrounding:
                case 2:
                    board.append(i)
                    #print("Stays")
                case 3:
                    board.append(1)
                    #print("New")
                case _:
                    board.append(0)
                    #print("Dieing")
            counter += 1
        self.board = board


game = GOL()
game.display()
game.tick()
game.display()
game.tick()
game.display()
