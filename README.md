# Brians Guitar lessons and blog.

This is an ecommerce website with User log in and Stripe payments. It is a fictional website
in which I offered online Skype Guitar lessons. Also the blog consists of many different Video
recordings of myself playing all the Solo's. Which I specifically recorded for this website.

## Built with ##

1.Django

2 HTML

3.CSS

4.Python

5.Javascript

# Steps to build the project 

## URL'S ##

there are many urls.py files in this project. But the very top level one (ecom_prj) gives the url
pattern routes to the views.py. For e.g.

from django.conf.urls import url, include

from django.contrib import admin

from home.views import say_hello

from accounts import urls as accounts_urls

from products import urls as products_urls

from django.views import static

from .settings import MEDIA_ROOT

from cart import urls as cart_urls

from payments import urls as payments_urls

from blog.views import im_home

from blog import urls as blog_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^$', say_hello, name='index'),
    
    url(r'accounts/', include(accounts_urls)),
    
    url(r'^store/', include(products_urls)),
    
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    
    url(r'^cart/', include(cart_urls)),
    
    url(r'^payments/', include(payments_urls)),
    
    url(r'^blog/', include(blog_urls)),
    
]


## Views  ##

Views consisted of python functions that where basically used to help complete and execute 
some functions for the website to run properly. For e.g logging in and out, making a blog post,
making payments.

## Templates ##

In the folder templates you will find a base.html page which is in the top level and is used as
a "base layout" for all of the other pages on the site. it deals with all the css/navbar/html/javascript
for the site.

{% block content %}
{% endblock content %}

the above two lines allowed other templates to be inserted to that area. The Block content line
was placed at the top above the navbar while the Endblock content was placed at the bottom near the footer.


# Applications

## Home app ##

Top level app that renders the index.html file, which then call the base.html template.
This then loads and presents the website.

## Accounts ##

This allows a vistor to my site to log in  and create there own profile. A register option 
is present on my navbar if a user has no profile already created. From here they can view there own profile,
Make blog posts, and Buy lessons. They also have the option to subscribe to a monthly magazine. A subcription function 
was created ( views.py ) and kicks in when the subscription button is clicked. From here it brings you to a Stripe payment form 
that prompts you for your card details.

## Blog ##

Consists of all my individual blog posts with my Guitar solo's. Any post's that have been created is displayed using
the blogpost.html. A typical post on my page would have a Title, Content section, and a special instagram video link section,
since all of Videos where hosted on instagram. This was very useful. Blog posts have a restricted view on the main page. So in order 
read the full blog post you have to click into the post by hitting the "Read More" postdetail.html dealt with this function.
django-disqus and pillow have to be pip installed to manage comments.

## Cart and payments ##

the cart lists how many items you have and the price your items will be. Then a form for a one off Stripe payment get
rendered from the Payments app

## products ##
this application lists all of the Lessons I have an offer on my website. Each option when selected
is added to the cart.

# Live demo

To view the live Demo view please click on the following link

https://com-ecom-guitar.herokuapp.com/

# Hosting

Website is hosted on Heroku.

# Installations

The followings instructions are needed to run this app.

1. in your terminal go to the folder you want to put the project into and type.

"git clone https://github.com/BrianSheridan/Stream-3-Project.git"

2. create a new virtual enviorment: "python -m venv "Name of virtual env""

then you Activate:

"VirtualEnv/name_of_env/bin/scripts/activate"

3. Install the project dependencies: "pip install -r requirements.txt'

4. Set up an account for Stripe at https://stripe.com/gb and save you STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY
in a safe place you will need them later.

5. go to your activate.bat file in your Virtual env folder and edit the file by placing the following code
at the end of the file.

set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

set SECRET_KEY="4af*&4lpr@uhjw99+sbg3io@(t!3ggsa##wy0#u-3^+5%89+&-"

set DEBUG="True"

set STRIPE_PUBLISHABLE_KEY=pk_test_bZjtObaNmQIO2jLuQjxKy5Kd

set STRIPE_SECRET_KEY=sk_test_V518FdWovtnwkljHoQWCeeSK

set DATABASE_URL=postgres://odglxozxzdftkw:a013c0acfe37e04780455e64d963fa25461d83771832aded70a5cb5976df9029@ec2-54-247-189-141.eu-west-1.compute.amazonaws.com:5432/dc08of8edi9nho

set BUCKET_NAME=djangoguitar-s3


set AWS_ACCESS_KEY=AKIAISR4LREM254PKLTA

set AWS_SECRET_ACCESS_KEY=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

:END


## 6. Go to you settings.py file and change the following lines of code: lines 148 - 177 ##

TO RUN ON LOCALLY HAVE LTHESE TWO LINKS UNCOMMENTED

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

TO RUN ON HEROKU HAVE THESE TWO UNCOMMENTED

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires

       'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
       
       'Cache-Control': 'max-age=94608000',
   }


AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

 Tell django-storages that when coming up with the URL for an item in S3 storage, keep

 it simple - just use this domain plus the path. (If this isn't set, things get complicated).

 This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.

 We also use it in the next setting.

AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'

STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'

MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

## 7. Change the following lines in settings.py (92 - 100) to run locally ##

TO RUN DATABASE LOCALLY
 DATABASES = {
 
     'default': {
     
         'ENGINE': 'django.db.backends.sqlite3',
         
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }

DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }





8. Go to your terminal and apply your migrations by using "python manage.py makemigrations" this will make migrations
to your local db sqlite database.

 9.Create a super user using "python manage.py createsuperuser" this will create your own admin log in

10. "python manage.py runserver" to run the project locally.

11. Go to your browser and type "localhost:8000" or "127.0.0.1:8000" to view website

12. "127.0.0.1:8000/admin" go to this link and sign in using the superuser information you created.
    you will be able to make blogposts from that point.


# Databases and static files

SQlite database was used when running the project locally. This database stored all of my media and Static files.
When it came to deployment Heroku postgres was used as the server, and for all my static files and media files an Amazon S3 bucket
was created and that was used to store all of my static and media files.
To switch between running locally and deploying on Heroku I had to comment out my database code in my
settings.py

# Testing

I carried out some tests in the accounts app to basically make sure all the information being used was validated correctly.
Did this by activating my virtual enviorment in my project folder.

From there you type the following:

"python manage.py test accounts"

this command test my registration form to see if it validates properly when the correct information is entered,
also tests to see if the form fails if the passwords dont match and finally test the form to see if it fails
when one password has not been entered.












































