# BackEnd Credit Card Registration CRUD
 A backend application with user authentication for register credit cards using FastApi and UnitTests
 
 - FastAPI. Docs [here](https://fastapi.tiangolo.com)


## Features
- User Registration: Users can create an account.
- User Login: Users can log in to their accounts.
- Role-based Authentication: Three roles with different permission levels - regular user, user manager, admin.
- User and Manager: User and managers can CRUD users and Register Credit Cards.
- Admin: Admins can CRUD all records and users, register, list, get, Delete Credit Cards.
- JSON API: Data is returned in JSON format.
- Filtering and Pagination: Endpoints provide filter capabilities and support pagination.
- Unit and E2E Tests: Includes unit tests and end-to-end tests.
- Python Web Framework: Uses any Python web framework.
- SQLite Database: Uses SQLite as the database.
## Get Started

#### Clone the repository.

```shell
    git clone https://github.com/orochidrake/credit-card-core
```


#### Install the required dependencies.

```shell
    pip install -r requirements.txt
```
#### Set up the database with sqlite.

```shell
    python create_db.py
```

#### Run the application.

Application will be exposed to port 8000 on http://localhost:8000/

```shell
    python main.py
```

#### Documentation Methods.

The Documentation for all methods http://localhost:8000/docs [here](http://localhost:8000/docs)
