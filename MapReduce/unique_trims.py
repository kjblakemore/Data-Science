import MapReduce
import sys

"""
Unique nucleotides in the Simple Python MapReduce Framework.
Given a list of nucleotides, strip the last 10 characters and print resulting
unique nucleotide strings.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Mapper takes a record of the form (sequence_id, nucleotides), where sequence_id
# is a unique identifier for the sequence and nucleotides is a string
# representing a sequence of nucleotides.  It strips the last 10 characters from
# the nucleotide and then emits the resulting string with an occurrence count of
# 1.
def mapper(record):
    nucleotides = record[1][:-10]   # strip last 10 chars from nucleotides
    mr.emit_intermediate(nucleotides, 1)

# Reducer takes as input a pair (nucleotide, list_of_values), where nucleotide
# is a unique trimmed nucleotide and list of values is a list of occurrence counts
# for the nucleotide.  It emits the nucleotide.
def reducer(nucleotide, list_of_values):
    mr.emit(nucleotide)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
