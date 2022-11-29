delimiter $$
create procedure usp_insertar_books(
title varchar(50),
author varchar(200),
publicado varchar(200))
begin
insert into books(book_title,book_author,book_published)
values(title,author,publicado);
end;

call usp_insertar_books('NODE USO DE SERVICIOS','ARMANDO RUIZ','27/03/202');
call usp_listar_books();