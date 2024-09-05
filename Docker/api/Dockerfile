# Dockerfile for API service
FROM node:16

# Set working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app to the container
COPY . .

# Expose port 3000 for the API
EXPOSE 3000

# Start the API
CMD ["node", "app.js"]