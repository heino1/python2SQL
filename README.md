# MySQL Toodete Haldamise API ja Veebiliides

Lihtne REST API ja veebiliides MySQL andmebaasi toodete haldamiseks. Projekt on mõeldud õppematerjaliks, et tutvustada REST API põhimõtteid ja veebiteenuste kasutamist.

## Funktsionaalsus

### Veebiliides
- Toodete nimekirja kuvamine
- Uue toote lisamine
- Olemasoleva toote muutmine
- Toote kustutamine
- Reaalajas andmete värskendamine

### REST API
API toetab järgmisi toiminguid:
- `GET /api/tooted` - Kõikide toodete pärimine
- `GET /api/tooted/<id>` - Üksiku toote pärimine ID järgi
- `GET /api/tooted/kategooria/<kategooria>` - Toodete pärimine kategooria järgi
- `POST /api/tooted` - Uue toote lisamine
- `PUT /api/tooted/<id>` - Toote andmete muutmine
- `DELETE /api/tooted/<id>` - Toote kustutamine

## Tehnoloogiad

- Python 3.9
- Flask (veebiraamistik)
- SQLAlchemy (ORM)
- MySQL (andmebaas)
- HTML/CSS/JavaScript (veebiliides)
- Docker (konteineriseerimine)

## Eeldused

1. Python 3.9 või uuem
2. MySQL andmebaas
3. Docker 

## Paigaldamine


1. Klooni repositoorium:
```bash
git clone https://github.com/heino1/python2SQL.git
cd python2SQL
```

2. Paranda .env fail oma andmetega vastavusse:
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

## Kasutamine

### Veebiliides

1. Ava brauser aadressil `http://AWS_NGINX_IP:5000`
2. Veebiliideses saad:
   - Näha kõiki tooteid
   - Lisada uusi tooteid
   - Muuta olemasolevaid tooteid
   - Kustutada tooteid
   - Värskendada toodete nimekirja

### edasijõudnud võivad proovida jõudu curl'i ja API-ga

1. Kõik tooted:
```bash
curl http://localhost:5000/api/tooted
```

2. Üks toode:
```bash
curl http://localhost:5000/api/tooted/1
```

3. Lisa uus toode:
```bash
curl -X POST http://localhost:5000/api/tooted \
     -H "Content-Type: application/json" \
     -d '{"nimi": "Uus toode", "hind": 19.99, "kategooria": "Elektroonika"}'
```

4. Muuda toodet:
```bash
curl -X PUT http://localhost:5000/api/tooted/1 \
     -H "Content-Type: application/json" \
     -d '{"nimi": "Muudetud nimi", "hind": 29.99}'
```

5. Kustuta toode:
```bash
curl -X DELETE http://localhost:5000/api/tooted/1
```

## Andmebaasi struktuur

Tabel `toode`:
- `toode_id` (INT, PRIMARY KEY) - Toote unikaalne identifikaator
- `nimi` (VARCHAR(255)) - Toote nimetus
- `hind` (FLOAT) - Toote hind
- `kategooria` (VARCHAR(255)) - Toote kategooria

## Litsents

MIT 