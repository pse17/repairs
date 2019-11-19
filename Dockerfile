FROM python:3.7.4-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

RUN apt-get update -yqq && apt-get install -y libfbclient2 

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 8080

# Run app.py when the container launches
# CMD uwsgi --http :8000 --module repairs.wsgi