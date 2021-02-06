import json
import matplotlib.pyplot as plt
import csv
with open("wikiData.json") as f:
    data = json.load(f)

time = []
scheduled = []
crawled = []

for entry in data:
    time.append(entry["time"])
    scheduled.append(entry["num_scheduled"])
    crawled.append(entry["num_scraped"])

time = [t-time[0] for t in time]
rows = zip(time, scheduled, crawled)

wtr = csv.writer(open ('out.csv', 'w'), delimiter=',', lineterminator='\n')

wtr.writerow(["Time", "Scheduled", "Crawled"])
for x in rows: wtr.writerow (x)


plt.scatter(time, scheduled, label="Scheduled")

plt.scatter(time, crawled, label="Crawled")
plt.ylabel("Number of Web Pages")
plt.xlabel("Time (Seconds)")
plt.legend()
plt.show()
