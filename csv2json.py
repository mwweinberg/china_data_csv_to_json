import csv
import pprint

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
    #breaks up the string value, turns it into numbers, and adds to list
    a,b = row[0].split(", ")
    locList = [float(a), float(b)]
    subList.append(locList)

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
    #website_en
    subList.append(row[15])


    #once that list for the entry is created, it is added to cleanData
    cleanData.append(subList)

#print(cleanData)
#print(cleanData[1])

#list to hold the list of dictionaries
jsonList = []


#print(cleanData[0])

for row in cleanData:
    #this is the dict for the entry
    subDict = {}

    subDict['geometry'] = {'type': 'Point', 'coordinates': row[0]}

    subDict['type'] = 'Feature'

    subDict['properties'] = {'orgname_en': row[1], 'orgname_ch': row[2], 'psu_en': row[3], 'originloc': row[4], 'sector': row[5], 'regloc': row[6], 'regdate': row[7], 'actarea': row[8], 'website_en': row[9]}

    #adds the now completed subDict to jsonList
    jsonList.append(subDict)

pprint.pprint(jsonList)
