#
# Implements a relational join as a MapReduce query.
#

import MapReduce
import sys

"""
Relational Join in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Mapper accepts records in one of the following two forms:
#   "line_item" order_id attribute2 attribute3 ... attribute17
#   "order" order_id element2 element3 ... element10
# The input records are mapped into (key, value) pairs, where key is the order_id and value
# is the input record.
def mapper(record):
    # key: order_id
    # record: the string "line_item" followed by 16 attributes or the string "order"
    #        followed by 9 elements.
    
    key = record[1]
    mr.emit_intermediate(key, record)

# Reducer takes an order_id and list of records corresponding to the order id.
# It returns the concatenation of each unique (order, line_item) pair of records.
def reducer(key, list_of_records):
    # key: order_id
    # list_of_records: list of all line_item and order records for the order_id.
    for record1 in list_of_records:
        if record1[0] == "order":
            for record2 in list_of_records:
                if record2[0] == "line_item":
                    mr.emit(record1 + record2)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
