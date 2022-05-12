
csvfile = open('import_southside.csv', 'r').readlines()
filename = 1

for i in range(len(csvfile)):
    if i % 500 == 0:
        open(str(filename) + '.csv', 'w+').writelines(csvfile[i: i + 500])
        filename += 1
