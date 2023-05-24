# Backend Task - Clean Architecture

This project is a very naive implementation of a simple shop system. It mimics in its structure a real world example of a service that was prepared for being split into microservices and uses the current Helu backend tech stack.

## Goals

Please answer the following questions:

1. Why can we not easily split this project into two microservices?

```
The project is not easily separable into two microservices because in its current state there is a strong dependency between Item and User in several places—both at the database level and in the application logic, such as in the “add_item_to_cart” functionality. At a more advanced and mature stage, it could be split by keeping Item and User independent, but this would require a synchronization system to keep the databases of both entities updated across both microservices.
```

2. Why does this project not adhere to the clean architecture even though we have seperate modules for api, repositories, usecases and the model?

```
This project does not comply with Clean Architecture because simply having a separation by layers is not enough. It is necessary to maintain a direction in the dependencies, where only the outermost layers depend on the innermost layers, and not the other way around. For example, the use_cases.py modules should not have references to classes from api.py, as that violates the principles of dependency direction. To achieve this, it is necessary to work on properly including interfaces and applying dependency injection correctly.
```

3. What would be your plan to refactor the project to stick to the clean architecture?

```
Some steps to provide a better clean architecture will be:

- Define abstract interfaces for repositories. Use cases must depend on abstractions not implementations.

-  The database logic to concrete implementations (in an infrastructure layer), and keep the models as dataclasses or Pydantic models in the domain layer.

- Push down all core logic to domain layer, like adding items to user cart. Validations are a core part of the domain, so this validation, for example, must be on the domain.

- Bring some design patterns to help layer isolation and respect single responsability like Repository, Command Handler Patterns.

- Raise specific domain exceptions (not HTTP exceptions).
```

4. How can you make dependencies between modules more explicit?

```
We can achieve that by dependency injection, working with the abstraction in the Application/Use Case Layer and taking advantage of type hints and linters.
```

*Please do not spend more than 2-3 hours on this task.*

Stretch goals:
* Fork the repository and start refactoring
* Write meaningful tests
* Replace the SQL repository with an in-memory implementation

```
Extra Considerations

After a little bit more than the recommended time to complete the tecnical assements, some tests have been left behind. However, the existings ones are good samples of the three main types of tests we should have in any repo, following the test pyramid, coverting all layers (API, Application, Infrastructure and Domain).

All remaining tests can be addressed following the same idea followed in the coded ones. For example, the use case for adding a cart, that contains the two repos and the item provider, in the end, it should just follow the same idea of mocking the "external" pieces of that command handler to guide the test.

```




## References
* [Clean Architecture by Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
* [Clean Architecture in Python](https://www.youtube.com/watch?v=C7MRkqP5NRI)
* [A detailed summary of the Clean Architecture book by Uncle Bob](https://github.com/serodriguez68/clean-architecture)

## How to use this project

If you have not installed poetry you find instructions [here](https://python-poetry.org/).

1. `docker-compose up` - runs a postgres instance for development
2. `poetry install` - install all dependency for the project
3. `poetry run schema` - creates the database schema in the postgres instance
4. `poetry run start` - runs the development server at port 8000
5. `/postman` - contains an postman environment and collections to test the project

## Other commands

* `poetry run graph` - draws a dependency graph for the project
* `poetry run tests` - runs the test suite
* `poetry run lint` - runs flake8 with a few plugins
* `poetry run format` - uses isort and black for autoformating
* `poetry run typing` - uses mypy to typecheck the project

## Specification - A simple shop

* As a customer, I want to be able to create an account so that I can save my personal information.
* As a customer, I want to be able to view detailed product information, such as price, quantity available, and product description, so that I can make an informed purchase decision.
* As a customer, I want to be able to add products to my cart so that I can easily keep track of my intended purchases.
* As an inventory manager, I want to be able to add new products to the system so that they are available for customers to purchase.