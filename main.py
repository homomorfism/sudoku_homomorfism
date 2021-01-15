from Controller.ComputerController import ComputerController
from Controller.PlayerController import PlayerController


def main():
    who_plays = input("Who plays: 0 - human, 1 - computer, default: human. $ ")
    if who_plays == "" or who_plays == "0":
        print("Ok, plays human")
        player_controller = PlayerController()
        if player_controller.solve():
            print("The solution was found!")
            player_controller.game.plot()

    else:
        print("Ok, plays computer")
        computer_controller = ComputerController()
        if computer_controller.solve():
            print("The solution was found!")
            computer_controller.game.plot()


if __name__ == '__main__':
    main()
