FROM node:22-alpine AS builder

WORKDIR /app
COPY eraowl-ops-frontend/package.json eraowl-ops-frontend/package-lock.json ./
RUN npm ci

COPY eraowl-ops-frontend/ ./
COPY design/ ../design/
RUN npm run build

FROM nginx:alpine AS runner

COPY --from=builder /app/dist /usr/share/nginx/html
COPY eraowl-ops-frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
