from collections import Counter


class Game:

    def __init__(self):
        self.feed = []
        self.hor_lines = []
        self.vert_lines = []
        self.squares = {}
        self.rep_values = []
        self.rep_indexes = []
        self.template = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None,
                         '8': None, '9': None}

    def feeding(self, file=0):
        temp = ""
        self.feed = []
        self.hor_lines = []
        self.vert_lines = []
        self.squares = {}
        with open("sudoku.txt", "r") as file:
            temp = file.read().strip()
            temp = temp.split("\n")

            self.hor_lines = list(temp)

            for i in range(0, len(temp)):
                get = ""
                for value in temp:
                    get += value[i]
                self.vert_lines.append(get)

                # feeding squares
                n = 0
                squares = []
                names = ["A0", "A1", "A2", "B0", "B1", "B2", "C0", "C1", "C2"]

                for num in range(0, 3):
                    a, b = 0, 3
                    for num in range(0, 3):
                        squares.append(temp[n][a:b] + temp[n + 1][a:b] +
                                       temp[n + 2][a:b])
                        a, b, = a + 3, b + 3
                    n += 3

                self.squares = dict(zip(names, squares))

            for val in temp:
                for i in range(0, 9):
                    self.feed.append(val[i])

    def setting_template(self):
        for i in self.template.keys():
            self.template[i] = None

    def checking_field(self, horz_index, vert_index, square_index):
        self.setting_template()
        for value in self.hor_lines[horz_index]:
            if value == "0":
                continue
            else:
                self.template[value] = True

        for value in self.vert_lines[vert_index]:
            if value == "0":
                continue
            else:
                self.template[value] = True

        for value in self.squares[square_index]:
            if value == "0":
                continue
            else:
                self.template[value] = True

        if list(self.template.values()).count(True) == 8:
            self.feed[horz_index * 9 + vert_index] = \
            dict(zip(list(self.template.values()), list(self.template.keys())))[None]
            # dict(zip(list(self.template.values()),list(self.template.keys())))[None]

        elif list(self.template.values()).count(True) == 7:
            temp_values = ""
            temp_indexes = str(horz_index)+str(vert_index)+str(square_index)
            print("---"*10)
            print(f"horz_index: {horz_index}, vert_index: {vert_index}, square: {square_index}"
                  f" ma 7 zaliczonych.")
            print(f"Do wyboru pozostaje:", end=" ")
            for k,v in self.template.items():
                if v == None:
                    print(k, end=" ")
                    temp_values += k

            print(f"\n{s.template}")
            self.rep_values.append(temp_values)
            self.rep_indexes.append(temp_indexes)

        else:
            return False

    def which_square(self, horz_index, vert_index):
        which_square = ""

        if horz_index >= 0 and horz_index <= 2:
            which_square += "A"
        elif horz_index >= 3 and horz_index <= 5:
            which_square += "B"
        elif horz_index >= 6 and horz_index <= 8:
            which_square += "C"

        if vert_index >= 0 and vert_index <= 2:
            which_square += "0"
        elif vert_index >= 3 and vert_index <= 5:
            which_square += "1"
        elif vert_index >= 6 and vert_index <= 8:
            which_square += "2"

        return which_square

    def checking_for_7(self):

        if "0" not in self.feed:
            return False
        else:
            return True


s = Game()
s.setting_template()
n = 0
with open("temp_file.txt", "w+") as file:
    pass
while True:
    n += 1
    s.feeding()
    checking_table = list(s.feed)
    with open("temp_file.txt", "a+") as file:
        file.write("---"*10)
        file.write(f"Loop nr: {n} ")
        file.write("---"*10)
        file.write("\n")
        for horz_index in range(0, 9):
            for vert_index in range(0, 9):
                file.write(s.feed[horz_index * 9 + vert_index])
            file.write("\n")


    # print(s.feed)
    for horz_index in range(0, 9):
        for vert_index in range(0, 9):
            if s.feed[horz_index * 9 + vert_index] != "0":
                # print(f"wchodze tu a wartosc wynosi {s.feed[horz_index*9+vert_index]}")
                continue
            else:
                s.checking_field(horz_index, vert_index, s.which_square(horz_index, vert_index))

    with open("sudoku.txt", "w+") as file:
        for horz_index in range(0, 9):
            for vert_index in range(0, 9):
                file.write(s.feed[horz_index * 9 + vert_index])
            file.write("\n")
    print(f"pętla nr: {n}")



    if "0" not in s.feed:
        break
    elif checking_table == s.feed:
        break





