drop table juegos
;
drop table biblioteca
;


INSERT INTO BIBLIOTECA(Rank, Name, Plataform, Year, Genre, Publisher, Rating) 
  VALUES(
          31, 
          (SELECT NAME FROM JUEGOS WHERE RANK=31),  
          (SELECT Plataform FROM JUEGOS WHERE RANK=31), 
          (SELECT Year FROM JUEGOS WHERE RANK=31), 
          (SELECT Genre FROM JUEGOS WHERE RANK=31), 
          (SELECT Publisher FROM JUEGOS WHERE RANK=31), 
          5
        );

INSERT INTO BIBLIOTECA(Rank, Name, Plataform, Year, Genre, Publisher, Rating) VALUES(31, 'eso', 'lksd', 1234, 'lqwk', 'lks', 5);

;

SELECT NAME FROM JUEGOS ORDER BY GLOBAL_SALES DESC 
FETCH FIRST 5 ROWS ONLY 

;

select * from v$version; 

SELECT * FROM JUEGOS 
;


INSERT INTO BIBLIOTECA(Rank, Name, Plataform, Year, Genre, Publisher, Rating) VALUES((SELECT Rank FROM JUEGOS WHERE NAME='Tetris'), 'Tetris',  (SELECT Plataform FROM JUEGOS WHERE NAME='Tetris'), (SELECT Year FROM JUEGOS WHERE NAME='Tetris'), (SELECT Genre FROM JUEGOS WHERE NAME='Tetris'), (SELECT Publisher FROM JUEGOS WHERE NAME='Tetris'), 2)
;

select name from juegos where name='Up' 

