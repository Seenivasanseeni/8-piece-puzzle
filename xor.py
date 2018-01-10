import numpy as np
epochs = 20000                                  # Number of iterations
inputNeurons=2
hiddenLayers=2 
outputNeurons = 1
L = .1                                          # learning rate      
 
XOR_ip= np.array([[0,0], [0,1], [1,0], [1,1]])
XOR_op= np.array([[ 0],   [1],   [1],   [0]])
 
def sigmoid (x): return 1/(1 + np.exp(-x))      # activation function
def sigmoid_(x): return x * (1 - x)             # derivative of sigmoid
                                                # weights on layer inputs
input_wh = np.random.uniform(size=(inputNeurons, hiddenLayers))
output_wh = np.random.uniform(size=(hiddenLayers,outputNeurons))
for i in range(epochs):

	H = sigmoid(np.dot(XOR_ip, input_wh))
	Z = np.dot(H,output_wh)                            # output layer, no activation
	Error = XOR_op - Z                                   # how much we missed (error)
	dZ = Error * L                                  # delta Z
	output_wh +=  H.T.dot(dZ)                          # update output layer weights
	dH = dZ.dot(output_wh.T) * sigmoid_(H)             # delta H
	input_wh +=  XOR_ip.T.dot(dH)                          # update hidden layer weights

def activate(z):
	sum_z=sum(z)
	ac_z=[ max(0,round(float(zi/sum_z),0)) for zi in z ]
	return ac_z

print(activate(Z))

    
#http://python3.codes/neural-network-python-part-1-sigmoid-function-gradient-descent-backpropagation/
