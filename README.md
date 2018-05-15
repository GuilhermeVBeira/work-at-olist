# Work at Olist
[![Code Health](https://landscape.io/github/GuilhermeVBeira/work-at-olist/master/landscape.svg?style=flat)](https://landscape.io/github/GuilhermeVBeira/work-at-olist/master)
[![Build Status](https://travis-ci.org/GuilhermeVBeira/work-at-olist.svg?branch=master)](https://travis-ci.org/GuilhermeVBeira/work-at-olist)

# Description

My solution to the [challenge](https://github.com/olist/work-at-olist/blob/master/README.md) from olist. An api where it is possible to inform the beginning and end of the connections, being possible to identify the price of each one per month.

# Instalation
After you have already cloned the project
```console
cd work-at-olist/
virtualenv env -p python3
source env/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
python manage.py migrate
python manage.py loaddata fixture_tax.json
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
|  Django version| 2.0  |
|  Python version | 3.6.4  |
|  djangorestframework version | 3.8.2 |




## Documentation


### List telefone taxs
`GET https://calls-api.herokuapp.com/phone-tax/`

response: 
```
  {
        "id": 1,
        "standing_charge": "0.36",
        "charge_minute": "0.09",
        "start": "06:00:00",
        "end": "22:00:00",
        "type": "standard"
    },
    {
        "id": 2,
        "standing_charge": "0.36",
        "charge_minute": "0.00",
        "start": "22:00:00",
        "end": "06:00:00",
        "type": "reduced"
    }
```

### List bills
`GET https://calls-api.herokuapp.com/bill/?subscriber=<number>`

this will return de last previus month, if you want other references use ‘reference’ for specific date,
example:

`GET https://calls-api.herokuapp.com/bill/?subscriber=<number>&reference=04/2018`

response: 
```
    {
        "destination": "9993468278",
        "started_date": "2016-02-29",
        "started_time": "14:00:00",
        "duration": "2:00:00",
        "call_price": "11.16"
    },
    ...
```

### Create a Call Record
`POST https://calls-api.herokuapp.com/record/`

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
