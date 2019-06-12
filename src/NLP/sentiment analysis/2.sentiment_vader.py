# download cornells movie review data
import os
from nltk.sentiment import vader
if os.name == 'nt':
    positiveReviewFileName = r"D:\github\python\src\NLP\sentiment analysis\rt-polaritydata\rt-polarity.pos"
    negitiveReviewFileName = r"D:\github\python\src\NLP\sentiment analysis\rt-polaritydata\rt-polarity.neg"
    

with open(positiveReviewFileName, 'r') as f:
    positiveReviews = f.readlines()

print(positiveReviews)
print(len(positiveReviews))


with open(negitiveReviewFileName, 'r') as f:
    negitiveReviews = f.readlines()

print(negitiveReviews)
print(len(negitiveReviews))

sia = vader.SentimentIntensityAnalyzer()

def vaderSentiment(review):
    return sia.polarity_scores(review)['compound']

vaderSentiment(positiveReviews[0])

def getReviewSentiments(sentimentCalculator):
    
    negReviewResult = [sentimentCalculator(oneNegativeReview) for oneNegativeReview in negitiveReviews]
    posReviewResult = [sentimentCalculator(onePositiveReview) for onePositiveReview in positiveReviews]

    return {"results-on-positive":posReviewResult, "results-on-negative":negReviewResult}


reviewResult = getReviewSentiments(vaderSentiment)

pctTrueNegative = float(sum(x < 0 for x in reviewResult["results-on-negative"])) / len(reviewResult["results-on-negative"])
pctTruePositive = float(sum(x > 0 for x in reviewResult["results-on-positive"])) / len(reviewResult["results-on-positive"])

totalAccurate = float(sum(x < 0 for x in reviewResult["results-on-negative"])) + float(sum(x > 0 for x in reviewResult["results-on-positive"]))

print("%-ve Comments:" ,pctTrueNegative,"%+ve Comments:", pctTruePositive)


total = len(reviewResult["results-on-negative"]) + len(reviewResult["results-on-positive"])
print("Accuracy Overall:=  " "%.2f" % ((totalAccurate*100)/total) + " %")

