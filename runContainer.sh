docker run -it --name webapp -h webapp donald122/myweb
docker run -it --volumes-from webapp --name nginxapp -h nginxapp -p 8000:8000 --link webapp:webapp donald122/nginxapp
