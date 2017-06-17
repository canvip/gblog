
    ----------------------------------------------------------------- 


اهلا وسهلا بكم 
.
gblog

## Starting from the Terminal

    $ python manage.py migrate

Run Django

    $ python manage.py runserver $IP:$PORT
    
    
## github 

https://github.com/canvip/gblog.git
 
 ## 00
 git init
 git add .
 git commit -m "add blog in heroku"
 git remote add origin https://github.com/canvip/gblog.git
 git push -u origin master
 ##
  
  
  
  ##########
  
  
  Install the Heroku CLI

Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login
Create a new Git repository

Initialize a git repository in a new or existing directory

$ cd my-project/
$ git init
$ heroku git:remote -a canvip-blog
Deploy your application

Commit your code to the repository and deploy it to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master
Existing Git repository

For existing repositories, simply add the heroku remote

$ heroku git:remote -a canvip-blog


## db 
heroku addons:create heroku-postgresql:hobby-dev