import numpy as np

output = ""

mu = 0
sigma = 0.05

f = open("./model_bunny.txt","r")
lines = f.readlines() 
for i in range(len(lines)):
	line = lines[i]
	val = line.split()
	if(len(val) == 3):
		if(np.random.uniform(0,1) > 0.05):
			x = float(val[0]) + np.random.normal(mu, sigma)
			y = float(val[1]) + np.random.normal(mu, sigma)
			z = float(val[2]) + np.random.normal(mu, sigma)


			x = round(x,6)
			y = round(y,6)
			z = round(z,6)


			output += str(x) + " " + str(y) + " " + str(z) + "\n"

text_file = open("generated_bunny.txt", "w")
text_file.write(output)
text_file.close()