drop table d_user;

create table d_user(
    id serial primary key,
    nome varchar(255) not null,
    email varchar(255) not null,
    tp_user varchar(50) not null,
    source_id varchar(255)
);
