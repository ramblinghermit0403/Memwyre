# Stage 1: Build the Vue app
FROM node:20-slim AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

# Accept the API URL as a build-time argument
ARG VITE_API_URL=http://localhost:8000/api/v1
ENV VITE_API_URL=${VITE_API_URL}

COPY . .
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Copy the built assets
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
