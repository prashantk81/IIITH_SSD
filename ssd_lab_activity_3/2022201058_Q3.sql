select Mgr_ssn, count(*)
from WORKS_ON as wt,
(select Mgr_ssn
from PROJECT as pj, DEPARTMENT as dp
where Pname='ProductY' and pj.Dnum=dp.Dnumber) as temp
where wt.Essn=temp.Mgr_ssn
