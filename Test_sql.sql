-- Bài 1
select email
from Person
group by email
having count(*)>1

-- Bài 2
select SalesPerson.name
from SalesPerson
except
select SalesPerson.name
from SalesPerson join Orders on SalesPerson.sales_id=Orders.sales_id
    join Company on Company.com_id=Orders.com_id
where Company.name like 'RED'

-- Bài 3
update Salary
set sex = 'p'
where sex='m'

update Salary
set sex = 'm'
where sex='f'

update Salary
set sex = 'f'
where sex='p'

-- Bài 4
select customer_id, count(visits.visit_id) as count_no_trans 
from visits left join transactions on visits.visit_id= transactions.visit_id
where transactions.transaction_id is NULL
group by visits.customer_id
order by count(visits.visit_id) 

-- Bài 5
select * 
from Patients
where conditions like '%DIAB1%'
 
-- Bài 6
select name, sum(amount) as balance
from Users join Transactions on Users.account= Transactions.account
group by name
having sum(amount) >10000

-- Bài 7
(select Employees.employee_id 
from Employees 
union 
select Salaries.employee_id 
from Salaries)
except
(select Employees.employee_id 
from Employees join Salaries on Employees.employee_id=Salaries.employee_id)

-- Bài 8
select employee_id,
    case when name not like 'M%' and employee_id%2=1 then salary*1
        else 0
    end as bonus
from Employees
order by employee_id

-- Bài 9
select sell_date, count(*) as num_sold, string_agg(product,',') as products
from (select distinct sell_date, product from Activities) as sub
group by sell_date

-- Bài 10
select Product.product_id, product_name 
from Product join Sales on Sales.product_id= Product.product_id
where sale_date between '2019-01-01' and '2019-03-31' 
except
select Product.product_id, product_name 
from Product join Sales on Sales.product_id= Product.product_id 
where sale_date not between '2019-01-01' and '2019-03-31' 
