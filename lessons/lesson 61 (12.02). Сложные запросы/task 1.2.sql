
SELECT Customers.FirstName, Customers.LastName, Orders.OrderID, Orders.TotalAmount
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

SELECT FirstName, LastName, NULL AS OrderID, NULL AS TotalAmount
FROM Customers
UNION
SELECT NULL, NULL, OrderID, TotalAmount
FROM Orders;