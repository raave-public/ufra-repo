-- Projeto criado por Luiz Felipe Araújo e disponibilizado no meu GitHub porque eu pretendo usá-lo de base para outros fins mais tarde.

CREATE TABLE Objetos_do_cenario (
    id_oc INT PRIMARY KEY,
    nome VARCHAR(100), 
    vegetacao INT,
    armadilhas INT,
    blocos INT
);

CREATE TABLE Cenario (
    id_cenario INT PRIMARY KEY,
    nome VARCHAR(100), 
    clima INT,
    atributo INT,
    tipo INT,
    id_objetos_cenario INT,
    FOREIGN KEY(id_objetos_cenario) REFERENCES Objetos_do_cenario(id_oc)
);

CREATE TABLE Itens (
    id_item INT PRIMARY KEY,
    nome VARCHAR(100), 
    tipo INT,
    forma INT,
    entrega INT
);

CREATE TABLE Jogador (
    id_jogador INT PRIMARY KEY,
    nome VARCHAR(100), 
    vida INT,
    dano INT,
    estado INT,
    bolsa INT,
    habilidades INT,
    id_cenario INT,
    id_objetos_cenario INT,
    id_itens INT,
    id_personagens INT,
    FOREIGN KEY(id_cenario) REFERENCES Cenario(id_cenario),
    FOREIGN KEY(id_objetos_cenario) REFERENCES Objetos_do_cenario(id_oc),
    FOREIGN KEY(id_itens) REFERENCES Itens(id_item)
);

CREATE TABLE Personagens (
    id_perso INT PRIMARY KEY,
    nome VARCHAR(100), 
    vida INT,
    tipo INT,
    caracteristicas INT,
    id_itens INT,
    id_objetos_cenario INT,
    FOREIGN KEY(id_itens) REFERENCES Itens(id_item)
);

CREATE TABLE Criaturas (
    id_cria INT PRIMARY KEY,
    nome VARCHAR(100), 
    vida INT,
    nivel INT,
    tipo INT,
    caracteristicas INT,
    armas INT,
    id_jogador INT,
    FOREIGN KEY(id_jogador) REFERENCES Jogador(id_jogador)
);

iNSERT INTO Objetos_do_cenario (id_oc, nome, vegetacao, armadilhas, blocos)
VALUES (1, 'Floresta', 20, 5, 10),
       (2, 'Caverna', 15, 3, 8),
       (3, 'Planície', 25, 7, 12);


INSERT INTO Cenario (id_cenario, nome, clima, atributo, tipo, id_objetos_cenario)
VALUES (1, 'Floresta Assombrada', 1, 2, 3, 1),
       (2, 'Montanhas Geladas', 2, 3, 1, 2),
       (3, 'Deserto Escaldante', 3, 1, 2, 3);


INSERT INTO Itens (id_item, nome, tipo, forma, entrega)
VALUES (1, 'Poção de Vida', 1, 2, 3),
       (2, 'Espada de Aço', 2, 3, 1),
       (3, 'Arco e Flecha', 3, 1, 2);


INSERT INTO Jogador (id_jogador, nome, vida, dano, estado, bolsa, habilidades, id_cenario, id_objetos_cenario, id_itens, id_personagens)
VALUES (1, 'Aventureiro1', 100, 20, 1, 50, 5, 1, 1, 1, 1);


INSERT INTO Personagens (id_perso, nome, vida, tipo, caracteristicas, id_itens, id_objetos_cenario)
VALUES (1, 'Guia', 80, 1, 10, 2, 2),
       (2, 'Mago', 90, 2, 8, 3, 3);


INSERT INTO Criaturas (id_cria, nome, vida, nivel, tipo, caracteristicas, armas, id_jogador)
VALUES (1, 'Lobo', 50, 10, 1, 5, 1, 1),
       (2, 'Dragão', 60, 8, 2, 7, 2, 1);