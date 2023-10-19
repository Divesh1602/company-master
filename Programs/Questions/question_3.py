import csv
import matplotlib.pyplot as plt


district_data_dict={}
with open("../../Data/mca_maharashtra_21042018.csv","r",encoding="ISO-8859-1") as file1, open("../../Data/dist_zip.csv","r",encoding="ISO-8859-1") as file2:
	company_data=csv.DictReader(file1)
	zip_code_data=csv.DictReader(file2)
	zip_code_list=[]
	zip_code_dict={}
	for row in zip_code_data:
		zip_code_dict[row["Pin Code"]]=row["District"]

	for row in company_data:
		address=row["REGISTERED_OFFICE_ADDRESS"].split()
		date=row["DATE_OF_REGISTRATION"].split("-")
		try:
			if date[2] == '2015':
				zip_code_list.append(address[len(address)-1])
		except Exception:
			pass


	for item in zip_code_list:
		if item in zip_code_dict:
			if zip_code_dict[item] in district_data_dict:
				district_data_dict[zip_code_dict[item]]+=1
			else:
				district_data_dict[zip_code_dict[item]]=1


plt.bar(district_data_dict.keys(),district_data_dict.values())
plt.xticks(rotation=270)
plt.title("District vs Number of registrations")
plt.xlabel(r"District $\longrightarrow$")
plt.ylabel(r"Number of registration $\longrightarrow$")
plt.savefig("../Figures/question_3_fig.png",bbox_inches="tight",pad_inches=0.2)
plt.show()