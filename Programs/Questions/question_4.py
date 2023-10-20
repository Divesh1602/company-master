import csv
import matplotlib.pyplot as plt

registration_dict = {}

with open("../../Data/mca_maharashtra_21042018.csv", "r", encoding = "ISO-8859-1") as file:
	company_data=csv.DictReader(file)
	for row in company_data:
		date=row["DATE_OF_REGISTRATION"].split("-")
		try:

			if int(date[2]) < 2018:
				if int(date[2]) in registration_dict:
					if row["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"] in registration_dict[int(date[2])]:
						registration_dict[int(date[2])][row["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]]+=1
					else:
						registration_dict[int(date[2])][row["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]]=1
				else:
					registration_dict[int(date[2])]={}
					registration_dict[int(date[2])][row["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]]=1
		except Exception:
			pass

# Sort the dictionary by the 'value' key in the inner dictionaries
sorted_registration_dict = dict(sorted(registration_dict.items(), key=lambda item: max(item[1].values()),reverse=True))




registration_year = list(sorted_registration_dict.keys())[:5]
activity_list=[]
count_of_activity=[]
for i in range(len(registration_year)):
	activity_list.append(list(sorted_registration_dict[registration_year[i]].keys())[:5])
	count_of_activity.append(list(sorted_registration_dict[registration_year[i]].values())[:5])

activity_list=activity_list[0]
colors = ['red', 'green', 'blue', 'orange', 'purple']

fig, ax = plt.subplots(figsize=(10,10))
for i in range(5):
	ax.bar(0,0,label=activity_list[i],color=colors[i])
bar_offset=0
bar_width=0.1
for i in range(len(registration_year)):
    for j in range(len(count_of_activity[i])):
        bar = count_of_activity[i][j]
        ax.bar(bar_offset, bar, width=bar_width,color=colors[j])
        bar_offset+=bar_width
    bar_offset+=bar_width*2
bar_positions=[0.3,1,1.7,2.4,3.1]

ax.set_title("Registration counts over year of registration principal Business Activity")
ax.set_xlabel(r"Years $\longrightarrow$")
ax.set_ylabel(r"Count $\longrightarrow$")
ax.set_xticks(bar_positions,registration_year)
plt.legend(loc=(0,0.80))
plt.savefig("../Figures/question_4_fig.png",bbox_inches="tight",pad_inches=0.2)
plt.show()