# Project-test Items, Banners

Proiectul dat este o simpla implementare a unui fastAPI pentru a crea un Item cu mai multi parametri si crearea unui Baner care contine image si name.
In cadrul acestui proect sa implementat metodele CRUD: POST, GET, DELETE, PUT, PATCH.
## Instalare
Această comandă instalează toate dependențele necesare pentru proiect, bazate pe lista de dependențe din fișierul requirements.txt. Asigură-te că rulezi această comandă din directorul proiectului pentru a asigura instalarea corectă a tuturor dependențelor.
```bash
pip install -r requirements.txt
```
### VENV
Este recomandat să lucrezi într-un mediu virtual Python (`venv`) pentru a izola dependențele proiectului și a evita conflictul cu alte proiecte. Iată cum să creezi și să activezi un mediu virtual:

1. Creează un mediu virtual în directorul proiectului. Poți folosi următoarea comandă:

```bash
python -m venv venv
```

## Utilizare

Pentru a executa un commit pentru baza de date, 
folosește următoarea comandă:

```bash
alembic revision --autogenerate -m "mesaj de commit"
```
Această comandă va genera o nouă migrare în directorul alembic, bazată pe modificările detectate în modelele tale.
După ce ai generat migrarea, pentru a aplica aceste modificări în baza de date, folosește comanda:

```bash
alembic upgrade head
```
Această comandă va aplica toate migrările care nu au fost încă aplicate în baza de date, aducând-o la ultima versiune specificată în migrările tale.

### Pornirea FastAPI

Pentru a porni aplicația FastAPI,este necesar comanda:

```bash
uvicorn main:app --reload
```

Inlocuiești main cu numele fișierului principal al aplicației tale FastAPI.

### FastAPI generează automat documentația API. 
Poți accesa documentația interactivă generată de Swagger UI la http://127.0.0.1:8000/docs
și documentația generată de ReDoc la http://127.0.0.1:8000/redoc.
