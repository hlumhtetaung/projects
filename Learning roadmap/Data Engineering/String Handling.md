**String Handling**



String functions for cleaning data

* TRIM
* Normalize with LOWER/UPPER
* || returns NULL if any part is NULL - CONCAT() doesn't
* ILIKE = case-insensitive LIKE



String Functions (Data cleaning)

* INITCAP(customer\_city): Capitalize the initial letters of the word
* UPPER(TRIM(customer\_city)): Capitalize every letters of the word
* LENGTH(customer\_city): Returns the length of words (include space)
* LEFT(customer\_city, 2): Returns two letters counting from the left
* RIGHT(): Same as LEFT but from RIGHT
* SPLIT\_PART('health\_beauty', '\_', 1); () - will return health after splitting health\_beauty
* REPLACE('bath\_with\_Itsuki', '\_', ' '): Returns \_ replaced with space



String Functions (Padding, slicing and regex)

* LPAD('1001', 5, '0'): Add 0 at the front so the length become 5 characters
* RPAD(): Same us LPAD but from right (from the end)
* SUBSTRING('health\_beauty', 1, 6): Return 6 characters starting from index 1
* STRPOS('bed\_bath', '\_'): Find string position of \_



**REGEXP**









