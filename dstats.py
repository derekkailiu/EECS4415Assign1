# Name: Jianxian Wang
# Student ID: 217557489
# Name: Kai Liu
# Student ID: 216624835


def getRestaurants(rows): #returns rows that only contains restaurants in its categories
    category = "RESTAURANT"
    result = []
    for row in rows:
        if category in (row[12]).upper():
            result.append(row)
    return result

def restaurantCount(rows): #returns count of restaurants
    category = "RESTAURANT"
    result = 0
    for row in rows:
        if category in (row[12]).upper():
            result = result + 1
    return result

def getRowCount(rows): #returns number of rows
    result = 0
    for row in rows:
        result = result + 1
    return result

def getAverage(rows, numOfRows, field): #retruns average of values in 'field'
    total = 0
    for row in rows:
        total = total + float(row[field])
    return total / numOfRows

import csv
import sys

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

    with open(filename, 'r', encoding='utf8') as csvfile: #opens the .csv file
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)

        for row in csvreader:
            if inputCity.upper() in row[4].upper(): #check if row contains city specified in argument
    
                rows.append(row) 
                counter = counter + 1
            
    #std output
    print("numOfBus:%d"%counter)
    print("avgStars:%f"%getAverage(rows, counter, f_stars))
    print("numOfRestaurants:%d"%restaurantCount(rows))
    print("avgStarsRestaurants:%f"%getAverage(getRestaurants(rows),getRowCount(getRestaurants(rows)), f_stars))
    print("avgNumOfReviews:%f"%getAverage(rows, counter, f_review_count))
    print("avgNumOfReviewsBus:%f"%getAverage(getRestaurants(rows), getRowCount(getRestaurants(rows)), f_review_count))
main(sys.argv)



    