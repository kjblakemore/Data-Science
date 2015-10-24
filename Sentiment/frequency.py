#
# Compute the term frequency histogram of twitter data.
#

import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    # Load the tweets
    lines = tweet_file.readlines()
    results = {}            # a list of tweets as dictionaries
    for i in range(len(lines)):
        pyresponse = json.loads(lines[i])
        results[i] = pyresponse

    # Build a dictionary containing word frequencies, indexed by the words. The frequency of a word
    # is the (number of occurrences of the word)/(number of occurrences of all words)
    dictionary = {}
    word_count = 0      # Total number of words in all tweets
    for i in range(len(results)):
        tweet = []
        if(results[i].has_key("text")):
            tweet = results[i]["text"].split()

            for j in range(len(tweet)):
                word = tweet[j].lower()
                if(word.isalpha):
                    word_count += 1
                    # Add new words to dictionary
                    if(not dictionary.has_key(word)):
                        dictionary[word] = 1    # initialize number of occurrences of this word
                    # Already in dictionary, increment the occurrence count
                    else:
                        dictionary[word] += 1
                        
    # Now print all words and their frequency
    for key in dictionary:
        encoded_key = key.encode('utf-8')
        print encoded_key, float(dictionary[key])/float(word_count)                
                    
if __name__ == '__main__':
    main()