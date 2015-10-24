import MapReduce
import sys

"""
Non-symmetric Friend Relationships in the Simple Python MapReduce Framework.
Given a list of friend relationships in the form (personA, personB), output the 
asymmetric relationships as pairs of friendships, (personA, personB) and 
(personB, personA).
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Mapper takes a record of the form (personA, personB), where personB is a friend
# of person A.  It emits the record sorted in alphabetical order.
def mapper(record):
    record.sort()
    mr.emit_intermediate((record[0],record[1]), 1)

# Reducer takes as input unordered friendship pairs and a list of occurrences
# of these friendships.  It generates a list of friendships, excluding those
# which are symmetric.
def reducer(record, list_of_values):
    # record: unordered friendship pair
    # list_of_values: list of occurrences of this friendship
    total = 0
    for v in list_of_values:
        total += v
        
    if total==1:
        mr.emit((record[0], record[1]))
        mr.emit((record[1], record[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
