# Blogger
## Django App to create blogs

Blogger is a cloud-enabled, Django-powered application for writing blog posts.
## URL
https://quiet-crag-39123.herokuapp.com/
## Features
- Users can create,update and delete their blog posts
- Users can change their profile image 

## Tech
Blogger uses a number of open source projects to work properly:

- [Django](https://www.djangoproject.com/) - Python web framework
- [Heroku](https://www.heroku.com/) -  lets you deploy, run and manage applications.
- [AWS S3](https://aws.amazon.com/s3/) - Object storage built to store and retrieve any amount of data from anywhere.

## Installation

Dillinger requires [Django](https://www.djangoproject.com/) to run.

1. Install the dependencies.
```sh
pip3 install -r requirements.txt
```
2. Make database migrations 
```sh
python manage.py migrate
```
3. Start the server 
```sh
python manage.py runserver 
```
4. Go to [localhost:8000](http://localhost:8000/)

## Create .env
1. To load the media files , you have to create an aws s3 bucket 
2. Create a .env file in the root dir of the project 
```sh 
touch .env
```
3. Go to aws s3 > create a new s3 bucket , get 
    1. Get the access key 
    2. secret access key 
    3. bucket name 
4. Generate a secret key with python secrets module 
    1. Open python shell 
    2. Type 
    ```python
    import secrets 
    print(secrets.token_hex(48))
    ```
    3. Copy the token 
5. Go to .env file. Paste the following values without quotes 
```sh
SECRET_KEY=<copied from python>
DEBUG_VALUE=True
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
```


## Django Admin
One of the most powerful parts of Django is the automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. 
##### To go to django admin 
1. Create a superuser 
```sh
python manage.py createsuperuser 
```
specify the username and password 
2. Go to http://localhost:8000/admin
3. Login with the credentials 
4. Here you will see all the django models and data inside each

draw.io: https://drive.google.com/file/d/1d9_tA4-hD69lz7S-AuzIac2TnycBCl5E/view?usp=sharing



## Docker

Blogger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8000, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
docker build -t django-app .
```

This will create the dillinger image and pull in the necessary dependencies in requirements.txt.
Once done, run the Docker image
```sh
docker compose up -d
```



Verify the deployment by navigating to your server address in
your preferred browser.
[localhost:8000](http://localhost:8000/)


