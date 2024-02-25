# Hemocentro - Gestão de Estoque de Sangue
#### (arquivos serão disponibilizados em breve)

![307550608-754dd79c-4266-4955-b564-7cc797cafdc5](https://github.com/LeviLucena/hemocentro/assets/34045910/88c6a127-a054-4b6f-9324-7783c84ab6ac)

Este é um projeto desenvolvido em Django com o objetivo de facilitar o controle de estoque de sangue em hemocentros. Com a crescente demanda por sangue e produtos sanguíneos, é crucial ter
um sistema eficiente para gerenciar o estoque e garantir a disponibilidade adequada para pacientes que necessitam de transfusões.

O sistema permite o registro detalhado dos estoques de sangue por tipo sanguíneo em diferentes hemocentros. Os usuários podem facilmente adicionar, atualizar e remover registros de estoque,
garantindo que as informações estejam sempre atualizadas e precisas.

Além disso, o sistema oferece uma variedade de funcionalidades adicionais para facilitar a gestão do estoque e a tomada de decisões informadas

Com essas funcionalidades integradas, o sistema de controle de estoque de sangue em hemocentros torna-se uma ferramenta poderosa para garantir a eficiência operacional e a disponibilidade
contínua de sangue para pacientes em necessidade.

## Funcionalidades

- Autenticação de usuários para acesso ao sistema.
- Registro de estoque de sangue por tipo sanguíneo e hemocentro.
- Visualização de registros em uma tabela interativa.
- Geração de gráficos para análise de estoque.
- Exportação de dados para formatos comuns.

## Galeria

| Imagem 1 | Imagem 2 | Imagem 3 | Imagem 4 | Imagem 5 | Imagem 6 | Imagem 7 |
| ---------| ---------| ---------| ---------| ---------| ---------| ---------|
| ![1](https://github.com/LeviLucena/hemocentro/assets/34045910/2460a12e-3b3d-4bfb-aa6a-5ae7577d3503) | ![2](https://github.com/LeviLucena/hemocentro/assets/34045910/38ef48b7-5a33-4d82-9492-012f1ad0626e) | ![3](https://github.com/LeviLucena/hemocentro/assets/34045910/a4ff15db-8cc7-4028-9341-30f9e4f78647) | ![4](https://github.com/LeviLucena/hemocentro/assets/34045910/ceb2d016-20a9-43ae-b1a9-13e2eefb5618) | ![5](https://github.com/LeviLucena/hemocentro/assets/34045910/17b1f603-6c3f-4626-a55d-b34240291119) | ![6](https://github.com/LeviLucena/hemocentro/assets/34045910/0e741f4c-7727-402e-921d-2261f99d2297) | ![7](https://github.com/LeviLucena/hemocentro/assets/34045910/dd5846d8-86f4-48e7-9545-fc4d1ec46869) |

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

