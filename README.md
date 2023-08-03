# BackEnd Credit Card Registration CRUD

I used FastAPI, for all its ease of structuring, ease of integrating other frameworks and its ease of scalability.
I used NextJS as a frontend framework because it is robust, scalable

 A backend application with user authentication for register credit cards using FastApi and UnitTests

- FastAPI. Docs [here](https://fastapi.tiangolo.com)

## Features

- User Registration: Users can create an account.
- User Login: Users can log in to their accounts.
- Role-based Authentication: Three roles with different permission levels - regular user, user manager, admin.
- User and Manager: User and managers can CRUD users and Register Credit Cards.
- Admin: Admins can CRUD all records and users, register, list, get, Delete Credit Cards.
- JSON API: Data is returned in JSON format.
- Unit and E2E Tests: Includes unit tests and end-to-end tests.
- Python Web Framework: Uses any Python web framework.
- Postgres Database: Uses Postgres Docker as the database.

## Get Started

#### Clone the repository

```shell
    git clone https://github.com/orochidrake/credit-card-core
    git clone https://github.com/orochidrake/credit-card-web
```

#### Install the required dependencies

```shell
    pip install -r requirements.txt
```

#### Run Postgres Docker Container for DataBase

```shell
    docker-compose up --build -d
```

#### Set up the database with sqlite

```shell
    python create_db.py
```

#### Run the application

Application will be exposed to port 8000 on <http://localhost:8000/>

```shell
    python main.py
```

#### Create Admin user

Use the culr to create a Admin User

```
curl --request POST \
  --url <http://localhost:8000/api/v1/signup/> \
  --header 'Content-Type: application/json' \
  --data '{
 "fullname": "Fulano",
 "email": "<fulano@gmail.com>",
 "password": "fulanopass",
 "role": "admin"
}'
```

#### Curls

Curl to create a credit card

```
curl --request POST \
  --url <http://localhost:8000/api/v1/credit-card> \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VyX25hbWUiOiJGdWxhbm8iLCJ1c2VyX2VtYWlsIjoiZnVsYW5vQGZ1bGFuMi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHBpcmVzIjoxNjkxMDg0MzU4LjM3NDk5Mjh9.io_IP2q4q8_Gb2T7UERY_qaHrQBN7xLDRLnh7GZ6j0E' \
  --header 'Content-Type: application/json' \
  --data '{
 "exp_date": "2023-12",
 "number": "5113134705352482",
 "holder": "Carlinho Moreira Cesar",
 "cvv": "340"
}'
```

Curl to get all credit cards

```
curl --request GET \
  --url <http://localhost:8000/api/v1/credit-card/> \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VyX25hbWUiOiJGdWxhbm8iLCJ1c2VyX2VtYWlsIjoiZnVsYW5vQGZ1bGFuMi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHBpcmVzIjoxNjkxMDg1MTU0LjcxOTgzMjJ9.Nxh-OWTqi8m6oZTI7GVkq_WL0I9w7fOUko7B0SZXMcg'
```

Curl to get  credit card

```
curl --request GET \
  --url <http://localhost:8000/api/v1/credit-card/1> \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VyX25hbWUiOiJGdWxhbm8iLCJ1c2VyX2VtYWlsIjoiZnVsYW5vQGZ1bGFuMi5jb20iLCJyb2xlIjoiYWRtaW4iLCJleHBpcmVzIjoxNjkxMDg1MTU0LjcxOTgzMjJ9.Nxh-OWTqi8m6oZTI7GVkq_WL0I9w7fOUko7B0SZXMcg'
```

#### For Documentation

The Documentation for all methods [here](http://localhost:8000/docs)
