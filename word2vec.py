class Word2Vec:
    input = []
    mapping = []
    strip = False
    def __init__(self, input, strip = False):
        self.input = input
        self.strip = strip
        self.generateMap()

    def generateMap(self):
        for i in range(0, len(self.input)):
            word = Word2Vec.process(self.input[i])
            if self.input[i] not in self.mapping and word != "":
                self.mapping.append(word)
        return self.mapping
    def getVector(self, input):
        output = []
        for i in range(0, len(self.mapping)):
            output.append(0)
        splitinput = input.split()
        for s in splitinput:
            word = Word2Vec.process(s)
            if word == "":
                continue
            output[self.mapping.index(word)] += 1
        return output
    
    def process(word):
        word = word.replace('...', "")
        word = word.replace('..', "")
        word = word.replace('!', "")
        word = word.replace('"', "")
        word = word.replace("'", "")
        word = word.replace(',', "")
        word = word.replace('?', "")
        word = word.replace(')', "")
        word = word.replace('(', "")
        return word

