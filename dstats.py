import csv
import sys

def main():
    # declaration of vars
    numOfBus=0
    avgStars=0
    numOfRestaurants=0
    avgStarsRestaurants=0
    avgNumberOfReviews=0
    avgNumOfReviewsBus=0

    # scan though the file, count numOfBus and Total Stars
    with open(sys.argv[1]) as f:
        reader=csv.reader(f)
        for row in reader:
            city = row[4]
            if city == sys.argv[2]:
                numOfBus+=1
                avgStars+=float(row[9])
                avgNumberOfReviews+=int(row[10])
                if "Restaurant" in row[12]:
                    numOfRestaurants+=1
                    avgStarsRestaurants+=1
                    avgNumOfReviewsBus+=int(row[10])
                    

    # Calculate stats
    avgStars=avgStars/numOfBus;
    avgStarsRestaurants=avgStarsRestaurants/numOfBus
    avgNumberOfReviews=avgNumberOfReviews/numOfBus
    avgNumOfReviewsBus=avgNumOfReviewsBus/numOfRestaurants
    print("numOfBus:{}\navgStars:{}\nnumOfRestaurants:{}\navgNumberOfReviews:{}\navgNumOfReviewsBus:{}".format(numOfBus,avgStars,numOfRestaurants,avgNumberOfReviews,avgNumOfReviewsBus))

#Check Main()
if __name__ == "__main__":
    main()