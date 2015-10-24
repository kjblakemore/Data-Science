/*
 * Operating on the reuters data set as a term-document matrix.  Each row of the
 * matrix is a document vector, with one column for every term in the entire
 * corpus.
 */


/* 
 * Computes the similarity matrix by multiplying the matrix by its' transpose. 
 */
SELECT A.docid, B.docid, SUM(A.count*B.count)
FROM frequency A, frequency B
WHERE A.term = B.term AND A.docid < B.docid
GROUP BY A.docid, B.docid;

/* 
 * Finds the best matching document to the keyword query "washington taxes 
 * treasury", using the similarity matrix and filtering for matches to 
 * the keywords. The keywords were added to the document set using the
 * following:
 * SELECT * FROM frequency
 * UNION
 * SELECT 'q' as docid, 'washington' as term, 1 as count
 * UNION
 * SELECT 'q' as docid, 'taxes' as term, 1 as count
 * UNION
 * SELECT 'q' as docid, 'treasury' as term, 1 as count
 */
SELECT B.docid, SUM(A.count*B.count)
    FROM q_frequency A, frequency B
    WHERE A.term = B.term AND A.docid <> B.docid
    GROUP BY A.docid, B.docid;