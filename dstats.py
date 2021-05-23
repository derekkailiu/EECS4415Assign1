
def averageStars(rows, numOfRows):
    total = 0
    avg = 0
    for row in rows:
        # print(rows[9])
        total = total + float(row[9])
    avg = total / numOfRows
    return avg

def getRestaurants(rows):
    category = "RESTAURANT"
    result = []
    for row in rows:
        if category in (row[12]).upper():
            result.append(row)
    return result

def restaurantCount(rows):
    category = "RESTAURANT"
    result = 0
    for row in rows:
        if category in (row[12]).upper():
            result = result + 1
    return result

def getRowCount(rows):
    result = 0
    for row in rows:
        result = result + 1
    return result

def getAverage(rows, numOfRows, field):
    total = 0
    for row in rows:
        total = total + float(row[field])
    return total / numOfRows

import csv
import sys

def main(argv):
    print(argv)


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

    file = open('./sample.csv', 'w+', encoding = 'utf8', newline = '')
    with file:
        writer = csv.writer(file)
        
        with open(filename, 'r', encoding='utf8') as csvfile:
            csvreader = csv.reader(csvfile)

            fields = next(csvreader)

            for row in csvreader:
                if inputCity.upper() in row[4].upper():
        
                    rows.append(row)
                    counter = counter + 1
            
            
        # writer.writerows(rows)
    print("numOfBus:%d"%counter)
    print("avgStars:" + inputCity + " is :%f"%averageStars(rows, counter))
    print("numOfRestaurants:%d"%restaurantCount(rows))
    print("avgStarsRestaurants:%f"%averageStars(getRestaurants(rows),getRowCount(getRestaurants(rows))) )
    print("avgNumOfReviews:%f"%getAverage(rows, counter, f_review_count))
    print("avgNumOfReviewsBus:%f"%getAverage(getRestaurants(rows), getRowCount(getRestaurants(rows)), f_review_count))
main(sys.argv)



    