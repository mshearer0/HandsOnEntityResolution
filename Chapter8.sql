# Select all rows with clusters_ids where those cluster_ids have at least one Mari match

CREATE TEMP TABLE temp AS 
    SELECT src.* FROM Chapter8.clusters_15719257497877843494 AS src
            INNER JOIN 
                (SELECT cluster_id from Chapter8.clusters_15719257497877843494 WHERE source_name = "mari") AS mari
                    ON src.cluster_id = mari.cluster_id;

# Select subset of clusters who have both an Mari match and at least one Basic match. Remove clusters with only Mari match

CREATE TEMP TABLE match AS
    SELECT src.* FROM temp AS src
        INNER JOIN
            (SELECT cluster_id FROM temp GROUP BY cluster_id HAVING COUNT(*) > 1) AS matches ON matches.cluster_id = src.cluster_id;

# Add extra columns from either basic or mari table, order by cluster for easy comparision

CREATE TABLE Chapter8.results AS
    SELECT * FROM Chapter8.basic AS bas
        INNER JOIN
            (SELECT * FROM match WHERE match.source_name = "basic") AS res1        
                ON res1.source_key = CAST(bas.unique_id AS STRING)
    UNION ALL
    SELECT * FROM Chapter8.mari AS mari
        INNER JOIN
            (SELECT * FROM match WHERE match.source_name = "mari") AS res2        
                ON res2.source_key = CAST(mari.unique_id AS STRING)
    ORDER BY confidence,cluster_id