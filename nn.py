import numpy as np
import math
class NeuralNetwork:
    input = []
    weights = []
    layers = []
    biases = []
    y = []
    hiddenlayersize = 4
    output = 0
    dweights = []
    def __init__(self, inp, layers, training_output):
        self.input = inp
        self.y = training_output
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
                tempx = np.dot(self.input, self.weights[0])[0]
                #print("tempx: " + str(tempx))
                self.layers[i] = self.sigmoid(tempx)
            else:
                tempx = np.dot(self.layers[i - 1], self.weights[i])[0]
                #print("tempx for " + str(i) + ": " + str(tempx))
                self.layers[i] = self.sigmoid(tempx)
            print("self.layers[" + str(i) + "]: " + str(self.layers[i]))
        self.output = self.layers[len(self.layers) - 1]
        print("self.output: " + str(self.output))
        return self.output
    def backprop(self):
        for i in range(0, len(self.weights)):
            dweight = np.dot(self.layers[i], (2 * (self.y - self.output) * self.sigmoid_derivative(self.output)))
            print("dweight: " + str(dweight))
            self.weights += dweight
        print("weights: " + str(self.weights))
        return self.weights

    def sigmoid_derivative(self, x):
        return x * (1.0 - x)

    def sigmoid(self, x, derivative=False):
        print("x: " + str(x))
        sigm = 1.0 / (1.0 + np.exp(x * -1.0))
        return sigm
    def sum(arr):
        output = 0
        for i in range(0, len(arr)):
            output += arr[i]
        return output

nn = NeuralNetwork([[0.0]], 3, [1])
#nn.feedforward()
for i in range(0, 100):
    nn.feedforward()
    nn.backprop()

# print(nn.feedforward())
#print(nn.backprop())

