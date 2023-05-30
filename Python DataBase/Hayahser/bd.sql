create table articulos(
    codigo Serial not null unique,
    nombre text,
    precio float,
    tipo text

)

INSERT INTO articulos(codigo, nombre, precio , tipo)
VALUES (001, 'Manzana', '2.50', 'Fruta');

INSERT INTO articulos(codigo, nombre, precio , tipo)
VALUES (002, 'Uva', '4.50', 'Fruta');

SELECT * FROM articulos;


