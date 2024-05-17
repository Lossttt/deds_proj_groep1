-- SalesTerritoryData --
CREATE TABLE SalesTerritoryData (
    BusinessEntityID INT,
    TerritoryID INT,
    Name VARCHAR(255),
    CountryRegionCode VARCHAR(255),
    GroupName VARCHAR(255),
    SalesYTD FLOAT,
    SalesLastYear FLOAT,
    CostYTD FLOAT,
    CostLastYear FLOAT,
    StartDate DATETIME,
    EndDate DATETIME,
);

-- EmployeeData --
CREATE TABLE EmployeeData (
    IDSK INT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    employee_title VARCHAR(255),
    birthdate DATE,
    address VARCHAR(255),
    city VARCHAR(255),
    phone_number VARCHAR(255),
    hiredate DATE,
    department_id VARCHAR(255),  
    /* EmployeeData is missing a column for the employee_id. */
);