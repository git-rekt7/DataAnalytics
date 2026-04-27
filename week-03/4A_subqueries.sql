-- 1. What is the product name(s) of the most expensive products?


SELECT 
	ProductName, 
    UnitPrice
FROM 
	Products
WHERE UnitPrice = (
    SELECT 
		MAX(UnitPrice)
    FROM 
		Products
);

-- 2. What is the product name(s) and categories of the least expensive products?


SELECT 
	p.ProductName, 
	c.CategoryName, 
	p.UnitPrice
FROM 
	Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (
    SELECT 
		MIN(UnitPrice)
    FROM 
		Products
);

-- 3. What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?

SELECT 
	OrderID, 
    ShipName, 
    ShipAddress
FROM Orders
WHERE ShipVia = (
    SELECT 
		ShipperID
    FROM 
		Shippers
    WHERE 
    CompanyName = 'Federal Shipping'
);

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?

SELECT 
	OrderID
FROM 
	`Order Details`
WHERE ProductID = (
    SELECT 
		ProductID
    FROM 
		Products
    WHERE 
		ProductName = 'Sasquatch Ale'
);

-- 5 and 6

SELECT 
    o.OrderID,
    c.CompanyName AS CustomerName,
    CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName
FROM 
	Orders o
JOIN `Order Details` od ON o.OrderID = od.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
JOIN Employees e ON o.EmployeeID = e.EmployeeID
WHERE od.ProductID = (
    SELECT 
		ProductID
    FROM 
		Products
    WHERE 
		ProductName = 'Sasquatch Ale'
);

-- Order 10266 employee is Robert King. The customer that bought it was "White Clover Markets"