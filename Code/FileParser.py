class FileParser:
    def __init__(self, path):
        self.path = path
        self.content = []

    def get_input(self, test):
        if test:
            with open("../TestInputs/" + self.path, newline='') as f:
                lines = f.readlines()

                for line in lines:
                    strip = line.strip()
                    self.content.append(strip)

        else:
            with open("../PuzzleInputs/" + self.path, newline='') as f:
                lines = f.readlines()

                for line in lines:
                    strip = line.strip()
                    self.content.append(strip)




def main():
    parser = FileParser("d1.in")
    parser.get_input(True)


if __name__ == "__main__":
    main()