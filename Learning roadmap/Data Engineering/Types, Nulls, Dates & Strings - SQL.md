**Types, Nulls, Dates \& Strings**



Data Types:

* INTEGER/BIGINT
* NUMERIC
* DOUBLE
* TEXT/VARCHAR
* DATE/TIMESTAMP
* BOOLEAN



Casting change data type of a value.



**Null Semantics**



How NULL behaves in everyday SQL

* Use IS NULL/IS NOT NULL with null values
* Aggregates functions skip NULLs
* COUNT(col) skips NULLs
* Arithmetic results in NULL
* Nulls sort last in ASC sorting
* All NULLs fall into one group in GROUP BY



COALESCE() can be use to fill null values with a string or other related column values.

CASE WHEN, NULLIF can also be used.



**Dates \& Time**

EXTRACT(YEAR FROM time\_stamp) -- extract year from date data

TO\_DATE() change date text to date format



