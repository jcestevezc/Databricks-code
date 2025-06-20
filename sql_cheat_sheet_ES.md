# SQL Cheat Sheet para Entrevistas

Este documento resume los comandos de SQL m\u00e1s comunes que suelen preguntarse en entrevistas de trabajo. Cada secci\u00f3n incluye la sintaxis b\u00e1sica y un ejemplo breve.

## Crear y modificar tablas

- **CREATE TABLE**: crea una tabla nueva.
  ```sql
  CREATE TABLE empleados (
      id INT PRIMARY KEY,
      nombre VARCHAR(100),
      salario DECIMAL(10,2)
  );
  ```
- **ALTER TABLE**: modifica la estructura de una tabla existente.
  ```sql
  ALTER TABLE empleados ADD COLUMN departamento VARCHAR(50);
  ```
- **DROP TABLE**: elimina por completo una tabla y su contenido.
  ```sql
  DROP TABLE empleados;
  ```

## Manipulación de datos

- **INSERT INTO**: agrega filas a una tabla.
  ```sql
  INSERT INTO empleados (id, nombre, salario)
  VALUES (1, 'Ana', 45000.00);
  ```

- **INSERT INTO ... SELECT**: copia datos de otra tabla.
  ```sql
  INSERT INTO empleados_historial
  SELECT * FROM empleados;
  ```

- **UPDATE**: actualiza valores existentes.
  ```sql
  UPDATE empleados
  SET salario = 48000.00
  WHERE id = 1;
  ```

- **DELETE**: elimina filas según una condición.
  ```sql
  DELETE FROM empleados WHERE id = 1;
  ```

## Consultas b\u00e1sicas

- **SELECT**: obtiene datos de una o m\u00e1s tablas.
  ```sql
  SELECT nombre, salario
  FROM empleados;
  ```
- **WHERE**: filtra resultados.
  ```sql
  SELECT *
  FROM empleados
  WHERE salario > 50000.00;
  ```
- **ORDER BY**: ordena los resultados.
  ```sql
  SELECT nombre, salario
  FROM empleados
  ORDER BY salario DESC;
  ```

## Filtrado avanzado y condicionales

- **LIKE (wildcards)**: busca coincidencias con `%` o `_`.
  ```sql
  SELECT nombre FROM empleados
  WHERE nombre LIKE 'A%';
  ```
- **IN**: especifica una lista de valores permitidos.
  ```sql
  SELECT * FROM empleados
  WHERE departamento IN ('Ventas', 'Marketing');
  ```
- **BETWEEN**: filtra un rango incluido.
  ```sql
  SELECT * FROM empleados
  WHERE salario BETWEEN 30000 AND 60000;
  ```
- **EXISTS**: verifica la existencia de filas en una subconsulta.
  ```sql
  SELECT nombre FROM empleados e
  WHERE EXISTS (SELECT 1 FROM departamentos d WHERE d.id = e.dep_id);
  ```
- **CASE**: aplica lógica condicional dentro de una consulta.
  ```sql
  SELECT nombre,
         CASE WHEN salario > 50000 THEN 'Alto' ELSE 'Medio' END AS rango_salario
  FROM empleados;
  ```

## Agregaci\u00f3n y agrupaci\u00f3n

- **GROUP BY**: agrupa datos para funciones de agregaci\u00f3n.
  ```sql
  SELECT departamento, AVG(salario) AS salario_promedio
  FROM empleados
  GROUP BY departamento;
  ```
- **HAVING**: filtra grupos resultantes.
  ```sql
  SELECT departamento, COUNT(*) AS total
  FROM empleados
  GROUP BY departamento
  HAVING COUNT(*) > 5;
  ```

## Uniones (JOIN)

- **INNER JOIN**: devuelve filas coincidentes en ambas tablas.
  ```sql
  SELECT e.nombre, d.nombre AS dep_nombre
  FROM empleados e
  INNER JOIN departamentos d ON e.dep_id = d.id;
  ```
- **LEFT JOIN**: devuelve todas las filas de la tabla de la izquierda y las que coinciden de la derecha.
  ```sql
  SELECT e.nombre, d.nombre AS dep_nombre
  FROM empleados e
  LEFT JOIN departamentos d ON e.dep_id = d.id;
  ```
- **UNION**: combina resultados de dos consultas.
  ```sql
  SELECT nombre FROM empleados_archivo
  UNION
  SELECT nombre FROM ex_empleados;
  ```


## Otras sentencias \u00fatiles

- **CREATE VIEW**: define una vista para simplificar consultas complejas.
  ```sql
  CREATE VIEW vista_empleados AS
  SELECT nombre, salario
  FROM empleados
  WHERE salario > 40000;
  ```
- **CREATE INDEX**: optimiza la b\u00fasqueda de datos.
  ```sql
  CREATE INDEX idx_salario ON empleados(salario);
  ```


## Funciones de ventana

- **ROW_NUMBER**: asigna un número secuencial dentro de un grupo.
  ```sql
  SELECT nombre,
         ROW_NUMBER() OVER (PARTITION BY departamento ORDER BY salario DESC) AS pos
  FROM empleados;
  ```
- **RANK**: calcula el rango dejando huecos para empates.
  ```sql
  SELECT nombre,
         RANK() OVER (ORDER BY salario DESC) AS rango
  FROM empleados;
  ```
- **LAG**: accede a la fila previa dentro del conjunto.
  ```sql
  SELECT nombre, salario,
         LAG(salario) OVER (ORDER BY salario) AS salario_anterior
  FROM empleados;
  ```

Este cheat sheet pretende ser un repaso r\u00e1pido de los comandos esenciales. Practicar su uso en ejemplos reales te ayudar\u00e1 a estar preparado para la entrevista.
