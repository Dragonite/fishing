Create database fishingPolls
user fishingPolls


PRINT '';
PRINT '***Creating users Table.....';
GO    

DROP TABLE IF EXISTS users;
Create table users()



PRINT '';
PRINT '***Creating polls Table.....';
GO    

DROP TABLE IF EXISTS polls;
Create table polls()





PRINT '';
PRINT '***Creating votes Table.....';
GO    

DROP TABLE IF EXISTS votes;
Create table votes()

PRINT '';
PRINT '***Creating voteXpoll Table.....';
GO    

DROP TABLE IF EXISTS voteXpoll;
Create table voteXpoll()



BULK INSERT [tablename] 
FROM 'file path'
with
(
    firstrow = 2,
    fieldterminator = ',',
	rowterminator='\n',
	ROWS_PER_BATCH =501
);
GO