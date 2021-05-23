import csv
import sys

def main(argv):
    # print(argv)

    filename = "./" + argv[1]
    
    fields = []
    rows = []

    csv.field_size_limit(100000000)

    with open(filename, 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile)
        friendshipList = []
        fields = next(csvreader)

        for row in csvreader:
            
            rows.append([row[0], row[4].strip().split(',')]) #add all entries to rows

        for r in rows:
            for friend in r[1]:
                if "None" not in r[1]:

                    friendshipList.append([r[0], friend]) #add all friendships to list
      
        
        friendshipSet =  set(frozenset(i) for i in friendshipList) #convert list to set create bidirectional graph
    
        with open("./yelp-network_KL.txt", "w") as  w:
            for f in friendshipSet:
                
                print(str(f).replace("frozenset({", "").replace("'", "").replace(",", "").replace("})","").replace("  ", " ").strip(), file=w) #converts to string and parse the unnecessary characters, then write to file

main(sys.argv)



    
