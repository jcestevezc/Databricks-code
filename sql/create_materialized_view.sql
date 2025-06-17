-- Example: Creating a materialized view in Databricks
-- Adjust the schema, table, and view names to match your environment.

CREATE OR REPLACE MATERIALIZED VIEW example.summary_view AS
SELECT column1,
       COUNT(*) AS total_count
FROM example.source_table
GROUP BY column1;
