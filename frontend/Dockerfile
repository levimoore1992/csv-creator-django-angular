### Stage 1: build ###

FROM node:12.0.0-alpine as builder

# Set working directory.
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY /package.json /package-lock.json /app/frontend/

# Install app dependencies.
RUN npm install

# Copy app files.
COPY . /app

# Build app
ENV PATH=/app/node_modules/.bin:$PATH

EXPOSE 4200

