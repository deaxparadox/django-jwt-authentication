FROM node:20-alpine

# set work directory
WORKDIR /frontend


# copy project
COPY public/ .
COPY src/ .
COPY package.json .


# RUN npm install --global npm@10.4.0
RUN npm install
# RUN npm audit
# RUN npm audit fix --force