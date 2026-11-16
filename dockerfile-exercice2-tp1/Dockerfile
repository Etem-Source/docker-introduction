# Étape 1 : construction
FROM node:jod-alpine3.24 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# Étape 2 : image finale minimale
FROM busybox:musl
RUN addgroup -S appgroup \
    && adduser -S -G appgroup appuser
COPY --from=build /app/dist /www
USER appuser
EXPOSE 8080
CMD ["httpd", "-f", "-p", "8080", "-h", "/www"]