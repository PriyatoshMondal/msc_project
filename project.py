import json as js

# Array of file names
file_names = ["1kf1_metbp.json", "1n32_metbp.json"]


def searchItem(data, accn, metal):
	bases = []
	if (accn == data.get("accn")):
		for elem in data["metbp_sites"]:
			if (elem["metal"].get("name") == metal):
				bases.append(elem)
	else:
		pass

	print(bases)


def driverFun(file_names):
	accn = input("Enter accn value: ")
	metal = input("Enter metal name: ")
	fname = ""
	try:
		for item in file_names:
			fname = item
			file = open(item)
			data = js.load(file)
			searchItem(data, accn, metal)
	except:
		print(f"{fname} does not exist")


driverFun(file_names)
