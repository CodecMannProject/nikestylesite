# NikeStyleSite
My own site built on [Django](https://www.djangoproject.com/) created a few years ago

## Instalation

### Firstly, create a fresh new django project and venv

```
django-admin startproject [your project name]
virtualenv venv
venv/scripts/activate
```

### Now, clone this repository:
```
git clone https://github.com/CodecMannProject/nikestylesite.git
```

### Then install requirements in your venv

```
pip install -r requirements.txt
```

### Then, go to your settings.py and copy its SECRET_KEY (save it somewhere)
### Now move all repository files into yours, and remove folder with your project name

### And finally, create file in "kukurudzo" with blank name in format .env, and add your secret key like this:
```
SECRET_KEY='[your key goes here]'
```

## Usage

### To setup, run:
```
py manage.py makemigrations
py manage.py migrate
```

### And then:
```
py manage.py runserver [port, default is 8000]
```

