# Blog API with Django Rest Framework 

<p><a href="https://www.python.org/"><img src="https://user-images.githubusercontent.com/94041207/199345472-e98865f2-0d41-4bd9-9a5c-9c21b4831c1e.png" alt="python" height="30" data-canonical-src="https://www.python.org/static/img/python-logo.png" style="max-width: 100%;">   </a>
<a href="https://www.djangoproject.com/"><img src="https://user-images.githubusercontent.com/94041207/199345498-a5e894de-16cc-4715-8a68-78fe070afd30.png" alt="django" height="30" data-canonical-src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" style="max-width: 100%;">   </a>
<a href="https://www.django-rest-framework.org/"><img src="https://user-images.githubusercontent.com/94041207/199345513-1a3bd338-9d8a-44a4-b3c4-e64b2ac7eed4.png" alt="django rest framework" height="30" style="max-width: 100%;"></a>
<a href="https://www.sqlite.org/index.html"><img src="https://user-images.githubusercontent.com/94041207/199345538-30ee000d-8dc2-4334-ac31-f54a62fc9549.png" alt="SQLite" height="30" style="max-width: 100%;"></a>
<a href="https://www.postgresql.org/"><img src="https://user-images.githubusercontent.com/94041207/199345580-4c43f36f-6ec8-4d87-8c0c-756c9d91827f.png" alt="PostgreSQL" height="30" style="max-width: 100%;"></a>
<a href="https://www.heroku.com/"> <img src="https://user-images.githubusercontent.com/94041207/199347164-3f31eca4-6b7e-4c6d-bb1d-0959f5134e30.png" alt="heroku" height="30" data-canonical-src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" style="max-width: 100%;"> </a></p>

## Demo
<a href="https://react-redux-blogapp.vercel.app/" target="_blank"> Live link 🚀 </a>

## In Backend
[Project link 🚀](https://blogapp-react-redux.herokuapp.com/) for to check with postman
* In developoment process database is <img src="https://logos-download.com/wp-content/uploads/2018/09/SQLite_Logo-450x193.png"  alt="sqlite" height="30">
* In production process database is <img src="https://icon-library.com/images/postgresql-icon/postgresql-icon-13.jpg"  alt="postgresql" height="30"> 
* Backend part was deployed to <img src="https://user-images.githubusercontent.com/94041207/182912844-075185f7-3c3f-4d77-9f49-740dbdadd14d.png"  alt="heroku" height="30"> 
* **dj rest auth** package was used for login, logout and authentication. However register view and serializer were hard coded.
* **Concrete views** and **Viewsets** were used as views. 
* **Nested serializers** were used. 
* **Token authentication** was used for authentication.
* **Custom permissions** and **object permissions** were used for authorization/permission. 
* **Cursor pegination** was choosed for pegination.
* **Search filter** was choosed for filtering.
* Although **form validation** was done in frontend, **it was also done in the backend.**
* **Swagger**, **redoc**, **debug toolbar** were used. And debug was made true for other users to check easily. 
* Finally as tiny details: 
**select_related** method was preferred for query optimisation. 
**SerializerMethodField** was preferred for field customization.
**Some methods were overridden** to create custom functionalities.


<a href="https://github.com/bekirugurr/react-redux-blog-app" target="_blank"> Frontend repository 🚀 </a> if you want to check


