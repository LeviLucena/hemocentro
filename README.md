# Hemocentro - Gestão de Estoque de Sangue
#### (arquivos serão disponibilizados em breve)

![307550608-754dd79c-4266-4955-b564-7cc797cafdc5](https://github.com/LeviLucena/hemocentro/assets/34045910/88c6a127-a054-4b6f-9324-7783c84ab6ac)

Este é um projeto desenvolvido em Django para controle de estoque de sangue em hemocentros. O sistema permite o registro de estoques de sangue por tipo sanguíneo em diferentes hemocentros, além de fornecer funcionalidades como visualização de registros, geração de gráficos e exportação de dados.

## Funcionalidades

- Autenticação de usuários para acesso ao sistema.
- Registro de estoque de sangue por tipo sanguíneo e hemocentro.
- Visualização de registros em uma tabela interativa.
- Geração de gráficos para análise de estoque.
- Exportação de dados para formatos comuns.

## Galeria

| Imagem 1 | Imagem 2 | Imagem 3 | Imagem 4 | Imagem 5 |
| ---------| ---------| ---------| ---------| ---------|
|![image](https://github.com/LeviLucena/hemocentro/assets/34045910/2ed820a3-38d8-40a2-9cb1-0a5ecc9457cf) | ![image](https://github.com/LeviLucena/hemocentro/assets/34045910/81c95146-698f-4a19-80d2-4c366c803cc4) | ![image](https://github.com/LeviLucena/hemocentro/assets/34045910/a6ffcddf-fa8b-4a71-8169-d20f401e4725) | ![image](https://github.com/LeviLucena/hemocentro/assets/34045910/7ec32685-e46b-41ce-87bf-486daf240442) | ![image](https://github.com/LeviLucena/hemocentro/assets/34045910/372856b0-19b7-44ee-85ad-6dbaf8c292f1) |


## Instalação

1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/LeviLucena/hemocentro.git
```

2. Navegue até o diretório do projeto:

```
cd estoque-sangue
```

3. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

4. Execute as migrações do banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

6. Acesse o sistema no seu navegador através do endereço [http://localhost:8000/](http://localhost:8000/).

7. Para acessar o banco de dados Django, utilize o endereço [http://localhost:8000/admin](http://localhost:8000/admin).

Crie um superusuário: Antes de acessar a interface administrativa, certifique-se de que você tenha um superusuário criado para acessar o admin do Django. Se você ainda não criou um, pode fazer isso 
executando o comando ```python manage.py createsuperuser``` no terminal e seguir as instruções.

Com isto será possível:

- Criar tabelas e colunas de acordo com as regras de negócio do seu sistema.
- Criar superusuário de demais usuários genéricos para acessar o sistema.
- Criar grupos para gestão de acessos e permissionamentos.

## Tecnologias Utilizadas

- Anaconda: Distribuição gratuita e de código aberto da linguagem de programação Python, que oferece uma maneira eficiente de gerenciar pacotes e ambientes virtuais
- Django: Framework web em Python para desenvolvimento rápido e limpo.
- Bootstrap: Framework front-end para criação de interfaces responsivas.
- DataTables: Plugin jQuery para manipulação de tabelas HTML.
- Chart.js: Biblioteca JavaScript para geração de gráficos interativos.
- jQuery: Biblioteca JavaScript para manipulação de documentos HTML.

## Contribuições

Contribuições são bem-vindas! Se você tiver ideias de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma nova issue ou enviar um pull request.
Licença. Este projeto é licenciado sob a licença MIT. Você é livre para usar, modificar e distribuir o código conforme necessário.

Espero que isso ajude a descrever seu projeto de Gestão de Equipamentos de TI para o GitHub. Boa sorte com o seu projeto!

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Autor: [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/levilucena/)](https://www.linkedin.com/in/levilucena/)

