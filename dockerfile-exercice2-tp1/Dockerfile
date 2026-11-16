# ===== Étape 1 : build (outils de développement, non conservés) =====
FROM node:22.23.5-alpine3.24 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# ===== Étape 2 : production (image finale minimale) =====
FROM busybox:1.38.0-musl
RUN addgroup -S appgroup \
    && adduser -S -G appgroup appuser
COPY --from=build /app/dist /www
USER appuser
EXPOSE 8080
CMD ["httpd", "-f", "-p", "8080", "-h", "/www"]