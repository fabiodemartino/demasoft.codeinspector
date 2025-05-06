# Use an official Node.js runtime as a parent image
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json first for caching dependencies
COPY package.json package-lock.json ./ 

# Install the required dependencies
RUN npm install

# Copy the rest of the frontend files into the container (including src/)
COPY . . 

# Expose the necessary port (e.g., 3000 for React app)
EXPOSE 3000

# Run the app
CMD ["npm", "start"]
