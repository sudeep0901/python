# download cornells movie review data
import os
from nltk.corpus import sentiwordnet as swn
from string import punctuation
from nltk.corpus import stopwords
if os.name == 'nt':
    positiveReviewFileName = r"D:\github\python\src\NLP\sentiment analysis\rt-polaritydata\rt-polarity.pos"
    negitiveReviewFileName = r"D:\github\python\src\NLP\sentiment analysis\rt-polaritydata\rt-polarity.neg"
    

with open(positiveReviewFileName, 'r') as f:
    positiveReviews = f.readlines()
with open(negitiveReviewFileName, 'r') as f:
    negativeReviews = f.readlines()

print(swn.senti_synsets("dog"))
for synset in swn.senti_synsets("dog"):
    print(synset)
    

testTrainingSplitIndex = 2500
# split data in training and testing set
testPositiveReviews = negativeReviews[testTrainingSplitIndex + 1:]
testNegativeReviews = positiveReviews[testTrainingSplitIndex + 1:]
trainingPositiveReviews = negativeReviews[:testTrainingSplitIndex]
trainingNegativeReviews = positiveReviews[:testTrainingSplitIndex]

import itertools as it
def getVocublary():
    positiveWordList = [word for line in trainingPositiveReviews for word in line.split()]
    negativeWordList = [word for line in trainingNegativeReviews for word in line.split()]
    allWordList = [item for sublist in [positiveWordList,negativeWordList] for item in sublist]
    allWordList1 = [item for item in it.chain([positiveWordList,negativeWordList])]
    allWordSet = list(set(allWordList))
    vocabulary = allWordSet


def superNaiveSentiment(review):
    reviewPolarity =0.0
    numExceptions = 0
    for word in review.lower().split():
        # print(word)
        weight = 0.0
        try:
            common_meaning = list(swn.senti_synsets(word))[0]
            if common_meaning.pos_score() > common_meaning.neg_score():
                weight =weight + common_meaning.pos_score()
            elif common_meaning.pos_score() < common_meaning.neg_score():
                weight = weight - common_meaning.neg_score()
        except:
            numExceptions = numExceptions + 1
        
        reviewPolarity = reviewPolarity + weight
    return reviewPolarity


def getReviewSentiments(sentimentCalculator):
    
    negReviewResult = [sentimentCalculator(oneNegativeReview) for oneNegativeReview in negativeReviews]
    posReviewResult = [sentimentCalculator(onePositiveReview) for onePositiveReview in positiveReviews]

    return {"results-on-positive":posReviewResult, "results-on-negative":negReviewResult}


reviewResult = getReviewSentiments(superNaiveSentiment)

pctTrueNegative = float(sum(x < 0 for x in reviewResult["results-on-negative"])) / len(reviewResult["results-on-negative"])
pctTruePositive = float(sum(x > 0 for x in reviewResult["results-on-positive"])) / len(reviewResult["results-on-positive"])

totalAccurate = float(sum(x < 0 for x in reviewResult["results-on-negative"])) + float(sum(x > 0 for x in reviewResult["results-on-positive"]))

print("%-ve Comments:" ,pctTrueNegative,"%+ve Comments:", pctTruePositive)


total = len(reviewResult["results-on-negative"]) + len(reviewResult["results-on-positive"])
print("Accuracy Overall:=  " "%.2f" % ((totalAccurate*100)/total) + " %")


# improve accuracy
from string import punctuation
from nltk.corpus import stopwords

stopwords = set(stopwords.words("english") + list(punctuation))
print(stopwords)

# ignore punctuation + stopwords and use all meansing for a word to improve accuracy
def naiveSentiment(review):
    numMeanings =0.0
    numExceptions = 0
    reviewPolarity = 0.0    
    for word in review.lower().split():
        # print(word)
        if word in stopwords:
            continue
        weight = 0.0    
        try:
            for meaning in swn.senti_synsets(word):
                if meaning.pos_score() > meaning.neg_score():
                    weight =weight + (meaning.pos_score() - meaning.neg_score())
                    numMeanings = numMeanings + 1
                elif meaning.pos_score() < meaning.neg_score():
                    weight = weight + (meaning.pos_score() - meaning.neg_score())
                    numMeanings = numMeanings + 1

        except:
            numExceptions = numExceptions + 1
        if numMeanings > 1:
            reviewPolarity = reviewPolarity + (weight/numMeanings)
    return reviewPolarity

    
reviewResult = getReviewSentiments(naiveSentiment)

pctTrueNegative = float(sum(x < 0 for x in reviewResult["results-on-negative"])) / len(reviewResult["results-on-negative"])
pctTruePositive = float(sum(x > 0 for x in reviewResult["results-on-positive"])) / len(reviewResult["results-on-positive"])

totalAccurate = float(sum(x < 0 for x in reviewResult["results-on-negative"])) + float(sum(x > 0 for x in reviewResult["results-on-positive"]))

print("%-ve Comments:" ,pctTrueNegative,"%+ve Comments:", pctTruePositive)


total = len(reviewResult["results-on-negative"]) + len(reviewResult["results-on-positive"])
print("Accuracy Overall:=  " "%.2f" % ((totalAccurate*100)/total) + " %")

# usign stopwords affects negative comment accuracy

