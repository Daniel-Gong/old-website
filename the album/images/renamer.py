import os

for filename in os.listdir("stimuli"):
	name = filename.split(".")[0]
	name = name.split("_")
	number = str(int(name[-2]))
	if name[-1] == "ori":
		final_name = "Noise/"+number+"Noise.JPG"
	else:
		final_name = "Anti_Noise/"+number+"Anti_Noise.JPG"
	os.rename("stimuli/"+filename, final_name)

	print(final_name)

