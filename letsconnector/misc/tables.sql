create database lets_test;

use lets_test;

create table members
(
member_id int unsigned not null auto_increment primary key,
sha1_password char(40),
date_joined date not null,
date_left_or_dormant date,
next_renewal_date date,
status enum ("active", "dormant", "left", "other"),
notes char(255)
);

create table trades
(
trade_id int unsigned not null auto_increment primary key,
date_entered date not null,
date_of_trade date not null,
member_id_entered_by int unsigned not null,
statement_date date not null,
amount int unsigned not null,
member_id_from int unsigned not null,
member_id_to int unsigned not null,
is_this_a_cheque enum ("cheque", "not_a_cheque"),
service int unsigned not null,
description char(255)
);

create table services
(
service_id int unsigned not null auto_increment primary key,
name char(32) not null,
description char(128)
);

create table wants_and_offers
(
want_offer_id int unsigned not null auto_increment primary key,
member_id int unsigned not null,
service_id int unsigned not null,
date_added date not null,
permanent enum ("permanent", "not_permanent"),
expiry_date date,
description char(255),
want_or_offer enum ("want", "offer", "want_and_offer", "other")
);

create table members_change_log
(
members_change_id int unsigned not null auto_increment primary key,
date_changed date not null,
member_id_entered_by int unsigned not null,
member_id_changed int unsigned not null,
change_description char(255)
);

create table wants_and_offers_change_log
(
wants_and_offers_change_id int unsigned not null auto_increment primary key,
date_changed date not null,
member_id_entered_by int unsigned not null,
member_id_changed int unsigned not null,
change_description char(255)
);
