from linkedstack import LinkedStack


class Polindrom(LinkedStack):
    """docstring for Polindrom."""
    def __init__(self):
        self.dictionary = LinkedStack()
        self.polindroms = []

    def read_dict(self, filename):
        """reads data from file and saves it to dictionary"""
        with open(filename, encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            if ".lst" in filename:
                for line in lines:
                    self.dictionary.push(line.split()[0])
                # counter = 0
                # with open("try.txt", "w") as t:
                #     while counter < 30:
                #         t.write(lines[counter].split()[0]+"\n")
                #         counter += 1
                        # self.dictionary.push(line.strip())
            else:
                for line in lines:
                    self.dictionary.push(line.strip())

    def process_dict(self):
        """looks for polindroms in processed dict and returns a list of them"""
        while not self.dictionary.isEmpty():
            isPolindrom = True
            curr_word = self.dictionary.pop()
            curr_word_len = len(curr_word)
            if curr_word_len > 1:
                for i in range(curr_word_len//2):
                    if curr_word[i].lower() == curr_word[curr_word_len - i - 1].lower() and isPolindrom:
                        isPolindrom = True
                    else:
                        isPolindrom = False
                if isPolindrom:
                    self.polindroms.append(curr_word)



    def write_dict(self, filename):
        """writes data from polindroms to file"""
        with open(filename, "w", encoding='utf-8', errors='ignore') as f:
            for item in self.polindroms:
                f.write(item)
                f.write("\n")

# Process English dictionary
x = Polindrom()

x.read_dict("words.txt")
x.process_dict()
x.write_dict("palindrome_en.txt")

# Process UKR dictionary
y = Polindrom()

y.read_dict("base.lst")
y.process_dict()
y.write_dict("palindrome_uk.txt")
