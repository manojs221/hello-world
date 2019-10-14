'''Challenge 5 - Self Preservation'''
def question05(input):
	import numpy as np
	noOfattacks=input.pop(0)
	print(noOfattacks)
	input=np.reshape(input, (-1, 2))
	input=input[np.argsort(input[:, 0])]
	print(input[0,1])
	x=[input[0,1]]
	for i in range noOfattacks:
		timeDiff=input[i+1,0]-input[i,0]
		freqDiff=input[i+1,1]-input[i,1]
		if timeDiff==freqDiff:
			x[0]=input[i+1,1]
		else:
			x.append(input[i+1,1])
	
	
	
	
	
	
	
	answer = input
	return answer
print(question05([8, 5, 3, 12, 12, 8, 6, 7, 11, 6, 5, 7, 12, 11, 8, 3, 9]))
