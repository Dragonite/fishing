----How to run scripts
----install sqlite3
----execute sqlite3 [databaseName]
----sqlite> .read DDL-tables.sql



---Created by Luna
---Modified on 16.04.2019 by Luna




DROP TABLE IF EXISTS users;
Create table users(
    userId integer PRIMARY KEY AUTOINCREMENT,
    email text NOT NULL,
    firstName text NOT NULL,
    lastName text,
   
    pwd text, 
   
    ad_street text,
    ad_suburb text, 
    ad_state text,

    createdAt datetime,
    isActive integer check(isActive IN(0,1))
);





DROP TABLE IF EXISTS polls;
Create table polls(
    pollId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title text,
    description text,
    
    openedAt datetime,
    closedAt datetime,
    completedAt datetime,
    
    totalCandidates integer NOT NULL ,
    createdByUserId integer NOT NULL,

    createdAt datetime NOT NULL ,
    
    isOpen integer NOT NULL check(isActive IN(0,1)),
    isActive integer NOT NULL check(isActive IN(0,1)),

    constraint fk_createdByUser
      foreign key(createdByUserId) references users(userId)
);

DROP TABLE IF EXISTS candidates;
Create table candidates(
    candidateId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    candidateDescription text,

    isActive integer NOT NULL check(isActive IN(0,1))
);

DROP TABLE IF EXISTS pollxCandidates;
Create table pollxCandidates(
    pollID integer ,
    candidateID integer, 

    constraint pf_pollxCandidates
      foreign key(pollID) references polls(pollId),
      foreign key(candidateID) references candidates(candidateId),
      primary key(pollID, candidateID)
);

DROP TABLE IF EXISTS responses;
Create table responses(

)


.tables
--.schema users
--.schema polls
--.schema candidates
