import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []

with open("data/OlympicsData.csv") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this the first row")
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print("won gold")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("won silver")
				silvers.append(row[7])
			else:
				print("won bronze")
				bronzes.append(row[7])
			print(line_count)
			line_count += 1

print(len(golds))
print(len(silvers))
print(len(bronzes))

				
labels = ["Gold", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0.1, 0.1)	
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.f%%', shadow=True, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("hockey")
plt.xlabel("medal count")

plt.show()		