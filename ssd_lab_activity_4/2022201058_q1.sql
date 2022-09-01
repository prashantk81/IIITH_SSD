drop procedure if exists add_two_numbers; 

DELIMITER //
Create Procedure add_two_numbers(in num1 int, in num2 int, out result int)
Begin
    Set result = num1+num2;
End //

call add_two_numbers(4, 4, @result);
select @result;

