# Hemocentro - Gestão de Estoque de Sangue

![307550608-754dd79c-4266-4955-b564-7cc797cafdc5](https://github.com/LeviLucena/hemocentro/assets/34045910/88c6a127-a054-4b6f-9324-7783c84ab6ac)

Este é um projeto desenvolvido em Django para controle de estoque de sangue em hemocentros. O sistema permite o registro de estoques de sangue por tipo sanguíneo em diferentes hemocentros, além de fornecer funcionalidades como visualização de registros, geração de gráficos e exportação de dados.

## Funcionalidades

- Autenticação de usuários para acesso ao sistema.
- Registro de estoque de sangue por tipo sanguíneo e hemocentro.
- Visualização de registros em uma tabela interativa.
- Geração de gráficos para análise de estoque.
- Exportação de dados para formatos comuns.

## Galeria

| Imagem 1 | Imagem 2 | Imagem 3 | Imagem 4 |
| ---------| ---------| ---------| ---------|
|![image](https://github.com/LeviLucena/hemocentro/assets/34045910/4fc817d0-49e6-4fe0-9b70-af2f4d37e672) | ![image](https://github.com/LeviLucena/hemocentro/assets/34045910/e6600e99-27e5-416d-bedc-43dc4b074af2) | ![image](https://github.com/LeviLucena/hemocentro/assets/34045910/ae055f4d-2739-451f-8861-a425d69056e0) | ![image](https://github.com/LeviLucena/hemocentro/assets/34045910/fb67f57e-1787-4fae-8292-e3861d97a849)

## Instalação

1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/seu-usuario/estoque-sangue.git
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

- Criar tabelas e colunas de acordo com as regras de negócio do seu sistema.
- Criar superusuário de demais usuários genéricos para acessar o sistema.
- Criar grupos para gestão de acessos e permissionamentos.

## Tecnologias Utilizadas

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

