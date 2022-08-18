select Fname, Minit, Lname , Ssn, Dnumber, temp2.ssn_count 
from EMPLOYEE as emp,
(select Dnumber, Mgr_ssn, temp.ssn_count
from DEPARTMENT as dp,
(select Super_ssn,count(*) as ssn_count
from EMPLOYEE
group by Super_ssn) as temp
where temp.Super_ssn= dp.Mgr_ssn) as temp2
where temp2.Mgr_ssn= emp.Ssn

