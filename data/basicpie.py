import matplotlib.pyplot as plt

hours = [4, 8, 2]
activities = ["sleep", "work", "play"]
colours = ["gold", "silver", "red"]

plt.pie(hours, labels=activities, colors=colours, startangle=90, autopct='%.1f%%')

plt.show()