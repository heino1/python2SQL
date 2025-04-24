# MySQL REST API

Lihtne REST API MySQL andmebaasi jaoks, mis võimaldab toodete haldamist.

## Funktsionaalsus

API toetab järgmisi toiminguid:
- Kõikide toodete pärimine
- Üksiku toote pärimine ID järgi
- Toodete pärimine kategooria järgi
- Uue toote lisamine
- Toote andmete muutmine
- Toote kustutamine

## Tehnoloogiad

- Python 3.9
- Flask
- SQLAlchemy
- MySQL
- Docker

## Paigaldamine

1. Klooni repositoorium:
```bash
git clone https://github.com/heino1/python2SQL.git
cd python2SQL/
```

2. Muuda nano abil .env faili: 
```
MYSQL_HOST=your_mysql_host
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=logistika_labor
```

3. Ehita Docker image:
```bash
docker build -t mysql-api .
```

4. Käivita konteiner:
```bash
docker run -d -p 5000:5000 --env-file .env mysql-api
```

## API Kasutamine

### Päringute näited

1. Kõik tooted:
```bash
GET /api/tooted
```

2. Üks toode:
```bash
GET /api/tooted/{toode_id}
```

3. Tooted kategooria järgi:
```bash
GET /api/tooted/kategooria/{kategooria}
```

4. Lisa uus toode:
```bash
POST /api/tooted
Content-Type: application/json

{
    "nimi": "Uus toode",
    "hind": 19.99,
    "kategooria": "Elektroonika"
}
```

5. Muuda toodet:
```bash
PUT /api/tooted/{toode_id}
Content-Type: application/json

{
    "nimi": "Muudetud nimi",
    "hind": 29.99,
    "kategooria": "Arvutid"
}
```

6. Kustuta toode:
```bash
DELETE /api/tooted/{toode_id}
```

