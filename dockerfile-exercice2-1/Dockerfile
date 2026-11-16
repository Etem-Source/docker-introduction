# Étape 1 : construction de l'application
FROM node:jod-alpine3.24 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# Étape 2 : image finale minimale (busybox + fichiers statiques)
FROM busybox:musl
COPY --from=build /app/dist /www
EXPOSE 80
CMD ["httpd", "-f", "-p", "80", "-h", "/www"]