class KeepPlaying:

    def __init__(self):
        self.playAgain = True

    def replayGame(self):
        replay = input("Keep Playing? Y/N: ")
        replay = replay.lower()
        if replay in ("n", "no"):
            self.playAgain = False