# EatDeal

EatDeal is a service that aggregates promotions for food in restaurants and cafes. The user can view promotions that are available in the selected city at the moment. Stock markers appear on the map only at the moment of their activation. It is also possible to see all the promotions in the city.


The administrator can add any number of cities to the service, as well as edit the promotions themselves.


Registration in the service is available locally or using the Google service. After registration, the user can add promotions to favorites.
## Environment Variables

Before installing and running the project, you need to change the values ​​​​of the variables in the .env file in the infra folder:

`GOOGLE_API=` - 
can be obtained from https://developers.google.com

`DB_NAME=`

`POSTGRES_USER=`

`POSTGRES_PASSWORD=`

`DB_HOST=`

`DB_PORT=`

`SECRET_KEY=` - can be generated here https://djecrety.ir/## Run Locally

At the first start, for the project to function, it is necessary to install a virtual environment and perform migrations:

    $ python -m venv venv
    $ source venv/Scripts/activate
    $ pip install -r requirements.txt
    $ python yatube_api/manage.py makemigrations
    $ python yatube_api/manage.py migrate

Create superuser for admin panel:

    $ python yatube_api/manage.py createsuperuser

Run server:

    $ python yatube_api/manage.py runserver
    

After launch, the admin panel will be available at http://127.0.0.1:8000/admin/


## Google Authorization

After launch, you need to create a google provider in the administrative panel in order for authorization through Google to work. To do this, you first need to register at https://developers.google.com and get a **Client ID** and **Secret** for OAuth 2.0 authorization.

## Database structure

