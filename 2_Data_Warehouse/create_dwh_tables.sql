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