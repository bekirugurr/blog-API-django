# Blog API with Django Rest Framework 

<a href="https://www.python.org/"><img src="https://user-images.githubusercontent.com/94041207/199492900-766b0685-56b1-42fc-8510-a221f05de673.png" alt="python" height="30" data-canonical-src="https://www.python.org/static/img/python-logo.png" style="max-width: 100%;">   </a>
<a href="https://www.djangoproject.com/"><img src="https://user-images.githubusercontent.com/94041207/199492944-09e06dfc-a246-48e5-9dea-08c57195fcbd.png" alt="django" height="30" data-canonical-src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" style="max-width: 100%;"></a>
<a href="https://www.django-rest-framework.org/"><img src="https://user-images.githubusercontent.com/94041207/199345513-1a3bd338-9d8a-44a4-b3c4-e64b2ac7eed4.png" alt="django rest framework" height="30" style="max-width: 100%;"></a>
<a href="https://www.sqlite.org/index.html"><img src="https://user-images.githubusercontent.com/94041207/199492996-de5eaa34-dc69-463a-a31d-8fc3a3dc7694.png" alt="SQLite" height="30" style="max-width: 100%;"></a>
<a href="https://www.postgresql.org/"><img src="https://user-images.githubusercontent.com/94041207/199492963-9315ee83-5be9-43b3-aa14-ebdd9a869aea.png" alt="PostgreSQL" height="30" style="max-width: 100%;"></a>
<a href="https://postman.com" rel="nofollow"> <img src="https://user-images.githubusercontent.com/94041207/199493662-5b0ab606-1e40-4aee-919e-f8bae4e65794.png" alt="postman" height="30" data-canonical-src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" style="max-width: 100%;"> </a>
<a href="https://www.heroku.com/"> <img src="https://user-images.githubusercontent.com/94041207/199493654-70c90e3b-24e6-43ab-b700-b73977c6187c.png" alt="heroku" height="30" data-canonical-src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" style="max-width: 100%;"> </a>

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


