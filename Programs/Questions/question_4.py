import csv
import matplotlib.pyplot as plt

registration_dict = {}
buissness_activity_dict = {}
with open("../../Data/mca_maharashtra_21042018.csv", "r", encoding = "ISO-8859-1") as file:
	company_data=csv.DictReader(file)
	for row in company_data:
		date=row["DATE_OF_REGISTRATION"].split("-")
		try:
			if int(date[2]) < 2018:
				if date[2] in registration_dict:
					registration_dict[date[2]] += 1
				else:
					registration_dict[date[2]] = 1
			if row["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"] in buissness_activity_dict:
				buissness_activity_dict[row["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]] += 1
			else:
				buissness_activity_dict[row["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]] = 1
		except Exception:
			pass



sorted_registration_dict = dict(sorted(registration_dict.items(), key = lambda item: item[1], reverse = True))
sorted_buissness_activity_dict = dict(sorted(buissness_activity_dict.items(), key = lambda item: item[1], reverse = True))
registration_year = list(sorted_registration_dict.keys())[:5]
registration_count = list(sorted_registration_dict.values())[:5]

buissness_activity = list(sorted_buissness_activity_dict.keys())[:5]
buissness_activity_count = list(sorted_buissness_activity_dict.values())[:5]
start_registration = [0.825, 1.825, 2.825, 3.825, 4.825]
start_buissness = [1.175, 2.175, 3.175, 4.175, 5.175]
plt.bar(start_registration, registration_count, 0.35, label = "group1")
plt.bar(start_buissness, buissness_activity_count, 0.35, label = "group2")
x_labels = registration_year + buissness_activity
x_ticks = [0.825, 1.825, 2.825, 3.825, 4.825, 1.175, 2.175, 3.175, 4.175, 5.175]
plt.xticks(x_ticks, x_labels, rotation = 270, ha = 'right')
plt.ylabel(r"count $\longrightarrow$")
plt.xlabel(r"Registration year, Buissness activity $\longrightarrow$")
plt.title("Aggregating registration counts")
plt.savefig("../Figures/question_4_fig.png", bbox_inches = "tight", pad_inches = 0.2)
plt.show()
