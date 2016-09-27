FROM nginx:latest


RUN apt-get update && apt-get install -y \
    vim \
    net-tools \
    --no-install-recommends && rm -rf /var/lib/apt/list/*

COPY . /app/
WORKDIR /app/

RUN cat /app/DonProfile_nginx.conf > /etc/nginx/conf.d/default.conf
EXPOSE 8000

CMD nginx -g 'daemon off;'
