-- ejercicio 1
SELECT * FROM customers
where Country = 'Brazil'

-- ejercicio 2
SELECT * FROM employees
WHERE title = 'Sales Support Agent'

--ejercicio 3
SELECT tracks.Name, albums.Title, artists.Name from tracks 

inner join albums 
on tracks.AlbumId = albums.AlbumId
inner join artists 
ON albums.ArtistId = artists.ArtistId

where artists.name = 'AC/DC'

--ejercicio 4
SELECT customerid, firstname, lastname, country FROM customers
WHERE NOT Country = 'USA'

--ejercicio 5
SELECT lastname, firstname, address, city, state, country, email  
FROM employees
WHERE title = 'Sales Support Agent'

--ejercicio 6
SELECT country  FROM customers
INNER JOIN invoices ON invoices.CustomerId = customers.CustomerId
GROUP BY country

--ejercicio 7
SELECT COUNT (customerid), state, country  FROM customers
WHERE country = 'USA'
GROUP BY state

--ejercicio 8
SELECT SUM(quantity) FROM invoice_items
WHERE invoiceid = 37

--ejercicio 9
SELECT COUNT (tracks.Name), albums.Title, artists.Name from tracks 

inner join albums 
on tracks.AlbumId = albums.AlbumId
inner join artists 
ON albums.ArtistId = artists.ArtistId

where artists.name = 'AC/DC'

--ejercicio 10
SELECT invoiceid, COUNT (quantity) 
FROM invoice_items
group by invoiceid

--ejercicio 11
SELECT country, COUNT (*) AS num_faturas
FROM customers
INNER JOIN invoices ON invoices.CustomerId = customers.CustomerId
GROUP BY country

--ejercicio 12 
SELECT COUNT (invoiceid)
FROM invoices
where invoicedate like '2009%' or invoicedate like '2011%'

--ejercicio 13
SELECT COUNT (invoiceid)
FROM invoices
where invoicedate BETWEEN '2009/01/01%' AND '2011/12/31%'

--ejercicio 14
SELECT country, customerid
FROM customers
where country ='Spain' or country = 'Brazil'
GROUP BY country

--ejercicio 15
SELECT name
FROM tracks
where name like 'You%'

--SEGUNDA PARTE 
--ejercicio 1
SELECT customers.country, customers.FirstName, invoices.invoiceid, invoices.invoicedate, invoices.billingcountry
FROM invoices

inner join customers on customers.customerId = invoices.customerId
where country = 'Brazil'

--ejercicio 2
SELECT 
    invoices.InvoiceId AS 'ID Factura',
    invoices.InvoiceDate AS 'Fecha Factura',
    invoices.Total AS 'Total',
    employees.EmployeeId AS 'ID Agente',
    employees.FirstName || ' ' || employees.LastName AS 'Nombre Completo Agente'
FROM 
    invoices 
JOIN 
    customers ON invoices.CustomerId = customers.CustomerId
JOIN 
    employees ON customers.SupportRepId = employees.EmployeeId
ORDER BY 
    employees.LastName, employees.FirstName, invoices.InvoiceDate

--ejercicio 3
SELECT 
    customers.FirstName || ' ' || customers.LastName AS 'NombreCliente',
    customers.Country AS 'País',
    employees.FirstName || ' ' || employees.LastName AS 'NombreAgente',
    invoices.Total AS 'TotalFactura'
FROM 
    invoices 
JOIN 
    customers ON invoices.CustomerId = customers.CustomerId
JOIN 
    employees ON customers.SupportRepId = employees.EmployeeId
ORDER BY 
    customers.Country, 'NombreCliente', invoices.InvoiceDate

--ejercicio 4
SELECT 
    invoice_items.InvoiceId,
    tracks.Name,
    invoice_items.Quantity AS 'Cantidad'
FROM 
    invoice_items 
JOIN 
    tracks ON invoice_items.TrackId = tracks.TrackId
ORDER BY 
    invoice_items.InvoiceId

--ejercicio 5
SELECT 
    tracks.Name,
    media_types.Name,
    albums.Title,
    genres.Name
FROM 
    tracks 
JOIN 
    media_types ON tracks.MediaTypeId = media_types.MediaTypeId
JOIN 
    albums ON tracks.AlbumId = albums.AlbumId
JOIN 
    genres ON tracks.GenreId = genres.GenreId
ORDER BY 
    tracks.Name

--ejercicio 6
SELECT 
    playlists.PlaylistId ,
    playlists.Name ,
    COUNT(playlist_track.TrackId) 
FROM 
    playlists 
LEFT JOIN 
    playlist_track ON playlists.PlaylistId = playlist_track.PlaylistId
GROUP BY 
    playlists.PlaylistId, playlists.Name
ORDER BY 
    COUNT(playlist_track.TrackId) DESC

--ejercicio 7
SELECT 
    employees.EmployeeId,
    employees.FirstName, 
    employees.LastName,
    SUM(invoices.Total),
    COUNT(DISTINCT invoices.InvoiceId)
FROM 
    employees 
JOIN 
    customers ON employees.EmployeeId = customers.SupportRepId
JOIN 
    invoices ON customers.CustomerId = invoices.CustomerId
GROUP BY 
    employees.EmployeeId, employees.FirstName, employees.LastName
ORDER BY 
    SUM(invoices.Total) DESC

--ejercicio 8
SELECT 
    employees.EmployeeId,
    employees.FirstName, 
    employees.LastName,
    SUM(invoices.Total),
    COUNT(invoices.InvoiceId)
FROM 
    employees 
JOIN 
    customers ON employees.EmployeeId = customers.SupportRepId
JOIN 
    invoices ON customers.CustomerId = invoices.CustomerId
WHERE 
    invoices.InvoiceDate BETWEEN '2009-01-01' AND '2009-12-31'
GROUP BY 
    employees.EmployeeId, employees.FirstName, employees.LastName
ORDER BY 
    SUM(invoices.Total) DESC
LIMIT 1

--ejercicio 9
SELECT 
    artists.ArtistId,
    artists.Name,
    SUM(invoice_items.UnitPrice * invoice_items.Quantity),
    COUNT(DISTINCT invoices.InvoiceId)
FROM 
    artists 
JOIN 
    albums ON artists.ArtistId = albums.ArtistId
JOIN 
    tracks ON albums.AlbumId = tracks.AlbumId
JOIN 
    invoice_items ON tracks.TrackId = invoice_items.TrackId
JOIN 
    invoices ON invoice_items.InvoiceId = invoices.InvoiceId
GROUP BY 
    artists.ArtistId, artists.Name
ORDER BY 
    SUM(invoice_items.UnitPrice * invoice_items.Quantity) DESC
LIMIT 3


