import csv
import argparse
from os import read
import matplotlib.pyplot
import numpy


def main():
    # vars
    categories = []
    numbers = []
    reviews = []
    stars = []

    categoriesList = []
    starList = []
    reviewList = []

    tokenList = []

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("city")
    args = parser.parse_args()

    with open(args.filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            categoriesList.append(row[12])
            starList.append(row[9])
            reviewList.append(row[10])
        # tokenize categories
        for str in categoriesList:
            tokenList.append(str.split(';'))
        # convert starList's datatype to float
        for i in range(len(starList)):
            starList[i] = float(starList[i])
        # convert reviewList's datatype to int
        for i in range(len(reviewList)):
            reviewList[i] = int(reviewList[i])
        # Scan though tokens
        for listing in tokenList:
            if 'Restaurants' in listing:
                tokenIndex = tokenList.index(listing)
                for str in listing:
                    if str != 'Restaurants':
                        if str in categories:
                            strIndex = categories.index(str)
                            numbers[strIndex] += 1
                            reviews[strIndex] += reviewList[tokenIndex]
                            stars[strIndex] += starList[tokenIndex]
                        else:
                            categories.append(str)
                            numbers.append(1)
                            reviews.append(reviewList[tokenIndex])
                            stars.append(starList[tokenIndex])

    # Caculate avg stars
    for i in range(len(stars)):
        stars[i] = stars[i]/numbers[i]

    # Sort lists
    zipList = zip(numbers, categories, reviews, stars)
    zipListReview = zip(numbers, categories, reviews, stars)

    sortedZippedList = sorted(zipList, reverse=True)

    sortedZippedListReview = sorted(zipListReview,reverse=True,key=lambda item:item[2])

    # print to file
    with open('p2_output.txt', 'w') as w:
        print('category:#restaurants',file=w)
        for i in sortedZippedList:
            print('{}:{}'.format(i[1], i[0]),file=w)
        print('\n',file=w)
        print('category:#reviews:avg_stars\n',file=w)
        for i in sortedZippedListReview:
            print('{}:{}:{:.2f}'.format(i[1], i[2], i[3]),file=w)

    # Generate Graph
    top10Cat = []
    top10Num = []

    for i in range(10):
        top10Cat.append(sortedZippedList[i][1])
        top10Num.append(sortedZippedList[i][0])

    objects = (top10Cat)
    y_pos = numpy.arange(len(objects))

    matplotlib.pyplot.bar(y_pos, top10Num, align='center', alpha=0.5)
    matplotlib.pyplot.xticks(y_pos, objects)
    matplotlib.pyplot.ylabel('#Restaurants')
    matplotlib.pyplot.title('restaurantCategoryDist')
    matplotlib.pyplot.show()


# Check main()
if __name__ == "__main__":
    main()