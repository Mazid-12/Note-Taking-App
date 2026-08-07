\c projects postgres
drop role note_user;
create role note_user createdb login password 'note';
drop database note_taker;
\c projets note_user


create database note_taker;



\c note_taker

create table users (id_user serial primary key, username varchar (50), password_hash text not null);
create table notes (id_notes serial primary key, id_user  integer references users(id_user), content text, dateCreation date default current_date);

insert into users (username, password_hash) values ('mazid', '2edcxwtgv');
insert into notes (id_user, content) values (1, 'I am very happy');