use CUSTOMER_DB;
drop table if exists result;
drop procedure if exists cursor_problem; 
CREATE TABLE result(Naam varchar(40),
city varchar(35),
country varchar(20),grade int);
DELIMITER //
create procedure cursor_problem()
begin
DECLARE DONE INT DEFAULT FALSE;
DECLARE Naam varchar(40);
DECLARE city varchar(35);
DECLARE country varchar(20);
DECLARE grade_cust int;

DECLARE code_cursor cursor for
select CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE
from customer
where AGENT_CODE LIKE "A00%";
declare continue handler for not found set DONE=TRUE;
open code_cursor;

LABEL: loop 
fetch  code_cursor into Naam,city,country,grade_cust;

    if DONE THEN LEAVE LABEL;
    END IF; 
    insert into result values (naam, city, country, grade_cust);
end LOOP;
close code_cursor;
select * from result;
end //

call cursor_problem(); 




