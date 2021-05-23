import csv
import argparse
import sys


csv.field_size_limit(sys.maxsize)


def main():
    # vars
    friends = []
    result = []

    # read args
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    # Scan file
    with open(args.filename) as f, open("yelp-network.txt", "w") as w:
        reader_source = csv.reader(f)
        #Skip header
        next(reader_source)
        for row in reader_source:
            if 'None' not in row[4]:
                friends=[x.strip() for x in row[4].split(',')]
                for str in friends:
                    str1 = row[0]+' '+ str
                    str2 = str + ' '+row[0]
                    if str1 not in result and str2 not in result:
                        result.append(str1)

        #print result to file
        for str in result:
            print(str,file=w)

# check main()
if __name__ == "__main__":
    main()
