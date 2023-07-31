# BackEnd Credit Card Registration CRUD
 A backend application with user authentication for register credit cards using FastApi and UnitTests
 
 - FastAPI. Docs [here](https://fastapi.tiangolo.com)


## Features
- User Registration: Users can create an account.
- User Login: Users can log in to their accounts.
- Role-based Authentication: Three roles with different permission levels - regular user, user manager, admin.
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