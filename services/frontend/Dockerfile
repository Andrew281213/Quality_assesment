FROM node:lts-alpine

WORKDIR /app

RUN npm install @vue/cli -g

COPY package*.json ./
RUN npm install --silent

COPY . /app

CMD ["npm", "run", "serve"]
