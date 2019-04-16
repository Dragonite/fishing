----How to run scripts
----install sqlite3
----execute sqlite3
----sqlite> .read DDL.sql



---Created by Luna
---Modified on 16.04.2019 by Luna




DROP TABLE IF EXISTS users;
Create table users(
    id INTEGER PRIMARY KEY,
    pollName Text NOT NULL
);

.schema users
