# https://archive.ics.uci.edu/ml/machine-learning-databases/00331/

lines = " "
with open ("/home/sudeep/sources/github/pythongithub/src/ML Algorithms1/Naive bayes/sentiment labelled sentences/imdb_labelled.txt", "r" ) as text_file:
    lines = text_file.read().split("\n")
    # print(lines)
with open ("/home/sudeep/sources/github/pythongithub/src/ML Algorithms1/Naive bayes/sentiment labelled sentences/amazon_cells_labelled.txt", "r" ) as text_file:
    lines += text_file.read().split("\n")
    # print(lines)
with open ("/home/sudeep/sources/github/pythongithub/src/ML Algorithms1/Naive bayes/sentiment labelled sentences/yelp_labelled.txt", "r" ) as text_file:
    lines += text_file.read().split("\n")
    # print(lines)

lines =  [line.split("\t") for line in lines if (len(line.split("\t"))==2 and line.split("\t")[1] != '' or len(line.split("\t0"))==2 and line.split("\t0")[1] != '')]

print(type(lines))

train_documents  = [line[0] for line in lines]
train_labels = [int(line(1) for line in  lines)]