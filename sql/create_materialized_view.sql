-- Example: Creating a materialized view in Databricks using the Delta format
-- Adjust the catalog, schema, table, and view names to match your environment.

CREATE OR REPLACE MATERIALIZED VIEW example_catalog.example_schema.summary_view
USING DELTA
AS
SELECT column1,
       COUNT(*) AS total_count
FROM example_catalog.example_schema.source_table
GROUP BY column1;
