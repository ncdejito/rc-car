Add env variable to use motor or not
```
echo export use_motor=False > .envrc
```

build for rpi4
```
poetry export -f requirements.txt --output requirements.txt --without-hashes
docker buildx create --name multiarchbuilder
docker buildx use multiarchbuilder
apt install -y qemu-user-static
# check if arm64 is in included in architectures: docker buildx inspect --bootstrap
docker buildx build -t ncdejito/backend:local-arm64 --platform linux/arm64/v8 --push .
docker pull ncdejito/backend:local-arm64
```

run image
```
sudo docker run --rm -p 8000:8000 -e "use_motor=False" ncdejito/backend:local-arm64
```