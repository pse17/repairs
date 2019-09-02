FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

RUN apt-get update -yqq && apt-get -y install libfbclient2
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt



# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD uwsgi --http :8000 --module repairs.wsgi