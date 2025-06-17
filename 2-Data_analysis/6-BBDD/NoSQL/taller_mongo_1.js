use ('taller_mongo')

/*db.clientes.find(
    {telefono:{$eq:[]},compras:{$eq:[]}}
)

db.clientes.find(
    {telefono:{$eq:[]},compras:{$eq:[]}}
)*/

/*db.clientes.find(
        {
            'direcciones.ciudad':'Barcelona',
            $or:[
                {telefono:{$eq:[]}},
                {compras:{$eq:[]}}
            ]
        }
)*/

/*db.clientes.find(
).sort(
    { nombre: 1 }
)*/

db.clientes.aggregate([
  //{ $match: {} }, // (1) Opcional: filtra documentos (aquí no filtramos nada)
    { $unwind: "$direcciones" },
    { $group: { _id: "$direcciones.ciudad", totalClientes: { $sum: 1 } } }, // (2) Agrupar por ciudad
    { $sort: { totalClientes: 1 } } // (3) Ordenar de mayor a menor

])

