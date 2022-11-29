drop database barbershop;
create database barbershop;
use barbershop;


CREATE TABLE books (
	ID INT NOT NULL AUTO_INCREMENT,
	Nombre varchar(75) NOT NULL,
	Author varchar(100) NOT NULL,
	PRIMARY KEY (ID)
);

describe books;

insert into books values
(1,'La familia de Pascual Duarte','Camilo Jose Cela'),
(2,'Bestiario','Julio Cortazar'),
(3,'Don Quijote de la Mancha','Miguel de Cervantes');

select * from books;