FROM python:3.4
MAINTAINER donald.leung@icloud.com

# Install packages
RUN apt-get update && apt-get install -y \
    gcc \
    python-dev \
    postgresql-client libpq-dev \
    sqlite3 \
    vim net-tools \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Install python dependency
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy all source files to the container
COPY . /app/
WORKDIR /app/

# Create log and shared directory
RUN mkdir /var/log/uwsgi /shared

# Forward uwsgi logs to the docker log collector
RUN ln -s /dev/stdout /var/log/uwsgi/djangoapp.log \
    && ln -sf /dev/stdout /var/log/uwsgi/emperor.log

# Collect django static files and then copy to volume
RUN python manage.py collectstatic --noinput && \
    cp -r static /shared/

VOLUME /shared

# port
EXPOSE 20080 20081


# Start uWSGI
CMD /usr/local/bin/uwsgi uwsgi_config.ini
