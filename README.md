
# Djano OpenVPN - Admin Interface

  

  

Have you ever used the [Docker-Open VPN repository](https://github.com/kylemanna/docker-openvpn) before? If yes, have you ever thought about making it automatic?

  

This is exactly what I have done with this mini-project. By connecting Django Admin Panel to "Docker-Openvpn", you can immediately have your own openvpn admin panel.

  

Let's get started.

  

  

# Project setup

First of all install [Docker-Open VPN](https://github.com/kylemanna/docker-openvpn) on your server and create a user. Please follow [this simple tutorial in medium](https://medium.com/@gurayy/set-up-a-vpn-server-with-docker-in-5-minutes-a66184882c45).

  

After that clone the project:

```
git clone https://github.com/pyhp2017/Django-OpenVpn-Maker
```

Change the following lines in Django Settings:

```
...

# TODO: add your host ip here

ALLOWED_HOSTS = ['1.1.1.1']

...

# TODO: Change username

STATICFILES_DIRS = [

BASE_DIR / "static",

'<path_to_project_dir>/Django-OpenVpn-Maker/static/configs/',

]
```

after that go to Authentications/models and change the following settings:

```
...

# TODO: Change Path here:

vpn_data_absolute_path = '<path_to_vpn_data_docker_openvpn>/vpn-data'

...

# TODO:Change Path here:

output_absolute_path = "<path_to_project_dir>/static/configs/"

...
```

create a virtual environment and activate it:

```
cd Django-OpenVpn-Maker

python3 -m venv venv

source venv/bin/activate
```

install dependencies:

```
pip3 install -r requirements.txt
```

migrate models:

```
python3 manage.py migrate
```

Run Server and login with following username and password:

```
python3 manage.py runserver
```

Panel: <Server_IP>/admin/login/?next=/admin/
username: openvpn
password: openvpn

  

**Warning: After logging in, change the default password**

  

If you have all the settings set up correctly, you can create an Openvpn client from your admin panel's User Authentication section. Just be aware that you can connect to created configs without a password, so submitting a correct password is not necessary. (I'm working on a solution for this issue).

  
  
  

# Screenshots:

![User Creation](https://google.com  "User Create")

![User Edit and Download Config](https://google.com  "User Edit and Download Config")