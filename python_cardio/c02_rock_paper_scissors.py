def rock_paper_scissors(choose1: str, choose2: str) -> str:
    if (
        (choose1 == "rock" and choose2 == "paper")
        or (choose1 == "scissors" and choose2 == "rock")
        or (choose1 == "paper" and choose2 == "scissors")
    ):
        return "player 2"
    else:
        return "player 1"


if __name__ == "__main__":
    win = rock_paper_scissors("rock", "paper")
    print("The winer is {}".format(win))
