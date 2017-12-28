import csv

#turns the csv into a list of lists [[x, y, z,], [a, b, c]
exampleFile = open('input.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


#variable to hold the data we care about
cleanData = []

#removes header row
del exampleData[0]

#pull the data you care about into a new list. Each entry is a list in the list 

for row in exampleData:
    #this is the list of the elements for the individual entry
    subList = []

    #this goes through an plucks out the data that matters
    #lat/long
    subList.append(row[0])

    #clean up name and add
    if 'The' in row[4]:
        fullName = 'The ' + row[5]
    else:
        fullName = row[5]
    subList.append(fullName)

    #chinese name
    subList.append(row[6])
    #psu_en
    subList.append(row[7])
    #origin_loc
    subList.append(row[9])
    #sec
    subList.append(row[10])
    #regloc
    subList.append(row[12])
    #regdate
    subList.append(row[13])
    #actarea
    subList.append(row[14])

    #once that list for the entry is created, it is added to cleanData
    cleanData.append(subList)


print(cleanData)
