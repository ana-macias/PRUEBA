use('empleados')

/*Devuelve todas las empleadas de la empresa usando $match*/
db.empleados.aggregate([
  {
    $match: {
      gender: "female"  // Filtra solo los documentos donde gender sea 'female'
    }
  }
])

/*Devuelve un array de objetos que tenga en cada uno {id_departamento,totalEmployees}
datos como en el siguiente ejemplo:
[
  { _id: 'Marketing', totalEmployees: 2},
  { _id: 'HR', totalEmployees: 2},
  { _id: 'Finance', totalEmployees: 3}
]*/
db.empleados.aggregate([
  {
    $group: {
      _id: "$department.name",  // Agrupa por el nombre del departamento
      totalEmployees: { $sum: 1 }  // Cuenta los empleados en cada grupo
    }
  },
  {
    $project: {
      _id: 1,
      totalEmployees: 1
    }
  }
])

/*Modifica el ejercicio anterior para que sólo devuelva datos de los empleados*/
db.empleados.aggregate([
  {
    $group: {
      _id: "$department.name",
      employees: { 
        $push: "$$ROOT"  // Guarda el documento completo de cada empleado
      }
    }
  }
])

/*Devuelve los datos de las empleadas ordenados por salario ascendente*/
db.empleados.find(
  { gender: "female" },          // Filtra solo empleadas
  { _id: 0, department: 0 }      // Opcional: excluye campos no necesarios
).sort(
  { salary: 1 }                  // Ordena por salario ascendente (1: ascendente, -1: descendente)
)

/*Devuelve los datos de las empleadas por departamento ordenados por total salario ascendente 
para sacar una salida parecida a:
[
  { _id: { deptName: 'Finance' }, totalEmployees: 2, totalSalaries: 12500},
  { _id: { deptName: 'HR' }, totalEmployees: 1, totalSalaries: 10000},
  { _id: { deptName: 'Marketing' }, totalEmployees: 2, totalSalaries: 5000}
]*/
db.empleados.aggregate([
  { 
    $match: { 
      gender: "female"  // Filtra solo empleadas (gender: 'female')
    } 
  },
  { 
    $group: { 
      _id: { 
        deptName: "$department.name"  // Agrupa por nombre del departamento
      }, 
      totalEmployees: { $sum: 1 },    // Cuenta empleadas por departamento
      totalSalaries: { $sum: "$salary" }  // Suma los salarios por departamento
    } 
  },
  { 
    $sort: { 
      totalSalaries: 1  // Ordena por totalSalaries ascendente (1: menor a mayor)
    } 
  }
])
