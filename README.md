
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Thanks for checking it out.

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
Supporting the Development of Django
Django's development depends on your contributions.

If you depend on Django, remember to support the Django Software Foundation: https://www.djangoproject.com/fundraising/






Django REST framework
build-status-image coverage-status-image pypi-version



Full documentation for the project is available at https://www.django-rest-framework.org/.

Funding
REST framework is a collaboratively funded project. If you use REST framework commercially we strongly encourage you to invest in its continued development by signing up for a paid plan.

The initial aim is to provide a single full-time position on REST framework. Every single sign-up makes a significant impact towards making that possible.

       

Many thanks to all our wonderful sponsors, and in particular to our premium backers, Sentry, Stream, Spacinov, Retool, bit.io, PostHog, CryptAPI, and FEZTO.

Overview
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

The Web browsable API is a huge usability win for your developers.
Authentication policies including optional packages for OAuth1a and OAuth2.
Serialization that supports both ORM and non-ORM data sources.
Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
Extensive documentation, and great community support.
There is a live example API for testing purposes, available here.

Below: Screenshot from the browsable API

Screenshot

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

For questions and support, use the REST framework discussion group, or #restframework on libera.chat IRC.

You may also want to follow the author on Twitter.

Security
Please see the security policy.
