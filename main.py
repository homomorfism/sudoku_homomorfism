from Controller.PlayerController import PlayerController


def main():
    who_plays = input("Who plays: 0 - human, 1 - computer, default: human. $ ")
    if who_plays == "" or "0":
        print("Ok, plays human")
        player_controller = PlayerController()
        player_controller.solve()

    else:
        raise NotImplemented


if __name__ == '__main__':
    main()
