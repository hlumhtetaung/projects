**Data Engineering - Day 2**



Data modeling

* Seeing if the dataset's features should be made a dimension table or put in fact table.

There can be more than one fact table for different values, such as insurance transaction and insurance claim. Claims and transaction can't be combine due to different natures.



Single point failure?





Two data modeling schema taught -

* Star schema
* Snowflake schema



Difference

* Star schema

  * One join per dimension
  * Easy for analysts
  * Dashboards, ad-hoc analysis - most cases
* Snowflake schema

  * Extra join for every level
  * Not easy for analysts
  * Very large or frequent changing hierarchies



Course will use star schema.

