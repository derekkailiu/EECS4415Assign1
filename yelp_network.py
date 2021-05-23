
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

def getCatRows(rows, cat, field):
    result = []
    for row in rows:
        if cat in (row[field]):
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

def getTotal(rows, numOfRows, field):
    total = 0
    for row in rows:
        total = total + float(row[field])
    return total

def parseField(rows, field, delimiter):
    
    for row in rows:
        row[field] = row[field].split(delimiter)
       
        

def buildDict(rows, field, category):
    result = defaultdict(int)
    new_result = {}
    for row in rows: #iterates though the dataset by each row
        # print(row[field][0])
        for cat in row[field]:  #iterates through the `categories` field
           
            if cat.upper() != category.upper(): # check if the field is not a restaurant
               
                if result.get(cat) is None:
                    #print("no, key is not in dict")
                    result[cat] = 0
                result[cat] += 1
    for w in sorted(result, key = result.get, reverse = True):
        # print(w, result[w])
        new_result[w] = result[w]
    return new_result
    
import csv
import sys
from collections import defaultdict


def main(argv):
    print(argv)


    filename = "./" + argv[1]

    
    fields = []
    rows = []
    counter = 0
    csv.field_size_limit(100000000)

    # maxInt = sys.maxsize

    # while True:
    # # decrease the maxInt value by factor 10 
    # # as long as the OverflowError occurs.

    #     try:
    #         csv.field_size_limit(maxInt)
    #         break
    #     except OverflowError:
    #         maxInt = int(maxInt/10)


    with open(filename, 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile)
        friendshipList = []
        fields = next(csvreader)

        for row in csvreader:
            
            rows.append([row[0], row[4].strip().split(',')])
            counter = counter + 1
        print(rows[0])
        print("DONE adding" + str(counter))
    
        for r in rows:
            for friend in r[1]:
                if "None" not in r[1]:

                    friendshipList.append([r[0], friend])
      
        
       
        friendshipSet =  set(frozenset(i) for i in friendshipList)
   
        # for fs in friendshipSet:
           
        #     print(str(fs).replace("frozenset({", "").replace("'", "").replace(",", "").replace("})","").replace("  ", " ").strip())
            

    
        with open("./yelp-network_KL.txt", "w") as  w:
            for f in friendshipSet:
                
                print(str(f).replace("frozenset({", "").replace("'", "").replace(",", "").replace("})","").replace("  ", " ").strip(), file=w)

            




main(sys.argv)



    