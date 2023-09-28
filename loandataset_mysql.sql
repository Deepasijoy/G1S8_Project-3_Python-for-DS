create database session_register_user_details;
use session_register_user_details;
create table Users (user_id int NOT NUll auto_increment,user_name varchar(80),
password varchar(20),primary key(user_id));
use session_register_user_details;
select * from Users;