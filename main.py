import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib import dates as mpl_dates
from datetime import datetime

spent = []
day = []
total = 0
data = 'FundsTransfer.csv'

with open(data, 'r', newline='') as d:
    csv_reader = csv.reader(d)
    next(csv_reader)
    for row in csv_reader:
        day.append(mpl_dates.date2num(datetime.strptime(row[4], '%m/%d/%Y')))
        spent.append(float(row[7].strip('$')))
        total += float(row[7].strip('$'))

#Formatting

print("Your average transaction amount was - ${:,.2f}".format(np.mean(spent)))
print("Your total spent was - ${:,.2f}".format(total))

ax = plt.gca()
ax.xaxis.set_minor_locator(matplotlib.dates.MonthLocator([4, 10]))
ax.xaxis.set_minor_formatter(matplotlib.dates.DateFormatter('%b'))
ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y'))

plt.title("Account Spending over Time")
plt.xlabel("Date")
plt.ylabel("Amount spent ($USD)")
plt.plot(day, spent, color='green')
plt.show()
