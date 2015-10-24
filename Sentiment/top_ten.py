#
# Compute the top ten most frequently occurring hashtags in the twitter data.
#

import sys
import json
from collections import Counter

def main():
    tweet_file = open(sys.argv[1])

    # Load the tweets
    lines = tweet_file.readlines()
    results = {}            # a list of tweets as dictionaries
    for i in range(len(lines)):
        pyresponse = json.loads(lines[i])
        results[i] = pyresponse

    # Create a dictionary of hashtags and their counts
    dictionary = {}
    for i in range(len(results)):   # for each tweet in the file
        entities = {}
        if(results[i].has_key("entities")):
            entities = results[i]["entities"]
            hashtags = []
            if(entities.has_key("hashtags")):
                hashtags = entities["hashtags"]
                for j in range(len(hashtags)):
                    hashtag = hashtags[j]["text"]
                    if(dictionary.has_key(hashtag)):    # Already in dictionary, increment count
                        dictionary[hashtag] += 1
                    else:                               # New entry in dictionary
                        dictionary[hashtag] = 1
                           
    # Sort dictionary and print top 10 hashtags and their values
    sorted_dictionary = Counter(dictionary)
    for hashtag, count in sorted_dictionary.most_common(10):
        encoded_hashtag = hashtag.encode('utf-8')   
        print '%s: %i' % (encoded_hashtag, count)

if __name__ == '__main__':
    main()