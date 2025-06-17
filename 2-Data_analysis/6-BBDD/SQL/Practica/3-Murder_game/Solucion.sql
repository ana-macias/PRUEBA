--Empiezo leyendo el informe,
SELECT *
FROM crime_scene_report
where city = 'SQL City'
group by type --está perdido

--Consulto la tabla con los detalles del crimen
SELECT *
FROM crime_scene_report
WHERE type = 'murder'
AND date = 20180115
AND city = 'SQL City'

--INFORME
--Security footage shows that there were 2 witnesses. 
--The first witness lives at the last house on "Northwestern Dr". 
--The second witness, named Annabel, lives somewhere on "Franklin Ave".

--Busco los testigos
--Primer testigo
SELECT *
FROM person
WHERE address_street_name = 'Northwestern Dr'
ORDER BY address_number DESC
LIMIT 1
--Se llama: MORTY SCHAPIRO id=14887

--Segundo testigo
SELECT *
FROM person
WHERE name LIKE '%Annabel%' AND address_street_name = 'Franklin Ave'
--Se llama ANNABEL MILLER id=16371

--Busco lo que ha dicho cada testigo
--MORTY SCHAPIRO
SELECT *
FROM interview
WHERE person_id = 14887
--I heard a gunshot and then saw a man run out. 
--He had a "Get Fit Now Gym" bag. 
--The membership number on the bag started with "48Z". 
--Only gold members have those bags. 
--The man got into a car with a plate that included "H42W".

--ANNABEL MILLER
SELECT *
FROM interview
WHERE person_id = 16371
--I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.

--Busco con las pistas MORTY el miembro 'Gold' del gimnasio que tiene un coche 
SELECT *
FROM get_fit_now_member
WHERE id LIKE '48Z%' AND membership_status = 'gold'
--Joe Germuska 28819 id gym=48Z7A y Jeremy Bowers 67318 id gym=48Z55

-- Busco con la pista del coche
SELECT person.name, drivers_license.*
FROM drivers_license 
JOIN person ON drivers_license.id = person.license_id
WHERE drivers_license.plate_number LIKE '%H42W%' AND person.id IN (28819, 67318)
------ME SALE JEREMY BOWERS------

--Confirmo con la pista de ANNABEL
SELECT *
FROM get_fit_now_check_in
WHERE membership_id IN ('48Z7A', '48Z55')
AND check_in_date = 20180109
--ME SALEN LOS DOS SOSPECHOSOS PERO SOLO JEREMY TIENE LA PLACA DEL COCHE CON LOS NÚMEROS QUE INDICA MORTY

-----ASESINO JEREMY BOWERS-----
--Pero en su confesion dice:
--I was hired by a woman with a lot of money. 
--I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). 
--She has red hair and she drives a Tesla Model S. 
--I know that she attended the SQL Symphony Concert 3 times in December 2017.

SELECT person.name, income.annual_income
FROM person 
JOIN drivers_license ON person.license_id = drivers_license.id
JOIN income ON person.ssn = income.ssn
WHERE drivers_license.gender = 'female'
AND drivers_license.hair_color = 'red'
AND drivers_license.height BETWEEN 65 AND 67
AND drivers_license.car_make = 'Tesla'
AND drivers_license.car_model = 'Model S'
ORDER BY income.annual_income DESC
LIMIT 1

-------LA VERDADERA ASESINA ES: MIRANDA PRIESTLY---------


