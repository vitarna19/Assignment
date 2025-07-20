IF OBJECT_ID('dbo.CUST_MSTR', 'U') IS NOT NULL DROP TABLE dbo.CUST_MSTR;
CREATE TABLE dbo.CUST_MSTR (
    ID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Amount INT,
    Date DATE
);

IF OBJECT_ID('dbo.master_child', 'U') IS NOT NULL DROP TABLE dbo.master_child;
CREATE TABLE dbo.master_child (
    ID INT PRIMARY KEY,
    Parent NVARCHAR(100),
    Child NVARCHAR(100),
    Date DATE,
    DateKey CHAR(8)
);

IF OBJECT_ID('dbo.H_ECOM_Orders', 'U') IS NOT NULL DROP TABLE dbo.H_ECOM_Orders;
CREATE TABLE dbo.H_ECOM_Orders (
    OrderID INT PRIMARY KEY,
    Product NVARCHAR(100),
    Quantity INT
);
