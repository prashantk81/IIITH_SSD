select Fname,Minit,Lname,Ssn,Dno, dname
from EMPLOYEE as et,
(select Dname,Mgr_ssn
from DEPARTMENT as dep,
(
select distinct Super_ssn
from EMPLOYEE as emp,(select distinct Essn
from WORKS_ON
where Hours<40) as temp
where emp.Ssn = temp.Essn
) as temp2
where dep.Mgr_ssn= temp2.Super_ssn ) as temp3
where et.Ssn= temp3.Mgr_ssn;

