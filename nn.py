import numpy as np
import math
class NeuralNetwork:
    input = []
    weights = []
    layers = []
    biases = []
    hiddenlayersize = 4
    output = 0
    def __init__(self, inp, layers):
        self.input = inp
        self.hiddenlayersize = len(inp)
        for i in range(0, layers):
            self.weights.append(np.random.rand(self.hiddenlayersize, 1))
            self.biases.append(np.random.rand(self.hiddenlayersize, 1))
            templayer = []
            for j in range(0, self.hiddenlayersize):
                templayer.append(0)
            self.layers.append(templayer)
    def feedforward(self):
        for i in range(0, len(self.layers)):
            if i == 0:
                self.layers[i] = self.sigmoid(np.dot(self.input, self.weights[0])[0])
            else:
                self.layers[i] = self.sigmoid(np.dot(self.layers[i - 1], self.weights[i])[0])
        return self.layers[len(self.layers) - 1]
    def sigmoid(self, x):
        return 1.0/(1 + math.exp(x * -1.0))
    def sum(arr):
        output = 0
        for i in range(0, len(arr)):
            output += arr[i]
        return output

nn = NeuralNetwork([1, 1, 1, 1], 4)
print(nn.feedforward())

