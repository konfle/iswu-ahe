# Użyj obrazu Node.js w wersji 14 (lub innej preferowanej)
FROM node:20.10.0

# Ustaw katalog roboczy w kontenerze
WORKDIR /usr/src/app

# Zainstaluj edytor vi
RUN apt-get update && apt-get install -y vim

# Skopiuj pliki projektu (package.json oraz package-lock.json)
COPY package*.json ./

# Zainstaluj zależności
RUN npm install

# Skopiuj resztę plików projektu
COPY . .

# Otwórz port 3000, który jest domyślnie używany przez aplikacje React
EXPOSE 3000

# Uruchom aplikację po uruchomieniu kontenera
CMD ["npm", "start"]
