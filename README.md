# SocialNetX
**SocialNetX** makes social media management super-easy. It synchronizes multiple social media accounts at one platform. SocialNetX allows the user to see all their social media analytics at one place. SocialNetX provides a dashboard through which multiple social accounts can be managed thus eliminating the need to manually go into each account and check what happened in the past week. 

![Image of Homepage ](http://i.imgur.com/2KYgkS6.png)

## Installation Instructions

If you like to contribute to the project you can set up development environment locally. Here are the steps to setup development environment:

Use git clone available to get a copy of the socialNetX project:
```
$ git clone https://github.com/atmishra/socialnetx.git
```
Create virtual environment for the project using virtualenvwrapper:
```
$ mkvirtualenv Socialnetx
```
Activate your working environment:
```
$ workon Socialnetx
```
Install proejct requirements:
```
cd socialnetx
pip install -r requirements/local.txt
```
Set Databse URL in your environment variable
```
$ gedit ~/.bashrc
export DATABASE_URL=postgres://exampleuser:user@localhost:5432/socialnetx
```
Create Database and run migrations
```
$ createdb socialnetx
$ ./manage.py makemigrations
$ ./manage.py migrate
```
Now you are ready to run development server:
```
$ ./manage.py runserver
```
You can now access **SocialNetX** through http://localhost:8000/

##Contributers
- Atul Mishra
- Parbhat Puri
