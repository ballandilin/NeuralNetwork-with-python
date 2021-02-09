

####### single neuron with 3 inputs #########

inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

output = (inputs[0]*weights[0] +
		  inputs[1]*weights[1] +
		  inputs[2]*weights[2] + bias)

print(f" 1# Neuron output : {output}")




####### single neuron with 4 inputs #########

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

output = (inputs[0]*weights[0] +
		  inputs[1]*weights[1] +
		  inputs[2]*weights[2] + 
		  inputs[3]*weights[3] + bias)

print(f" 2# Neuron output : {output}")