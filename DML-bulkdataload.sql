
insert into users(logInId, firstName, lastName, email, createdAt, isActive, isAdmin)
values('Luna', 'Luna','Lee', '22187554@student.uwa.edu.au',datetime('now'), 1,1 );

insert into users(logInId,firstName, lastName, email, createdAt, isActive, isAdmin)
values('Haolin','Haolin', 'Woo', '21706137@student.uwa.edu.au',datetime('now'), 1,1 );

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Maybelle','Maybelle',	'Bewley',   'cgrafenstein@gmail.com',	        'Dennison St',	        'Herron',	        'Western Australia',datetime('now'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Mayra',	'Mayra','Bena', 	'idella@hotmail.com',               '',	                    'Nedlands',	        'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Mariko','Mariko',	'Stayer',	    'leatha_block@gmail.com',	    'Sylvan Ave',       	'Nyamup',	        'Western Australia',  datetime('
'), 1);


insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Carlota',	'Carlota','Gephardt', 	'serita_barthlow@gmail.com',	'Market St',        	'Dartnall',	        'Western Australia',  datetime('
'), 1);


insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Gwen',	 'Gwen',   'Julye',	    'csoros@gmail.com',	            '',                  	'Kealy',	    'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Marica',	'Marica','Tarbor',	    'delfina_binnie@binnie.net.au',	'Fiesta Blvd',	        'East Newdegate',	'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Nadine','Nadine',	'Okojie',   	'rachael@gmail.com',        	'Blackington Ave',	    'North Cascade',	'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Roy',	'Roy',    'Nybo',     	'nadine.okojie@okojie.com.au',	'S Central Expy',	    'Stirling Range National Park',	'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Emelda','Emelda',	'Geffers',  	'jarvis@gmail.com',         	'Cherokee St',	        'Bobalong',	        'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Janessa',	'Janessa','Ruthers',  	'ycarabajal@carabajal.com.au',	'Aquarium Pl',       	'Ongerup',	        'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Reita',	'Reita','Tabar',	    'rosendo_jelsma@hotmail.com',	'S University Blvd',	    'Guildford',    	'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Rebbecca',	'Rebbecca','Didio',    	'laurene_bennett@gmail.com',	'Schoenborn St',	        'Hamel',    	'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Dexter','Dexter',	'Prosienski',	'bettyann@fernades.com.au',     'Park Pl',	            'FORRESTDALE',  	'Western Australia',  datetime('
'), 1);

insert into users(logInId,firstName, lastName, email, ad_street, ad_suburb, ad_state, createdAt, isActive)
values('Rosina','Rosina',	'Sidhu',     	'clare_bortignon@hotmail.com',  'State St',          	'Boya',	            'Western Australia',  datetime('
'), 1);





-----------------------------------------------------------------------------------------------------------

insert into polls(title, description, openedAt, totalCandidates, createdByUserId, createdAt, isOpenPoll, isActive, orderCandidatesBy)
values('where is your favorite fishing spot?','survey to find out perth best fishing spot', datetime('now'),  5, 12, datetime('now'),1,1, 'SpecialOrder');


------------------------------------------------------------------------------------------------------------

insert into candidates(candidateDescription, isActive, displayOrder)
values('Narrows Bridge Perth', 1, 3);

insert into candidates(candidateDescription, isActive, displayOrder)
values('White Hills Mandurah', 1, 2);

insert into candidates(candidateDescription, isActive, displayOrder)
values('North Mole Fremantle', 1, 1);

insert into candidates(candidateDescription, isActive, displayOrder)
values('Floreat Drain Floreat', 1, 4);

insert into candidates(candidateDescription, isActive, displayOrder)
values('Ricey Beach And Radar Reef Rottnest Island', 1, 5);

insert into candidates(candidateDescription, isActive, displayOrder)
values('Lancelin Jetty Lancelin', 1, 6);


----------------------------------------------------------------------------------------

insert into pollxCandidates(pollId, candidateId)
values(1,1);

insert into pollxCandidates(pollId, candidateId)
values(1,2);

insert into pollxCandidates(pollId, candidateId)
values(1,3);

insert into pollxCandidates(pollId, candidateId)
values(1,4);

insert into pollxCandidates(pollId, candidateId)
values(1,5);

insert into pollxCandidates(pollId, candidateId)
values(1,6);

----------------------------------------------------------------
insert into responses(userId, pollId, candidateId, response, createdAt)
values(3,1,1,2, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(3,1,2,1, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(3,1,3,3, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(3,1,4,5, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(3,1,5,4, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(3,1,6,6, datetime('now'));



insert into responses(userId, pollId, candidateId, response, createdAt)
values(4,1,1,6, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(4,1,2,2, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(4,1,3,3, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(4,1,4,4, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(4,1,5,1, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(4,1,6,5, datetime('now'));


insert into responses(userId, pollId, candidateId, response, createdAt)
values(5,1,1,5, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(5,1,2,3, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(5,1,3,2, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(5,1,4,1, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(5,1,5,4, datetime('now'));
insert into responses(userId, pollId, candidateId, response, createdAt)
values(5,1,6,6, datetime('now'));