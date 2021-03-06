# Example-1
SELECT 
	customerNumber,
    customerName, 
    CONCAT(TRIM(BOTH ' ' FROM contactFirstName), ' ', contactLastName) AS contactName,
    UPPER(country), 
    ROUND(creditLimit, 0) AS creditLimit, 
    ROUND((creditLimit / 1.21), -2) AS creditLimit_Euro,
    creditLimit > 100000 AS isPremiumCustomer
    # DISTINCT xyz    # and there is this DISTINCT thing.
FROM classicmodels.customers
WHERE country NOT IN ('USA', 'Australia') AND creditLimit > 0
# WHERE country != 'USA'
ORDER BY customerNumber ASC
LIMIT 20;

# Example-2
SELECT
	rating,
	# these are called "aggregate functions":
    MAX(rental_duration),
    MIN(rental_rate),
    ROUND(AVG(length), 1) AS length_avg,
    SUM(replacement_cost)
FROM sakila.film
WHERE rental_rate > 1.99
GROUP BY 1    # 1st column. Could write "rating". GROUP BY is placed between these two.
ORDER BY SUM(replacement_cost) DESC;

# Example-3
SELECT
	salesRepEmployeeNumber,
	COUNT(*),    # group by sütun ile gruplanan kayıtların satır sayısını verir.
    ROUND(AVG(creditLimit), 0) AS creditLimit_avg, 
    ROUND(MAX(creditLimit), 0) AS creditLimit_max,
    ROUND(MIN(creditLimit), 0) AS creditLimit_min
FROM classicmodels.customers
GROUP BY salesRepEmployeeNumber;

# Example-4
SELECT
	productLine,
    productScale,
    COUNT(*) AS record_count
FROM
	classicmodels.products
GROUP BY
	1, 2
ORDER BY record_count DESC;
    
# Example-5
SELECT 
	productLine,
    ROUND(AVG(buyPrice), 1) AS buyPrice_avg
FROM classicmodels.products
GROUP BY productLine
HAVING buyPrice_avg >= 47
# WHERE buyPrice_avg >= 48    # 'where' cannot be used w/ aggregate funcs.
ORDER BY buyPrice_avg ASC;

# Example-6
SELECT
	ord.orderNumber, 
    ord.orderDate, 
    cus.customerNumber,
    cus.contactLastName,
    cus.contactFirstName
FROM
	orders ord    # "aliases' are used
JOIN
	customers cus
ON
	ord.customerNumber = cus.customerNumber
LIMIT
	20
;

# Example-7
SELECT
	customerName, 
    contactLastName,
    contactFirstName, 
    country,
CASE country
	WHEN "USA"
		THEN "Hasan"
	WHEN "Canada"
		THEN "(Empty)"
	ELSE "Mert"
END "Representer"
FROM classicmodels.customers
;

# Example-8
CREATE TABLE orderdetails_abbreviated AS
SELECT
	orderNumber,
    productCode
FROM orderdetails
	orderdetails
LIMIT
	20
;
