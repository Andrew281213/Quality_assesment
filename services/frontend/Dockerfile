FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install -g @vue/cli@5.0.8

COPY package.json package-lock.json /app/
RUN npm install

CMD ["npm", "run", "serve"]