#
# Derive the sentiment of new terms not contained in the pre-computed
# sentiment scores.  


import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # Build the sentiment dictionary
    line = sent_file.readline()
    dictionary = {}
    while(line):
        entry = line.split()
        phrase = entry[0]
        for i in range(1,len(entry)-1):
            phrase = phrase + ' ' + entry[i]
        dictionary[phrase] = float(entry[len(entry)-1])
        line = sent_file.readline()

    # Load the tweets
    lines = tweet_file.readlines()
    results = {}            # a list of tweets as dictionaries
    for i in range(len(lines)):
        pyresponse = json.loads(lines[i])
        results[i] = pyresponse

    # Calculate sentiments for the tweets and create a dictionary of the words not in the 
    # original dictionary.
    tweet_sentiment = {}    # a list of sentiments for each tweet
    new_dictionary = {}     # dictionary of the new words
    for i in range(len(results)):
        tweet = []
        if(results[i].has_key("text")):
            tweet = results[i]["text"].split()
        
            tweet_sentiment[i] = 0.0
            # Make first pass through a tweet to calculate the tweet sentiment.
            for j in range(len(tweet)):
                word = tweet[j].lower()    # convert word to lower case
                if(word.isalpha and dictionary.has_key(word)):
                    tweet_sentiment[i] += dictionary[word]
                
            # Second pass through a tweet, to find new words and compute their sentiment
            for j in range(len(tweet)):
                word = tweet[j].lower()
                if(word.isalpha and not dictionary.has_key(word)):
                    # If in new dictionary add in the tweet sentiment
                    if(new_dictionary.has_key(word)):
                        new_dictionary[word] += tweet_sentiment[i]
                    # Add to new dictionary, initializing the sentiment to the tweet sentiment
                    else:
                        new_dictionary[word] = tweet_sentiment[i]
                        
    # Now average the sentiments in the new dictionary and print each word & sentiment
    for key in new_dictionary:
        encoded_key = key.encode('utf-8')
        print encoded_key, new_dictionary[key]                  
                    
if __name__ == '__main__':
    main()