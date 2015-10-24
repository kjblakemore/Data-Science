#
# Calculate the sentiment of each tweet.  The tweet sentiment is equal to the 
# sum of the sentiment scores for each term in the tweet.
#

import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # Build the sentiment dictionary
    line = sent_file.readline()
    sentiment_dictionary = {}
    while(line):
        entry = line.split()
        phrase = entry[0]
        for i in range(1,len(entry)-1):
            phrase = phrase + ' ' + entry[i]
        sentiment_dictionary[phrase] = float(entry[len(entry)-1])
        line = sent_file.readline()

    # Load the tweets
    lines = tweet_file.readlines()
    results = {}
    for i in range(len(lines)):
        pyresponse = json.loads(lines[i])
        results[i] = pyresponse

    #Calculate the sentiment for each tweet and print
    for i in range(len(results)):
        tweet = []
        if(results[i].has_key("text")):
            tweet = results[i]["text"].split()
        sentiment_score = 0.0
        for j in range(len(tweet)):
            if(tweet[j].isalpha and sentiment_dictionary.has_key(tweet[j])):
                sentiment_score = sentiment_score + sentiment_dictionary[tweet[j]]
        print sentiment_score

if __name__ == '__main__':
    main()