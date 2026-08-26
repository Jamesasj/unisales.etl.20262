create database dw;

create schema stage;

CREATE TABLE stage.rent_usuarios (
	id INT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	email VARCHAR(150) NOT NULL UNIQUE,
	senha VARCHAR(255) NOT NULL,
	data_cadastro DATE NOT NULL
);

CREATE TABLE stage.sold_usuarios (
	id INT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	email VARCHAR(150) NOT NULL UNIQUE,
	data_cadastro DATE NOT NULL
);

create table stage.rent_filmes (
        id_filme INT primary key,
        titulo VARCHAR(200) NOT NULL,
        ano_lancamento INT NOT NULL,
        foreign key (id_filme) references stage.rent_filmes(id)
);

create table stage.imdb_ratings (
        id INT primary key,
        titulo VARCHAR(200) NOT NULL,
        rating DECIMAL(3,2) NOT NULL,
        url text NOT NULL,
        foreign key (id_filme) references stage.rent_filmes(id)
);