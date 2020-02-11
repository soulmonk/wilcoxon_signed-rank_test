import csv


def save_data(data, headers, path):
    with open(path, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(headers)

        for row in data:
            spamwriter.writerow(row)
