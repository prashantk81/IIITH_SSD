drop procedure if exists name_cust; 

DELIMITER //
Create Procedure name_cust(in CITY varchar(35))
Begin
    select CUST_NAME from customer where WORKING_AREA =CITY;
End //

call name_cust("Bangalore");

