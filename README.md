
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. 
All documentation is in the "docs" directory and online at https://docs.djangoproject.com/en/stable/. If you're just getting started, here's how we recommend you read the docs:

First, read docs/intro/install.txt for instructions on installing Django.
Next, work through the tutorials in order (docs/intro/tutorial01.txt, docs/intro/tutorial02.txt, etc.).
If you want to set up an actual deployment server, read docs/howto/deployment/index.txt for instructions.
You'll probably want to read through the topical guides (in docs/topics) next; from there you can jump to the HOWTOs (in docs/howto) for specific problems, and check out the reference (docs/ref) for gory details.
See docs/README for instructions on building an HTML version of the docs.
Docs are updated rigorously. If you find any problems in the docs, or think they should be clarified in any way, please take 30 seconds to fill out a ticket here: https://code.djangoproject.com/newticket

To get more help:

Join the #django channel on irc.libera.chat. Lots of helpful people hang out there. Webchat is available.
Join the django-users mailing list, or read the archives, at https://groups.google.com/group/django-users.
Join the Django Discord community.
Join the community on the Django Forum.
To contribute to Django:

Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for information about getting involved.
To run Django's test suite:

Follow the instructions in the "Unit tests" section of docs/internals/contributing/writing-code/unit-tests.txt, published online at https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests


Django REST framework
build-status-image coverage-status-image pypi-version



Full documentation for the project is available at https://www.django-rest-framework.org/.

Funding
REST framework is a collaboratively funded project. If you use REST framework commercially we strongly encourage you to invest in its continued development by signing up for a paid plan.

The initial aim is to provide a single full-time position on REST framework. Every single sign-up makes a significant impact towards making that possible.


Overview
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

The Web browsable API is a huge usability win for your developers.
Authentication policies including optional packages for OAuth1a and OAuth2.
Serialization that supports both ORM and non-ORM data sources.
Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
Extensive documentation, and great community support.

Requirements
Python 3.6+
Django 4.2, 4.1, 4.0, 3.2, 3.1, 3.0
We highly recommend and only officially support the latest patch release of each Python and Django series.

Installation
Install using pip...

pip install djangorestframework
Add 'rest_framework' to your INSTALLED_APPS setting.

INSTALLED_APPS = [
    ...
    'rest_framework',
]
Example
Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups.

Startup up a new project like so...

pip install django
pip install djangorestframework
django-admin startproject example .
./manage.py migrate
./manage.py createsuperuser
Now edit the example/urls.py module in your project:

from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
We'd also like to configure a couple of settings for our API.

Add the following to your settings.py module:

INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
That's it, we're done!

./manage.py runserver
You can now open the API in your browser at http://127.0.0.1:8000/, and view your new 'users' API. If you use the Login control in the top right corner you'll also be able to add, create and delete users from the system.

You can also interact with the API using command line tools such as curl. For example, to list the users endpoint:

$ curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin",
        "email": "admin@example.com",
        "is_staff": true,
    }
]
Or to create a new user:

$ curl -X POST -d username=new -d email=new@example.com -d is_staff=false -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/
{
    "url": "http://127.0.0.1:8000/users/2/",
    "username": "new",
    "email": "new@example.com",
    "is_staff": false,
}
Documentation & Support
Full documentation for the project is available at https://www.django-rest-framework.org/.

#
Django is based on MVT (Model-View-Template) architecture. MVT is a software design pattern for developing a web application. 

MVT Structure has the following three parts – 

Model: The model is going to act as the interface of your data. It is responsible for maintaining data. It is the logical data structure behind the entire application and is represented by a database (generally relational databases such as MySql, Postgres). 

View: The View is the user interface — what you see in your browser when you render a website. It is represented by HTML/CSS/Javascript and Jinja files. 

Template: A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. 

 Project Structure :
A Django Project when initialized contains basic files by default such as manage.py, view.py, etc. A simple project structure is enough to create a single-page application. Here are the major files and their explanations. Inside the site folder ( project folder ) there will be the following files- 

manage.py- This file is used to interact with your project via the command line(start the server, sync the database… etc). For getting the full list of commands that can be executed by manage.py type this code in the command window- 
$ python manage.py help

 folder  – This folder contains all the packages of your project. Initially, it contains four files – 

_init_.py – It is a python package. It is invoked when the package or a module in the package is imported. We usually use this to execute package initialization code, for example for the initialization of package-level data.

settings.py – As the name indicates it contains all the website settings. In this file, we register any applications we create, the location of our static files, database configuration details, etc.

urls.py – In this file, we store all links of the project and functions to call.

wsgi.py – This file is used in deploying the project in WSGI. It is used to help your Django application communicate with the webserver.

