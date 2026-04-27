
-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price.

-- One
SELECT
	MIN(UnitPrice)
FROM
	Products;

-- Two
SELECT
	ProductName
FROM
	products
WHERE
	UnitPrice = 2.50;
    
-- 2. Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
-- using the ROUND function to round the average price to the nearest cent.)

SELECT 
	ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM 
	Products;
    
-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.

-- One
SELECT
	MAX(UnitPrice)
FROM 
	Products;

-- Two

SELECT
	p.ProductName,
    s.CompanyName AS Supplier,
    p.UnitPrice
FROM
	products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE
 p.UnitPrice = (SELECT MAX(UnitPrice) FROM Products);
 
--  4. Write a query to find total monthly payroll (the sum of all the employees’ monthly
-- salaries).

SELECT
	ROUND(SUM(Salary) / 12, 2) AS MonthlyPayroll
FROM
	Employees;
    
-- 5. Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)

SELECT
    MAX(Salary) AS HighestSalary,
    MIN(Salary) AS LowestSalary
FROM Employees;

-- 6. Write a query to find the name and supplier ID of each supplier and the number of
-- items they supply. Hint: Join is your friend here.

SELECT
    s.CompanyName AS Supplier,
    s.SupplierID,
    COUNT(p.ProductID) AS ItemCount
FROM
    Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY
    s.SupplierID, s.CompanyName
ORDER BY
    ItemCount DESC;
    
-- 7. Write a query to find the list of all category names and the average price for items in
-- each category.

SELECT
    c.CategoryName,
    ROUND(AVG(p.UnitPrice), 2) AS AveragePrice
FROM
    Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY
    c.CategoryID, c.CategoryName
ORDER BY
    AveragePrice DESC;
    
-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply.

SELECT
    s.CompanyName AS Supplier,
    COUNT(p.ProductID) AS ItemCount
FROM
    Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY
    s.SupplierID, s.CompanyName
HAVING
    COUNT(p.ProductID) >= 5
ORDER BY
    ItemCount DESC;
    
-- 9. Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list.

SELECT
    p.ProductID,
    p.ProductName,
    ROUND(p.UnitPrice * p.UnitsInStock, 2) AS InventoryValue
FROM
    Products p
WHERE
    p.UnitsInStock > 0
ORDER BY
    InventoryValue DESC,
    p.ProductName ASC;

