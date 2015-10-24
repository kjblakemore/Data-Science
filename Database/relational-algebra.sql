/*
 * Inspecting the Reuters Data Set; Basic Relational Algebra
 */

/* Select */
SELECT count(*) FROM (
    SELECT * FROM frequency WHERE docid="10398_txt_earn"
    );

/* Select Project */
SELECT count(*) FROM (
    SELECT term FROM frequency WHERE docid="10398_txt_earn" AND count=1
    );

/* Union */
SELECT count(*) FROM (
    SELECT term FROM frequency WHERE docid="10398_txt_earn" AND count=1
    UNION
    SELECT term FROM frequency WHERE docid="925_txt_trade" AND count=1
    );

 /* Count the number of documents containing the word "parliament" */
 SELECT count(*) FROM (
    SELECT docid FROM frequency WHERE term="parliament"
    );

 /* Find all documents having more than 300 terms, including duplicate terms */
 SELECT count(*) FROM (
    SELECT docid, SUM(count)
    FROM frequency
    GROUP BY docid
    HAVING SUM(count) > 300
    );

/* Count the number of unique documents that contain both the word 'transaction'
   and the word 'world'. */
CREATE VIEW term_transactions AS
    SELECT * FROM frequency WHERE term="transactions";
CREATE VIEW term_world AS
    SELECT * FROM frequency WHERE term="world";
SELECT count(*) FROM (
    SELECT * FROM term_transactions t, term_world w
    WHERE t.docid = w.docid
    );
