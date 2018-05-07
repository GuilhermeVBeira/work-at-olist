# Work at Olist
[![Code Health](https://landscape.io/github/GuilhermeVBeira/work-at-olist/master/landscape.svg?style=flat)](https://landscape.io/github/GuilhermeVBeira/work-at-olist/master)
[![Build Status](https://travis-ci.org/GuilhermeVBeira/work-at-olist.svg?branch=master)](https://travis-ci.org/GuilhermeVBeira/work-at-olist)

# Instalation
After you have already cloned the project
```console
virtualenv env -p python3
source env/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
python manage.py migrate
python manage.py loaddata fixture_tax.json
python maanage.py runserver
```

# Test
```
python manage.py test apps
```

### Environment

|   |    |
|---|---|
|  Computer |   Hp elitebook 8470p |
|  S.O. | Ubuntu 16lts  |
|  Editor | atom  |
|  Django | 2.0  |
|  Python | 3.6  |
|  Django | 2.0  |
|  djangorestframework | 3.8.2 |



## Documentation


#### List telefone taxs
`GET https://calls-api.herokuapp.com/fone-tax/`

#### List bills
`GET https://calls-api.herokuapp.com/bill/?subscriber=<number>`
this will return de last previus month, if you want other references use ‘reference’ for specific date
example:
`GET https://calls-api.herokuapp.com/bill/?subscriber=<number>&reference=04/2018`

### Create a Call Record
`POST https://calls-api.herokuapp.com/bill/`
For start records:
```
    {
        "type": "start",
        "timestamp": 2018-04-28T18:00,
        "call_id": 1991,
        "source": "4199998888",
        "destination": "4199998887"
    }
```

For end records:
```
    {
        "type": "end",
        "timestamp": 2018-04-28T18:40,
        "call_id": 1991,
    }
```
