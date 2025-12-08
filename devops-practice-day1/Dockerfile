FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json
RUN npm install

FROM node:18-alpine
WORKDIR /app
COPY --from=build /app .
USER node
EXPOSE 3000
CMD ["node","server.js"]
