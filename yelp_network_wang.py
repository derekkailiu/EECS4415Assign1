# Name: Jianxian Wang
# Student ID: 217557489
# Name: Kai Liu
# Student ID: 216624835

import csv
import argparse
# import sys


# Set csv field size limit to maximum
# csv.field_size_limit(sys.maxsize)


def main():
    # vars
    friends = []
    result = []

    # read args
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    # Scan file
    with open(args.filename, encoding='utf8') as f, open("yelp-network.txt", "w") as w: #opens a csv file from argument, also opens a file to write output
        reader_source = csv.reader(f)
        next(reader_source)  #Skip header
        for row in reader_source:
            if 'None' not in row[4]:
                friends=[x.strip() for x in row[4].split(',')] #parses values in the 'friends' column
                for str in friends:
                    str1 = row[0]+' '+ str
                    str2 = str + ' '+row[0]
                    if str1 not in result and str2 not in result: #checks is duplicate exists in list
                        result.append(str1) #append string to list

        #print result to file
        for str in result:
            print(str,file=w)

# check main()
if __name__ == "__main__":
    main()