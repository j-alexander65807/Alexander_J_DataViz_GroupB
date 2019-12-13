import csv

import matplotlib.pyplot as plt


can = []
others = []

categories = []


with open('OlympicsWinter2004-2014.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0



	for row in reader:

		if line_count == 0:

			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:

			if row[4] == "CAN":
				print("canada won")
				can.append(row[4])

			else:
				print("others won")
				others.append(row[4])


			line_count += 1;


# now we can see our medal counts
print(len(can), "medals for Canada")
print(len(others), "medals for Others")



#plot a pie chart

labels = ("Wins", "Loses")
colors = ['red', 'dimgrey']
explode = (0.1, 0.1)
sizes = [len(can), len(others)]

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.f%%', shadow=True, startangle=90)

plt.axis('equal')

#plt.legend(labels, loc=1)
#plt.title("Canadian Medal Wins")
plt.xlabel("2004-2014")
plt.show()