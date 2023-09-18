import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


#1- cursor.execute('CREATE TABLE alunos(id INT PRIMARY KEY,nome VARCHAR(100),idade INT, curso VARCHAR(100));')

#2- cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1,"Miliana",29,"Python"),(2,"Carol",30,"Python"),(3,"José",25,"Dados"),(4,"João",31,"Dados"),(5,"Pedro",32,"Engenharia")')


#3 - Consultas básicas
#a) Selecionar todos os registros da tabela "alunos".

# R: dados = cursor.execute('SELECT * FROM alunos')

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos

# R: dados = cursor.execute('SELECT nome, idade from alunos WHERE idade > 20')

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética

#R: dados = cursor.execute('SELECT * FROM alunos Where curso = "Engenharia" ORDER BY nome')

#d) Contar o número total de alunos na tabela

#R: dados = cursor.execute('SELECT count(*) FROM alunos')

#4- Atualização e Remoção

#a)Atualize a idade de um aluno especifico na tabela

#R: dados = cursor.execute('UPDATE alunos SET idade = 28 WHERE id=2')

#b)Remova um aluno pelo seu ID

#R: dados = cursor.execute('DELETE FROM alunos WHERE id = 5')

#5-Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada 'clientes' com os campos:
#id(chave primaria),nome(Varchar), idade(int) e saldo(float)
#Insira alguns registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY,nome VARCHAR(100),idade INT, saldo float);')
#R: dados = cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES (1,"Miliana",29,2500.0),(2,"Lucas",20,1000.0),(3,"Liz",20,5000.0),(4,"Carlos",30,10500.0)')

# 6-Consultas e Funções Agregadas/ Escreva consultas SQL para realizar as seguintes tarefas:
#a)Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#R: dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade >= 30 ')

#b)Calcule o saldo médio dos clientes.

#R: dados = cursor.execute('SELECT AVG(saldo) FROM clientes')

#c)Encontre o cliente com o saldo máximo

#R: dados= cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')

#d)Conte quantos clientes têm saldo acima de 1000.

#R: dados = cursor.execute('SELECT count(*) FROM clientes WHERE saldo >= 1.000')

#7 -Atualização e remoção  com condições

#a)Atualize o saldo de um cliente específico

#R:dados = cursor.execute('UPDATE clientes SET saldo = 6000 WHERE id = 4')

#b)Remova um cliente pelo seu ID.

#R: dados = cursor.execute('DELETE FROM Clientes WHERE id = 3')

#Junção de Tabelas
# 8- Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o idda tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra

#R: dados = cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY,cliente_id,produto VARCHAR,valor real, CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id));')

#R: dados = cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1,1, "Mochila",320.0),(2,1,"Caneta",15.50),(3,2,"Caderno",25.0)')

#c- clientes co- compras

#R: dados = cursor.execute('SELECT c.nome, co.produto, co.valor from compras as co INNER JOIN clientes as c on c.id = co.cliente_id')

#for alunos in dados:
# print(alunos)


conexao.commit()
conexao.close()
