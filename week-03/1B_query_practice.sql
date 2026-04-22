USE northwind;

-- 1. Write a query to list the product id, product name, and unit price of every product that
-- Northwind sells. (Hint: To help set up your query, look at the schema preview to see
-- what column names belong to each table. Or use SELECT * to query all columns
-- first, then refine your query to just the columns you want.)

SELECT 
    ProductID,
    ProductName,
    UnitPrice
FROM
	northwind.Products;
    
-- 2. Write a query to identify the products where the unit price is $7.50 or less.

SELECT 
    ProductID,
    ProductName,
    UnitPrice
FROM
	northwind.Products
WHERE UnitPrice <= 7.50;

-- 3. What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question.

SELECT
	ProductID,
    ProductName,
    UnitPrice,
    UnitsOnOrder,
    UnitsInStock
FROM
	northwind.Products
WHERE
	UnitsOnOrder > 0
AND
    UnitsInStock <= 0
;

-- 4. Examine the products table. How does it identify the type (category) of each item
-- sold? Where can you find a list of all categories? Write a set of queries to answer these
-- questions, ending with a query that creates a list of all the seafood items we carry.

SELECT
	CategoryID,
    CategoryName,
    description
FROM
	northwind.Categories; 
-- The type of item is categorized by numerical values 1-8.

SELECT
	*
FROM
	northwind.categories;
-- returns all results for categories, including pictures.

SELECT
	p.ProductName,
    c.CategoryName
FROM
	northwind.Products P
JOIN
	northwind.Categories C
ON
	p.CategoryID = c.CategoryID
    ;
    
-- Shows Product names and their categories

SELECT
	p.ProductName,
    c.CategoryName
FROM
	northwind.Products P
JOIN
	northwind.Categories C
ON
	p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';

-- returns all seafood products

-- 5. Examine the products table again. How do you know what supplier each product
-- comes from? Where can you find info on suppliers? Write a set of queries to find the
-- specific identifier for "Tokyo Traders" and then find all products from that supplier.

SELECT
	ProductID,
    ProductName,
    SupplierID
FROM
	northwind.Products;
-- Returns productID, name, and the supplierID

SELECT
	SupplierID,
    CompanyName,
    ContactName,
    City,
    country
FROM
	northwind.suppliers;
-- Returns suppliers, names, and geographic info. "Tokyo Traders ID = 4"

SELECT
	ProductID,
    ProductName,
    UnitPrice,
    SupplierID
From
	northwind.Products
WHERE
	SupplierID = 4;
-- Returns all products and prices for supplier ID 4 (Tokyo Traders)

SELECT 
    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    s.CompanyName
FROM 
	northwind.Products p
JOIN 
    northwind.Suppliers s
ON 
    p.SupplierID = s.SupplierID
WHERE 
    s.CompanyName = 'Tokyo Traders';
-- Join returns all products from company name "Tokyo Traders"

-- How many employees work at northwind? What employees have "manager"
-- somewhere in their job title? Write queries to answer each question.

SELECT
	EmployeeID,
    FirstName,
    LastName
FROM
	northwind.employees;
-- Returns first and last names of northwind employees with ID (returned 9 employees)

SELECT
	EmployeeID,
    FirstName,
    LastName,
    Title
FROM
	Northwind.employees
WHERE
	Title LIKE '%manager%';
-- returns employees who's title contains "Manager" the only manager at northwind is Steven Buchanan