import csv
import itertools

with open('output.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    elements = list(reader)

temp_inputs = []
inputs = []
outputs = []
counter = 0

all_data = list(itertools.chain.from_iterable(elements))
for item in all_data:
    inputs.append(item)
    # if counter < 10:
    #     temp_inputs.append(float(item))
    #     counter = counter + 1
    # else:
    #     inputs.append(temp_inputs)
    #     outputs.append(float(item))
    #     temp_inputs = []
    #     counter = 0

outputs = []
counter == 0
for x in inputs:
    if counter == 0:
        x = (float(x) - 7.5) / (17.7 - 7.5)
        outputs.append(x)
    if counter == 1:
        x = (float(x) - 7.5) / (17.7 - 7.5)
        outputs.append(x)
    if counter == 2:
        x = (float(x) - 3.2) / (10.3 - 3.2)
        outputs.append(x)
    if counter == 3:
        x = (float(x) - 3.2) / (10.3 - 3.2)
        outputs.append(x)
    if counter == 4:
        x = (float(x) - 1.15) / (7.25 - 1.15)
        outputs.append(x)
    if counter == 5:
        x = (float(x) - 1.15) / (7.25 - 1.15)
        outputs.append(x)
    if counter == 6:
        x = (float(x) - 23.85) / (13.85 - 23.85)
        outputs.append(x)
    if counter == 7:
        x = (float(x) - 23.85) / (13.85 - 23.85)
        outputs.append(x)
    if counter == 8:
        x = (float(x) - .405) / (.587 - .405)
        outputs.append(x)
    if counter == 9:
        x = (float(x) - .405) / (.587 - .405)
        outputs.append(x)
    counter = counter + 1
    if counter == 11:
        outputs.append(x)
        counter = 0

with open("converted stats.csv", "wb") as f:
    writer = csv.writer(f)
    for x in range(0, len(outputs)):
        writer.writerow([outputs[x]])
