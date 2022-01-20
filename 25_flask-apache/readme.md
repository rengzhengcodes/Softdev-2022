# how-to :: Deploy Flask App On Apache
---
## Overview
We code most of our stuff in Flask in this class, as its relatively easy to work with and well documented. Flask, however, is not good at load balancing or other webhosting features like Apache is. Doing this allows us to run Flask on Apache, taking advantage of both setups.

### Estimated Time Cost: 30 minutes

### Prerequisites:
- A VPS with LAMP set up
- Hairs to turn gray

## Instructions (Two Different Methods)

### Deploying Flask app with virtual host
1. Enable mod_wsgi
   ```
   sudo apt-get install libapache2-mod-wsgi-py3 python-dev
   ```
   ```
   sudo a2enmod wsgi
   ```
2. Create flask app (replace FlaskApp with name you would like to give)
   ```
   cd /var/www
   ```
   ```
   sudo mkdir FlaskApp
   ```
   ```
   cd FlaskApp
   ```
    ```
   sudo mkdir FlaskApp
   ```
   ```
   cd FlaskApp
   ```
   ```
   sudo mkdir static templates
   ```
   Add the contents of your flask app into __init__.py
   ```
   sudo nano __init__.py
   ```
   ```
   from flask import Flask
   app = Flask(__name__)
   @app.route("/")
   def hello():
   	return "Hello, I hate Digital Ocean!"
   if __name__ == "__main__": #this seems like a deviation from Cliu's that's important
   	app.run()
   ```
3. Install Flask
   ```
   sudo apt-get install python3-pip
   ```
   ```
   sudo pip3 install virtualenv #another cliu deviation that could be vital.
   ```
   replace venv with the name of virtual environment
   ```
   sudo virtualenv venv
   ```
   ```
   source venv/bin/activate
   ```
   ```
   sudo pip3 install Flask #Flask capitalization could also be vital.
   ```
   Test if you installed it
   ```
   sudo python3 __init__.py
   ```
4. Configure and enable virtual host (note again that all the FlaskApp -> <your_new_name>)
   ```
   sudo nano /etc/apache2/sites-available/FlaskApp.conf
   ```
   Change mywebsite.com to the IP, and FlaskApp to name of your flask app
   If you are using a domain, change your IP to the domain name.
   ```
   <VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
   </VirtualHost>
   ```
   Enable Virtual Host
   ```
   sudo a2ensite FlaskApp
   ```
5. Create WSGI file
   ```
   cd /var/www/FlaskApp
   ```
   ```
   sudo nano flaskapp.wsgi
   ```
   ```
   #!/usr/bin/python
   import sys
   import logging
   logging.basicConfig(stream=sys.stderr)
   sys.path.insert(0,"/var/www/FlaskApp/")

   from FlaskApp import app as application
   application.secret_key = 'Add your secret key'
   ```
6. Apply changes
   ```
   sudo service apache2 restart
   ```
You should be able to access your virtual host at your ip.

### Add your first app on the droplet by running the app normally (easier, fewer spots for errors, but when you exit, the process ends)
1. Clone your workshop repo onto the new machine (use http unless you want to add a key to the VM)
   ```
   git clone https://github.com/<your_username>/<workshop_repo_name>.git
   ```
2. Before doing anything else, type in the following commands so that python3 works while running flask
   ```
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt-get install python3-pip
   sudo apt-get install python3-dev
   sudo apt-get install python3-setuptools
   sudo apt-get install python3-venv
   sudo apt-get install build-essential libssl-dev libffi-dev
   sudo apt-get install libapache2-mod-wsgi-py3
   ```
3. Find the code for the simplest version of a flask app– perhaps k09?- and cd into that directory
    ```
    cd <workshop_repo_name>/<app_you_want>
    ```
4. Make and activate a virtual environment in that directory
    ```
    python3 -m venv <environment_name>
    source <environment_name>/bin/activate
    ```
5. Use pip install to get some basic packages
    ```
    pip install wheel
    pip install flask
    pip install uwsgi
    pip install requests
    ```
OR (if the directory has a requirements.txt)
    ```
    pip install -r requirements.txt
    ```

6. Make a quick change to where your app loads- open up the file that runs the app (should be app.py) and put '0.0.0.0' in the run parentheses
    ```
    nano (or vim...) app.py
    ```
  Then: scroll to the ```if __name__ == "__main__"``` and alter ```app.run``` to
  ```app.run(host='0.0.0.0')```

7. Enable traffic on port 5000 on the ufw firewall (default flask port)
    ```
    sudo ufw allow 5000
    ```
7. Run the app
    ```
    python3 app.py
    ```
8. Check if the app worked on port 5000 of your droplet (hopefully it does!!)

### Resources
* https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
---

Accurate as of (last update): 2022-01-18

#### Contributors:  
Eliza Knapp, pd2  
Andrew Juang, pd2  
Noakai Aronesty, pd2  
Renggeng Zheng, pd1
