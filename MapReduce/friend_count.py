import MapReduce
import sys

"""
Social Network Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Mapper takes a record of the form [personA, personB], where personB is a friend
# of person A.  The record is mapped to a (key, value) pair, where key is personA
# and value is 1 indicating that personA has a friend.
def mapper(record):
    mr.emit_intermediate(record[0], 1)

# Reducer takes a person name and list friend occurrence.  It converts this input
# to the pair (person, count), where count is the number of friends the person has.
def reducer(person, list_of_values):
    # person: name of the person who has friends
    # list_of_values: list of occurrence counts of friends
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((person, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
