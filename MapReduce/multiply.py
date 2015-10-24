import MapReduce
import sys

"""
Matix Multiplication for 4x4 matrices in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Mapper accepts records of the form [matrix, i, j, value], where matrix is
# either 'a' or 'b', i and j are row and column numbers and value is the
# corresponding value.  The record is mapped to every cell of the resulting C
# matrix.
def mapper(record):
    matrix = record[0]
    if matrix == 'a':
        i = record[1]
        for j in range(0,5):
            mr.emit_intermediate((i,j), record)
    if matrix == 'b':
        j = record[2]
        for i in range(0,5):
            mr.emit_intermediate((i,j), record)

# Reducer accepts as input the pair (C_indices, records), where C_indices is a 
# row and column number for the entry in C which is the product of the A row
# and B column in the records list.
def reducer(C_indices, records):
    intermediate_values = []    # list of a(i,j)*b(j,k), for all j = 0..4
    # for each a(i,j) find b(j,k)
    for a in records:   # r is of the form [matrix, i, j, value]
        if a[0] == 'a':
            for b in records:
                if b[0] == 'b':
                    if a[2] == b[1]:
                        intermediate_values.append(a[3]*b[3]) # a(i,j) * b(j,k) 
    total = 0
    for v in intermediate_values:
      total += v
    mr.emit((C_indices[0], C_indices[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
