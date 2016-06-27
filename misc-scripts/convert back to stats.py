import csv
import itertools

with open('training set.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    elements = list(reader)

vals = []
temp_inputs = []
inputs = []
outputs = []
counter = 0

all_data = list(itertools.chain.from_iterable(elements))
for item in all_data:
    if counter < 20:
        temp_inputs.append(float(item))
        counter = counter + 1
    else:
        inputs.append(temp_inputs)
        outputs.append(float(item))
        temp_inputs = []
        counter = 0

stats = []

counter = 0
for x in range(0, len(inputs)):
    counter = 0
    for y in inputs[x]:
        if counter == 6:
            # temp = float(y) * 12.7 + 8
            temp = y
            stats.append(temp)
        if counter == 16:
            # temp = y * 12.7 + 8
            temp = y
            stats.append(temp)
        counter = counter + 1
    counter = 0
    for y in inputs[x]:
        if counter == 2:
            # temp = y * 7 + 2.9
            temp = y
            stats.append(temp)
        if counter == 12:
            # temp = y * 7 + 2.9
            temp =y
            stats.append(temp)
        counter = counter + 1
    counter = 0
    for y in inputs[x]:
        if counter == 4:
            # temp = y * 5.4 + 1.3
            temp = y
            stats.append(temp)
        if counter == 14:
            # temp = y * 5.4 + 1.3
            temp = y
            stats.append(temp)
        counter = counter + 1
    counter = 0
    for y in inputs[x]:
        if counter == 0:
            # temp = float(y) * 9 + 15.2
            temp = y
            stats.append(temp)
        if counter == 10:
            # temp = y * 9 + 15.2
            temp = y
            stats.append(temp)
        counter = counter + 1
    counter = 0
    for y in inputs[x]:
        if counter == 8:
            # temp = y * .176 + .415
            temp = y
            stats.append(temp)
        if counter == 18:
            # temp = y * .176 + .415
            temp = y
            stats.append(temp)
        counter = counter + 1
    stats.append(outputs[x])

print stats


with open("converted data.csv", "wb") as f:
    writer = csv.writer(f)
    for x in range(0, len(stats)):
        print stats[x]
        writer.writerow([stats[x]])
