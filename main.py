import fileparser
import nn

parsedOutput = fileparser.FileParser.parseFile("data/business/training_set.csv")
network = nn.NeuralNetwork(parsedOutput[0], 3, parsedOutput[1])
for i in range(0, 5):
	network.feedforward()
print(parsedOutput[1])
print(network.getOutput())
