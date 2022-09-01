drop procedure if exists getting_details; 

DELIMITER //
Create Procedure getting_details()
Begin
    select CUST_NAME, GRADE from customer where (OPENING_AMT+RECEIVE_AMT)>10000;
End //

call getting_details();






