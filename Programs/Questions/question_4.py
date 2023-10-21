"""
Plot a Grouped Bar Plot by aggregating registration counts over ...

Year of registration
Principal Business Activity

"""
import csv
import matplotlib.pyplot as plt


def execute():
    """This function is calculating the data needed to plot the graph"""
    registration_dict = {}
    with open(
        "../../Data/mca_maharashtra_21042018.csv", "r", encoding="ISO-8859-1"
    ) as file:
        company_data = csv.DictReader(file)
        for row in company_data:
            date = row["DATE_OF_REGISTRATION"].split("-")
            try:
                if int(date[2]) < 2018:
                    if int(date[2]) in registration_dict:
                        if row[
                            "PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"
                        ] in registration_dict[int(date[2])]:
                            registration_dict[
                                int(date[2])
                            ][row[
                                "PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"
                            ]] += 1
                        else:
                            registration_dict[
                                int(date[2])
                            ][row[
                                "PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"
                            ]] = 1
                    else:
                        registration_dict[int(date[2])] = {}
                        registration_dict[
                            int(date[2])
                        ][row["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]] = 1
            except ValueError:
                pass
            except IndexError:
                pass
    return registration_dict


def transform(registration_dict):
    """This function is extracting the value as required in matplotlib"""
    sorted_registration_dict = dict(
                                    sorted(
                                        registration_dict.items(),
                                        key=lambda item: max(item[1].values()),
                                        reverse=True
                                    )
                                )
    registration_year = list(sorted_registration_dict.keys())[:5]
    activity_list = []
    count_of_activity = []
    for i in enumerate(registration_year):
        activity_list.append(
                list(
                    sorted_registration_dict[registration_year[i[0]]].keys()
                )[:5]
            )
        count_of_activity.append(
                list(
                    sorted_registration_dict[registration_year[i[0]]].values()
                )[:5]
            )
    activity_list = activity_list[0]
    plot(registration_year, count_of_activity, activity_list)


def plot(registration_year, count_of_activity, activity_list):
    """This function is ploting the graph with the given data"""
    colors = ['red', 'green', 'blue', 'orange', 'purple']
    _, axis = plt.subplots(figsize=(10, 10))
    for i in range(5):
        axis.bar(0, 0, label=activity_list[i], color=colors[i])
    bar_offset = 0
    bar_width = 0.1
    for i in enumerate(registration_year):
        for j in enumerate(count_of_activity[i[0]]):
            axis.bar(
                bar_offset,
                count_of_activity[i[0]][j[0]],
                width=bar_width,
                color=colors[j[0]]
            )
            bar_offset += bar_width
        bar_offset += bar_width*2
    bar_positions = [0.3, 1, 1.7, 2.4, 3.1]
    axis.set_title(
        "Registration counts over year of"
        " registration principal Business Activity"
    )
    axis.set_xlabel(r"Years $\longrightarrow$")
    axis.set_ylabel(r"Count $\longrightarrow$")
    axis.set_xticks(bar_positions, registration_year)
    plt.legend(loc=(0, 0.80))
    plt.savefig(
        "../Figures/question_4_fig.png", bbox_inches="tight", pad_inches=0.2
    )
    plt.show()


if __name__ == "__main__":
    data_dict = execute()
    transform(data_dict)
