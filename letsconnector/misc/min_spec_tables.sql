
drop database if exists lets_test;

create database lets_test;

use lets_test;

#This is how to create the user for the web software:
#GRANT select, insert, delete, update ON lets_test.* TO 'lets'@'localhost' IDENTIFIED BY 'monkeys';

create table members
(
member_id int unsigned not null primary key,
date_joined date not null,
notes char(255)
);

create table trades
(
trade_id int unsigned not null auto_increment primary key,
date_of_trade datetime not null,
member_id_entered_by int unsigned not null,
amount int unsigned not null,
member_id_from int unsigned not null,
member_id_to int unsigned not null,
description char(255)
);

create table members_change_log
(
members_change_id int unsigned not null auto_increment primary key,
date_changed date not null,
member_id_entered_by int unsigned not null,
member_id_changed int unsigned not null,
change_description char(255)
);
