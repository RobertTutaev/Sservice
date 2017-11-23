create database if not exists app;

use app;

create table s_db(
    id integer primary key auto_increment,
    name varchar(100) unique not null,
    p_host varchar(255) not null,
    p_name varchar(255) not null,
    p_username varchar(100) not null,
    p_password varchar(100) not null,
    comment text,
    checked tinyint(1) DEFAULT 1
)engine=innodb;

create table s_auth_user_db(
    id integer primary key auto_increment,
    auth_user_id integer not null,
    s_db_id integer not null,
    index fk_saudb_user (auth_user_id ASC),
    constraint fk_saudb_user
        foreign key (auth_user_id)
            references auth_user (id)
                on delete CASCADE,
    index fk_saudb_db (s_db_id ASC),
    constraint fk_saudb_db
        foreign key (s_db_id)
            references s_db (id)
                on delete CASCADE
)engine=innodb;

create table s_service(
    id integer primary key auto_increment,
    name varchar(100) unique not null,
    comment text,
    checked tinyint(1) DEFAULT 1
)engine=innodb;

create table s_auth_user_service(
    id integer primary key auto_increment,
    auth_user_id integer not null,
    s_service_id integer not null,
    index fk_sausr_user (auth_user_id ASC),
    constraint fk_sausr_user
        foreign key (auth_user_id)
            references auth_user (id)
                on delete CASCADE,
    index fk_sausr_service (s_service_id ASC),
    constraint fk_sausr_service
        foreign key (s_service_id)
            references s_service (id)
                on delete CASCADE
)engine=innodb;

create table s_type(
    id integer primary key auto_increment,
    name varchar(255) unique not null
)engine=innodb;

create table s_query(
    id integer primary key auto_increment,
    name varchar(255) unique not null,
    s_service_id integer not null,
    script text,
    priority integer not null,
    comment text,
    s_type_id integer not null,
    result varchar(255),
    index fk_sqr_service (s_service_id ASC),
    constraint fk_sqr_service
        foreign key (s_service_id)
            references s_service (id)
                on delete CASCADE,
    index fk_sqr_type (s_type_id ASC),
    constraint fk_sqr_type
        foreign key (s_type_id)
            references s_type (id)
                on delete RESTRICT on update RESTRICT
)engine=innodb;

create table s_log(
    id integer unsigned primary key auto_increment,
    info text,
    dt datetime default CURRENT_TIMESTAMP
)engine=innodb;

insert into s_db(name, p_host, p_name, p_username, p_password, comment) values 
    ('БД Калининского УСЗН',        '172.153.153.104\MINSOC_DB_SQL', 'NDA_CHEL_KALIL_201709',   'sa', 'FREIDER5', 'Id=214'),
    ('БД Курчатовского УСЗН',       '172.153.153.104\MINSOC_DB_SQL', 'NDA_CHEL_KURCH_201709',   'sa', 'FREIDER5', 'Id=219'),
    ('БД Ленинского УСЗН',          '172.153.153.104\MINSOC_DB_SQL', 'NDA_CHEL_LENIN_201709',   'sa', 'FREIDER5', 'Id=195'),
    ('БД Металлургического УСЗН',   '172.153.153.104\MINSOC_DB_SQL', 'NDA_CHEL_METALL_201709',  'sa', 'FREIDER5', 'Id=200'),
    ('БД Советского УСЗН',          '172.153.153.104\MINSOC_DB_SQL', 'chel_SOVET_20170922',     'sa', 'FREIDER5', 'Id=160'),
    ('БД Тракторозаводского УСЗН',  '172.153.153.104\MINSOC_DB_SQL', 'NDA_CHEL_TRACK_201709',   'sa', 'FREIDER5', 'Id=191'),
    ('БД Центрального УСЗН',        '172.153.153.104\MINSOC_DB_SQL', 'NDA_CENTR_201709_2',      'sa', 'FREIDER5', 'Id=234');

insert into s_type(name) values
    ('Данные из выборки'),
    ('Данные из значения при условии, что первое поле выборки больше 0'),
    ('Данные из значения при условии, что записей в выборке больше 0');

insert into s_service(name, comment) values
    ('Проезд', 'Проезд в муниципальном общественном транспорте города Челябинска');