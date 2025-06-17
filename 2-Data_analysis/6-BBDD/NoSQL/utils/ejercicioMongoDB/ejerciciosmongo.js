use ('Restaurantes')

/*Mostrar todos los documentos de la colección restaurantes*/
db.getCollection('Restaurantes').find({});

/*Mostrar los campos restaurant_id, nombre, distrito y cocina, pero excluya el campo _id para todos los documentos de la colección restaurantes*/
db.Restaurantes.find(
    {}, 
    { _id: 0,            // Sin el campo _id
      restaurant_id: 1,  // restaurant_id
      name: 1,           // nombre
      borough: 1,        // distrito
      cuisine: 1         // cocina
    }
)

/*Mostrar los primeros 5 restaurantes que se encuentran en el distrito Bronx*/
db.Restaurantes.find(
  { distrito: "Bronx" },  // Filtro para seleccionar solo restaurantes del Bronx
  { 
    _id: 0,              
    restaurant_id: 1,    
    name: 1,           
    borough: 1,         
    cuisine: 1           
  }
).limit(5)               // Los 5 primeros resultados


/*Devolver los restaurantes que lograron una puntuación superior a 80 pero inferior a 100*/
db.Restaurantes.find(
  {
    "grades": {
      $elemMatch: { score: { $gt: 80, $lt: 100 } }
    }
  },
  {
    _id: 0,
    name: 1,
    borough: 1,
    cuisine: 1,
    "grades.score": 1  // Sólo el score de los que cumplen
  }
)

/*Devolver los restaurantes que se ubican en un valor de latitud inferior a -95.754168*/
db.Restaurantes.find(
  {
    "address.coord.0": { $lt: -95.754168 }  // Longitud < -95.754168
  },
  {
    _id: 0,                 
    name: 1,                
    borough: 1,              
    cuisine: 1,              
    "address.coord": 1        // Mostrar las coordenadas
  }
)

/*Devolver los restaurantes que no preparan cocina americana y lograron una puntuación superior a 70 y
se ubicaron en una longitud inferior a -65.754168. Nota: Realice esta consulta sin usar el operador $and*/
db.Restaurantes.find(
  {
    "cuisine": { $ne: "American" },            
    "grades.score": { $gt: 70 },               
    "address.coord.0": { $lt: -65.754168 }     // Longitud < -65.754168
  },
  {
    _id: 0,                                   // Excluir _id
    name: 1,                                  // Mostrar nombre
    cuisine: 1,                               // Mostrar tipo de cocina
    "grades.score": 1,                        // Mostrar puntuación
    "address.coord": 1                        // Mostrar coordenadas
  }
)

/*Devolver los restaurantes que no preparan cocina americana y 
lograron un punto de calificación 'A' que no pertenece al distrito de Brooklyn. 
El documento debe mostrarse según la cocina en orden descendente.*/
db.Restaurantes.find(
  {
    "cuisine": { $ne: "American" },  
    "grades.grade": "A",             
    "borough": { $ne: "Brooklyn" }   
  },
  {
    _id: 0,                          
    name: 1,                         
    cuisine: 1,                      
    borough: 1,                     
    "grades.grade": 1                
  }
).sort({ cuisine: -1 })              // (descendente)

/*Devolver los restaurantes que pertenecen al distrito Bronx y preparan platos americanos o chinos*/
db.Restaurantes.find(
  {
    "borough": "Bronx",  // Pertenece al distrito Bronx
    "cuisine": { $in: ["American", "Chinese"] }  // Cocina americana o china
  },
  {
    _id: 0,              
    name: 1,             
    borough: 1,        
    cuisine: 1,          
    address: 1           
  }
)
/*Devolver ID del restaurante, nombre, distrito y la cocina para aquellos restaurantes
 que pertenecen al distrito de Staten Island o Queens o Bronx o Brooklyn*/
 db.Restaurantes.find(
  {
    "borough": { 
      $in: ["Staten Island", "Queens", "Bronx", "Brooklyn"] 
    }
  },
  {
    _id: 0,                   
    restaurant_id: 1,        
    name: 1,                 
    borough: 1,               
    cuisine: 1                
  }
)

/*Devolver ID del restaurante, nombre, distrito y la cocina de aquellos restaurantes que lograron una puntuación que no supere los 10*/
db.Restaurantes.find(
  {
    "grades.score": { $lte: 10 }  // Puntuación menor o igual a 10
  },
  {
    _id: 0,                      
    restaurant_id: 1,            
    name: 1,                     
    borough: 1,                  
    cuisine: 1,                  
    "grades.score": 1            
  }
)

/*Devolver ID del restaurante, el nombre y las calificaciones del restaurante para 
aquellos restaurantes que obtuvieron una calificación de "A" y obtuvieron un puntaje de 11 en una fecha ISO "2014-08-11T00: 00: 00Z" 
entre muchas fechas de encuesta*/
db.Restaurantes.find(
  {
    "grades": {
      $elemMatch: {
        grade: "A",
        score: 11,
        date: ISODate("2014-08-11T00:00:00Z")
      }
    }
  },
  {
    _id: 0,
    restaurant_id: 1,
    name: 1,
    grades: {
      $filter: {
        input: "$grades",
        as: "grade",
        cond: {
          $and: [
            { $eq: ["$$grade.grade", "A"] },
            { $eq: ["$$grade.score", 11] },
            { $eq: ["$$grade.date", ISODate("2014-08-11T00:00:00Z")] }
          ]
        }
      }
    }
  }
)

/*Devolver ID del restaurante, nombre, dirección y ubicación geográfica del restaurante de 
aquellos donde el segundo elemento de la matriz coord contiene un valor que es más de 42 y hasta 52*/
db.Restaurantes.find(
  {
    "address.coord.1": { 
      $gt: 42,   // Mayor que 42
      $lte: 52   // Menor o igual que 52
    }
  },
  {
    _id: 0,                      
    restaurant_id: 1,            
    name: 1,                    
    "address.building": 1,       // Número del edificio
    "address.street": 1,         // Calle
    "address.zipcode": 1,        // Código postal
    "address.coord": 1           // Coordenadas [longitud, latitud]
  }
)

/*Crea un par de restaurantes que te gusten. Tendrás que buscar en Google Maps los datos de las coordenadas*/

/*Actualiza los restaurantes. Cambia el tipo de cocina 'Ice Cream, Gelato, Yogurt, Ices' por 'sweets'*/

/*Actualiza nombre del restaurante 'Wild Asia' por 'Wild Wild West'*/

/*Borra los restaurantes con latitud menor que -95.754168*/

/*Borra los restaurantes cuyo nombre empiece por 'C'*/

