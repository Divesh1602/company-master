import csv
import matplotlib.pyplot as plt


capital_list = []
with open("../../Data/mca_maharashtra_21042018.csv",'r',encoding="ISO-8859-1") as file:
	company_data=csv.DictReader(file)
	for row in company_data:
		try:
			capital_list.append(int(row["AUTHORIZED_CAP"]))
		except Exception:
			pass    

    
plt.figure(figsize=(20,5))
labels = ['<=10L','10L to 30L','30L to 1Cr','1Cr to 3Cr','3Cr to 5Cr','5Cr to 10Cr','> 10Cr']
bins = [0,1000000,3000000,10000000,30000000,50000000,100000000]
plt.hist(capital_list,bins=bins,rwidth=0.95)
plt.xticks(bins, labels,rotation=270)  # Set x-axis labels
plt.title("Histogram of Authorized Capital")
plt.xlabel(r"AUTHORIZED_CAP $\longrightarrow$")
plt.ylabel(r"FREQUENCY $\longrightarrow$")
plt.savefig("../Figures/question_1_fig.png",bbox_inches='tight',pad_inches=0.1)
plt.show()
