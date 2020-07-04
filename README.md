# Django Rest API

This is a REST API to retrieve customers informations.

## Installation
For best pratices, we can create a new environment and activate it to hold the app.
I use conda to create my env, but you can use python,etc.

first of all you need to go to the project directory.
```
cd mysite
```
There will be a requirement.txt that holds all of the packages needed to run the project.

```bash
pip install -r requirements.txt
```
## Usage
As requested in `Question 1`, we will use a Django management commad to import our [`customers.csv`](customers.csv) file into the database.

```bash
python manage.py command 
```
Please note that it will take some time to process.
in this step we are importing all data inside our file to the database.
Besides to that we are adding two columns `longitude` and `latitude` for each `city`.

Since this step have already been done, we might run into an exception:
`Table 'myapi_customer' already exists`.

then we can process to running the server.

```bash
python manage.py runserver
```
then we access the localhost: 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

all customers are shown, there on the index page, we can select a customer id and submit the selection to retrieve data about that specific customer.
## Notes
I have used [Django Rest Api Framework](https://www.django-rest-framework.org/) which already provides all the CRUD and HTML and it can be accessed through this link [http://127.0.0.1:8000/framework](http://127.0.0.1:8000/framework).

## Contribution
Hedy Anouar Krid

Feel free to email me on [hedycreed@gmail.com](mailto:hedycreed@gmail.com) for any doubts.

