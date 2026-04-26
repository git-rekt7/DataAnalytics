-- 1. Create a single query to list the product id, product name, unit price and category
-- name of all products. Order by category name and within that, by product name.

SELECT
	ProductID,
    ProductName,
    UnitPrice,
    CategoryName
FROM
	products
JOIN
	categories
ON
	categories.CategoryID = products.CategoryID;
    
-- 2. Create a single query to list the product id, product name, unit price and supplier
-- name of all products that cost more than $75. Order by product name.

SELECT
	p.ProductID,
    p.ProductName,
    p.UnitPrice,
    s.CompanyName
FROM
	products p
JOIN
	suppliers s
ON
	p.SupplierID = s.SupplierID
WHERE
	UnitPrice > 75
ORDER BY
	ProductName;

-- 3. Create a single query to list the product id, product name, unit price, category name,
-- and supplier name of every product. Order by product name.

SELECT
	ProductID,
    ProductName,
    UnitPrice,
    CategoryName,
    CompanyName
FROM
	Products p 
JOIN
	Categories c ON c.CategoryID = p.CategoryID
JOIN
	Suppliers s ON s.SupplierID = p.SupplierID
ORDER BY
	ProductName;
    
-- 4. Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
-- shipped to.

SELECT
    o.OrderID,
    o.ShipAddress,
    o.ShipName,
    s.CompanyName AS 'Shipper'
FROM
    Orders o
JOIN Shippers s ON o.ShipVia = s.ShipperID

WHERE
	o.ShipCountry = 'Germany'
ORDER BY
	ShipName;
    
-- 5. Start from the same query as above (#4), but omit OrderID and add logic to group by
-- ship name, with a count of how many orders were shipped for that ship name.

SELECT
    o.ShipName,
    s.CompanyName AS Shipper,
    COUNT(o.OrderID) AS "Order Count"
FROM
    Orders o
JOIN Shippers s ON o.ShipVia = s.ShipperID
WHERE
    o.ShipCountry = 'Germany'
GROUP BY
    o.ShipName, s.CompanyName
ORDER BY
    o.ShipName;
    
-- 6. Create a single query to list the order id, order date, ship name, ship address of all
-- orders that included Sasquatch Ale.

SELECT
    o.OrderID,
    o.OrderDate,
    o.ShipName,
    o.ShipAddress
FROM
    Orders o
JOIN `Order Details` od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE
    p.ProductName = 'Sasquatch Ale';
    

	

    
    
    
	