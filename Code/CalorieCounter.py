from FileParser import FileParser


class CalorieCounter:
    def __init__(self):
        self.parser = FileParser("d1.in")

        self.calorie_counts = []
        self.max = 0

    def calculate(self, test):
        self.parser.get_input(test)

        sum = 0
        for dataPoint in self.parser.content:
            try:
                num = int(dataPoint)
                sum += num

            except:
                self.calorie_counts.append(sum)
                if sum > self.max:
                    temp = sum
                    self.max = temp

                sum = 0

    def get_max_three(self):
        self.calorie_counts.sort(reverse=True)
        return self.calorie_counts[0] + self.calorie_counts[1] + self.calorie_counts[2]


def main():
    counter = CalorieCounter()
    counter.calculate(False)

    print(counter.max)
    print(counter.get_max_three())


if __name__ == "__main__":
    main()
