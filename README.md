# spa-flask

Exemple d'aplicació flask amb autenticació i spa

## Configuració

Inicia el Python Virtual Environment

    python3 -m venv venv
    source venv/bin/activate

Instal·la el requisits:

    pip install -r service-flask/requirements.txt

Alternativament, els requisits es poden instal·lar manualment:

    pip install -U pip
    pip install -U flask flask-login flask-wtf python-dotenv

Per a generar el fitxer de requiriments:

    pip freeze > requirements.txt
    deactivate

Finalment, crea el fitxer `.env` a partir del `.env.exemple`

## Run it

Executa:

    flask run

I obre un navegador a l'adreça [http://127.0.0.1:5000/](http://127.0.0.1:5000/)