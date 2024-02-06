# Utilitza una imatge base amb Python i Tkinter
FROM python:3.8-slim

# Instal·la les dependències necessàries, incloent Tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Estableix el directori de treball a /app
WORKDIR /app

# Copia el codi de l'aplicació al contenidor
COPY . /app

# Instal·la les dependències necessàries per a la teva aplicació
RUN pip install --no-cache-dir -r requirements.txt

# Comanda per executar l'aplicació quan s'iniciï el contenidor
CMD [ "python", "menu.py" ]

