from FileParser import FileParser
# TODO So many helper methods. There has to be an easier way


class RPSPlayer:
    def __init__(self, test):
        self.parser = FileParser("d2.in")

        self.round_info = []
        self.parse_input(test)

    def parse_input(self, test):
        self.parser.get_input(test)

        for line in self.parser.content:
            split = line.split()

            self.round_info.append(split)

    def get_part1_score(self):
        score = 0
        for round in self.round_info:
            score += self.is_win_part1(round)
            score += self.shape(round[1])
        print("Part 1 " + score.__str__())

    def get_part2_score(self):
        score = 0
        for round in self.round_info:
            score += self.is_win_part2(round[1].upper())
            score += self.shape(self.get_play(round))
        print("Part 2 " + score.__str__())

    def is_win_part1(self, round):
        opponent = self.shape(round[0])
        you = self.shape(round[1])

        # 3 is a draw, 0 is a loss, 6 is a win
        if opponent == you:
            return 3

        # They are Rock
        if opponent == 1:
            # You are Paper
            if you == 2:
                return 6
            # You are Scissors
            else:
                return 0
        # They are Paper
        elif opponent == 2:
            # You are Rock
            if you == 1:
                return 0
            # You are Scissors
            else:
                return 6
        # They are Scissors
        else:
            # You are Rock
            if you == 1:
                return 6
            # You are Paper
            else:
                return 0

    @staticmethod
    def is_win_part2(char):
        if char == 'X':
            return 0
        elif char == 'Y':
            return 3
        else:
            return 6

    def get_play(self, round):
        opponent = round[0]

        # Need to Lose
        if round[1].upper() == 'X':
            return self.get_loss(opponent)

        # Need to Draw
        elif round[1].upper() == 'Y':
            temp = opponent
            return temp

        # Need to win
        else:
            return self.get_win(opponent)

    @staticmethod
    def get_loss(char):
        if char == 'A':
            return 'C'
        elif char == 'B':
            return 'A'
        return 'B'

    @staticmethod
    def get_win(char):
        if char == 'A':
            return 'B'
        elif char == 'B':
            return 'C'
        return 'A'

    @staticmethod
    def shape(char):
        switch = {
            'X': 1,
            'x': 1,
            'A': 1,
            'a': 1,
            'Y': 2,
            'y': 2,
            'B': 2,
            'b': 2,
            'Z': 3,
            'z': 3,
            'C': 3,
            'c': 3
        }
        return switch.get(char, "Invalid Input")


def main():
    player = RPSPlayer(False)

    player.get_part1_score()
    player.get_part2_score()


if __name__ == "__main__":
    main()