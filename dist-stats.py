# Name: Jianxian Wang
# Student ID: 217557489
# Name: Kai Liu
# Student ID: 216624835

def getCatRows(rows, cat, field): #returns all rows that contain specified category
    result = []
    for row in rows:
        if cat in (row[field]):
            result.append(row)
    return result

def getRowCount(rows): #returns number of rows
    result = 0
    for row in rows:
        result = result + 1
    return result

def getAverage(rows, numOfRows, field): #returns average of values in row[field]
    total = 0
    for row in rows:
        total = total + float(row[field])
    return total / numOfRows

def getTotal(rows, numOfRows, field): #returns total values of row[field]
    total = 0
    for row in rows:
        total = total + float(row[field])
    return total

def parseField(rows, field, delimiter): #splits categories from a string to a list, based on ';' as delimiter
    
    for row in rows:
        row[field] = row[field].split(delimiter)
       
        

def buildDict(rows, field, category): # build a dictionary with category as key, and numberof occruences as value
    result = defaultdict(int)
    new_result = {}
    for row in rows: #iterates though the dataset by each row
        for cat in row[field]:  #iterates through the `categories` field
            if cat.upper() != category.upper(): # check if the field is not a restaurant
                if result.get(cat) is None:
                    
                    result[cat] = 0
                result[cat] += 1

    for w in sorted(result, key = result.get, reverse = True):
        
        new_result[w] = result[w]
    return new_result
    
import csv
import sys
from collections import defaultdict
import matplotlib.pyplot
import numpy


def main(argv):

    filename = "./" + argv[1]
    inputCity = argv[2]
    fields = []
    rows = []
    counter = 0
    f_business = 0
    f_name = 1
    f_neighborhood = 2
    f_address = 3
    f_city = 4
    f_state = 5
    f_postalCode = 6
    f_latitude = 7
    f_longitude = 8
    f_stars = 9
    f_review_count = 10
    f_isOpen = 11
    f_categories = 12

    i = 0
    top10Cat = []
    top10Rest = []

  
        
    with open(filename, 'r', encoding='utf8') as csvfile: #opens csv file from argument
        csvreader = csv.reader(csvfile)

        fields = next(csvreader) #skip header

        for row in csvreader:
            if inputCity.upper() in row[4].upper():
    
                rows.append(row) #add each row to a list
         

    restaurants = getCatRows(rows, "Restaurants", f_categories) #include only rows that has 'restaurant' in its category
    parseField(rows, f_categories, ";") #converts category from a string to a list with ';' as delimiter
    dict = buildDict(restaurants, f_categories, "restaurants") #build a dictionary with category as key and frequency as value
  
    with open('categories.txt', 'w', encoding='utf8') as w, open('reviews_and_avg_stars.txt', 'w', encoding='utf8') as w2: #opens and writes output to two files
    
        for d in dict: #outputs category and number of business from most to fewest
            
            catRows = getCatRows(rows, d, f_categories)
            totalReviews = getTotal(catRows, getRowCount(catRows), f_review_count)
            avgStars = getAverage(catRows, getRowCount(catRows), f_stars)

            print(d + ":" + str(dict[d])) #std output
            w.write(d + ":" + str(dict[d]) + '\n') #write to file

            print(d + ":" + str(int(totalReviews)) + ":" + str(avgStars)) #std output
            w2.write(d + ":" + str(int(totalReviews)) + ":" + str(avgStars) + '\n') #write to file
            if i < 10 :
        
                top10Cat.append(d) #add top ten categories to list
                top10Rest.append(dict[d]) #add number of business of the top ten categories to list
                
            i += 1
        
  
    
    # Generate Graph
   
    objects = (top10Cat)
 
    y_pos = numpy.arange(len(objects))

    matplotlib.pyplot.bar(y_pos, top10Rest, align='center', alpha=0.5)
    matplotlib.pyplot.xticks(y_pos, objects)
    matplotlib.pyplot.ylabel('#Restaurants')
    matplotlib.pyplot.title('restaurantCategoryDist')
    matplotlib.pyplot.show()

main(sys.argv)



    