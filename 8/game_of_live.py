import time
import random


class GOL:
    def __init__(self):
        self.board = []
        self.length = int(input("Board width: "))
        self.height = int(input("Board height: "))

        for i in range(self.length):
            for i2 in range(self.height):
                self.board.append(0)

        active = input("Enter the active tiles as array or enter random for random ones:\n")
        if active == "random":
            counter = 0
            for i in self.board:
                self.board[counter] = random.randint(0, 1)
                counter += 1
        else:
            active = eval(active)
            for i in active:
                self.board[i] = 1

        print("Starting a StickyPiston Game Of Live (GOL) instance... ")

    def display(self):
        counter = 0
        render = ""

        for i in self.board:
            if i == 0:
                render += "██"
            else:
                render += "░░"

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
                    # print("Stays")
                case 3:
                    board.append(1)
                    # print("New")
                case _:
                    board.append(0)
                    # print("Dieing")
            counter += 1
        if self.board == board:
            print("Stopping StickyPiston Game Of Live (GOL) due to inactivity.")
            exit()
        self.board = board


if __name__ == "__main__":
    game = GOL()
    while True:
        game.display()
        game.tick()
        time.sleep(0.1)
