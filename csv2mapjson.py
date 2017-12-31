import csv
import json

import time

#turns the csv into a list of lists [[x, y, z,], [a, b, c]
exampleFile = open('repoffinput.csv')
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
    #website_ch
    subList.append(row[16])


    #once that list for the entry is created, it is added to cleanData
    cleanData.append(subList)


#list to hold the list of dictionaries
jsonList = []

#creates the json
for row in cleanData:
    #this is the dict for the entry
    subDict = {}

    subDict['geometry'] = {'type': 'Point', 'coordinates': row[0]}

    subDict['type'] = 'Feature'

    #this section only adds websites if they exist to the properties entry
    propertiesSubDict = {'orgname_en': row[1], 'orgname_ch': row[2], 'psu_en': row[3], 'originloc': row[4], 'sector': row[5], 'regloc': row[6], 'regdate': row[7], 'actarea': row[8]}

    if '.' in row[9]:
        propertiesSubDict['website_en'] = row[9]
    if '.' in row[10]:
        propertiesSubDict['website_ch'] = row[10]

    subDict['properties'] = propertiesSubDict

    #adds the now completed subDict to jsonList
    jsonList.append(subDict)

#writes the json
with open('jsonholder.json', 'w') as outfile:
    json.dump(jsonList, outfile)


#This is the first part of the input html page
top_half = open('map_top.html', 'r')
#This re-inports the  json as a text file because . . . that's how it works
middle = open('jsonholder.json', 'r')
#This is the last part of the input html page
bottom_half = open('map_bottom.html', 'r')

#sets up the regular output
output_page = open('index_RO_table.html', 'w')
##sets up the archive output
timestamp = time.strftime("%Y%m%d")
output_page_archive_filename = "index_RO_table" + timestamp + ".html"
archive_page = open(output_page_archive_filename, 'w')


#writes the html to the new page
for item in top_half:
    output_page.write(item)
    archive_page.write(item)
#writes the json
for item in middle:
    output_page.write(item)
    archive_page.write(item)
#writes the end
for item in bottom_half:
    output_page.write(item)
    archive_page.write(item)

top_half.close()
middle.close()
bottom_half.close()
output_page.close()
archive_page.close()
