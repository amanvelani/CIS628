# Download base image node 21.4.0
FROM node:21.4.0
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file to the working directory
COPY . .
# Install the Python dependencies
RUN npm install
RUN npm run build
RUN npm install -g @angular/cli
# Expose the port on which the Flask app will run
EXPOSE 4200
ENV NG_CLI_ANALYTICS=false
# Set the entrypoint command to run the Flask app
CMD ["ng", "serve", "--host", "0.0.0.0"]
