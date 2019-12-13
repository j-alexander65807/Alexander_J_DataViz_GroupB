import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []
#bins = [1924,1950,1975,2000,2025]
colors = ['gold', 'silver', 'darkgoldenrod']
labels = ['Gold', 'Silver', 'Bronze']

categories = [] # first row -> not data

with open('OlympicsWinterCan.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count == 0:
			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				print("won a gold medal")
				golds.append(row[0])
			elif row[7] == "Silver":
				print("won a silver medal")
				silvers.append(row[0])
			else:
				print("won a bronze medal")
				bronzes.append(row[0])

			print(line_count)
			line_count += 1
plt.figure()

#I had a real hard time getting stacked histograms to work. like a real hard time. Normalization issues?
plt.hist(golds, density=True,  edgecolor='black', color="gold")


#plt.legend(labels, loc=1)
plt.xlabel('years')
plt.ylabel('Number of Gold Medals')
plt.title('Canadian Gold Medals')
plt.show()