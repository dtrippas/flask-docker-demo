# various docker commands for building, tagging running
docker build -t flask-docker-demo:0.0.1 .
docker tag flask-docker-demo:0.0.1 dtrippas/flask-docker-demo:0.0.1
docker push dtrippas/flask-docker-demo:0.0.1
docker build -t flask-docker-demo:0.0.2 .
docker run -p 8000:8000 -d flask-docker-demo:0.0.1
docker build -f multistage.Dockerfile -t flask-docker-demo-small:0.0.1 .
docker run -p 8000:8000 -d flask-docker-demo-small:0.0.1

# make github repo
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/dtrippas/flask-docker-demo.git
git push -u origin master