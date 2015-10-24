#
# Creates an inverted index of a set of documents.  The inverted index is a
# dictionary where each word is associated with a list of document indentifiers
# in which that word appears.
#

import MapReduce
import sys

"""
Inverted Index in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # text: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)  # emit the word and document id

def reducer(key, list_of_strings):
    # key: word
    # list_of_strings: list of document identifiers, with duplicates
    
    mr.emit((key, list(set(list_of_strings))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
