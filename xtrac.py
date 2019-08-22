import json

with open('data.json') as data_file:
	data = json.load(data_file)

for key in data:
	if key == "sentences":
		#print(data["sentences"])
		data_list = data["sentences"][6]
		#print(data_list)
		
		for ref_key in data_list:
			if ref_key == "dependencies":
				print(data_list["dependencies"])