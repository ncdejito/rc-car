Add env variable to use motor or not
```
echo export use_motor=False > .envrc
```

deploy
```
docker build -t backend:local .
kubectl create deployment backend --image=backend:local
docker save backend > myimage.tar
microk8s ctr image import myimage.tar
kubectl apply -f deployment.yml
```

run image
```
docker run --rm -p 8000:8000 backend:local
```