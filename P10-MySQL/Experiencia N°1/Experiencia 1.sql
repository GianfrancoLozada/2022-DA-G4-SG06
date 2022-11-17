CREATE DATABASE prueba; 
Use prueba; 
CREATE TABLE classics( 
autor VARCHAR(128), 
title VARCHAR(128), 
typ VARCHAR(16), 
year CHAR(4) 
); 
Describe classics; 
Alter table classics ADD ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY; 
Describe classics; 
Alter table classics drop ID; 
INSERT INTO classics(autor, title, typ, year) VALUES('Mark Twain','The Adventures of Tom Sawyer','Fiction','1876'); 
INSERT INTO classics(autor, title, typ, year) VALUES('Jane Austen','Pride and Prejudice','Fiction','1811'); 
INSERT INTO classics(autor, title, typ, year) VALUES('Charles Darwin','The Origin of Species','Non- Fiction','1856'); 
INSERT INTO classics(autor, title, typ, year) VALUES('Charles Dickens','The Old Curiosity Shop','Fiction','1841'); 
INSERT INTO classics(autor, title, typ, year) VALUES('William Shakespeare','Romeo and Juliet','Play','1594'); 
SELECT *FROM classics;
ALTER TABLE classics RENAME pre1900; 
ALTER TABLE pre1900 MODIFY year SMALLINT; 
ALTER TABLE pre1900 ADD INDEX(autor(20)); 
ALTER TABLE pre1900 ADD INDEX(title(20)); 
ALTER TABLE pre1900 ADD INDEX(typ(4)); 
ALTER TABLE pre1900 ADD INDEX(year); 