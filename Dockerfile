FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

RUN apt-get update -yqq && \
    apt-get install -y \
        libfbclient2 \
        nginx \
        supervisor

COPY nginx_app.conf /etc/nginx/sites-available/default
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY supervisor_app.conf /etc/supervisor/conf.d/

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
# CMD uwsgi --http :8000 --module repairs.wsgi
CMD ["supervisord", "-n"]