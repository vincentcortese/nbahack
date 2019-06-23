class Word2Vec:
    input = []
    def __init__(self, input):
        self.input = input
    def getVector(self):
        output_arr = []
        for i in range(0, len(self.input)):
            if self.input[i] not in output_arr:
                output_arr.append(self.input[i])
        return output_arr