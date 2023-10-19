import csv
import matplotlib.pyplot as plt


registration_dict={}
with open("../../Data/mca_maharashtra_21042018.csv","r",encoding="ISO-8859-1") as file:
	company_data = csv.DictReader(file)
	for row in company_data:
		date=row["DATE_OF_REGISTRATION"].split("-")
		try:
			if int(date[2]) < 2018:
				if int(date[2]) in registration_dict:
					registration_dict[int(date[2])]+=1
				else:
					registration_dict[int(date[2])]=1
				
		except Exception:
			pass



plt.bar(registration_dict.keys(),registration_dict.values())
plt.title("Number of registrations before year 2018")
plt.xlabel(r"Year $\longrightarrow$")
plt.ylabel(r"Number of registration $\longrightarrow$")
plt.savefig("../Figures/question_2_fig.png",bbox_inches="tight",pad_inches=0.2)
plt.xticks(rotation=270)
plt.show()