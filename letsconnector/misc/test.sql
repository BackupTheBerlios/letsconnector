create database lets_test;

use lets_test;

create table members
(
member_id int unsigned not null auto_increment primary key,
name char(128) not null,
address char(255) not null,
phone_number_1 char(20),
phone_number_2 char(20),
email_1 char(128),
email_2 char(128),
date_joined date not null,
date_left_or_dormant date,
next_renewal_date date,
status enum ("active", "dormant", "left", "other"),
notes char(255)
);