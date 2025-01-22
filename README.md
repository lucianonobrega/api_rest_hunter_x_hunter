<h1 align="center">API REST de Personagens - Hunter DB</h1>
<h2>Descrição</h2>
<p>Esta é uma API REST básica construída com Flask para manipulação de dados de personagens em um banco de dados MySQL. Ele fornece endpoints para listar todos os personagens, buscar um personagem por ID, adicionar, atualizar e excluir personagens.</p>
<h2>Pré-requisitos</h2>
<ul>
  <li>Python 3.x</li>
  <li>MySQL</li>
  <li>Flask</li>
  <li>MySQL Connector</li>
</ul>
<h2>Instalação</h2>
<ol>
  <li>Instale as dependências: Baixe o arquivo 'requirements.txt' e instale utilizando o comando: 'pip install -r requirements.txt' no seu terminal.</li>
  <p>OBS: É recomendável criar um ambiente virtual para instalar as dependências, pois as mesmas podem causar conflito com outras dependências já instaladas em sua máquina.</p>
  <li>Baixe o arquivo 'hunter_db.sql' e importe para dentro do seu MySQL.</li>
  <li>Baixe o arquivo 'main.py' no qual está o script da API e abra no seu editor de código.</li>
  <li>Agora basta dar 'run' no arquivo 'main.py'.</li>
</ol>
<h2>Acesso aos endpoints</h2>
<ul>
  <li>Listar todos os personagens: Método = [GET] | Endpoint = [/personagens]</li>
  <li>Buscar um personagem por ID: Método = [GET] | Endpoint = [/personagens/id]</li>
  <li>Adicionar um novo personagem: Método = [POST] | Endpoint = [/personagens]</li>
  <li>Atualizar um personagem existente: Método = [PUT] | Endpoint = [/personagens/id]</li>
  <li>Excluir um personagem: Método = [DELETE] | Endpoint = [/personagens/id]</li>
</ul>
