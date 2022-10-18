build for rpi
```
docker buildx create --name multiarchbuilder
docker buildx use multiarchbuilder
apt install -y qemu-user-static
# check if arm64 is in included in architectures: docker buildx inspect --bootstrap
docker buildx build -t ncdejito/frontend:local-arm64 --platform linux/arm64/v8 --push .
docker pull ncdejito/frontend:local-arm64
```

run image
```
docker run --rm -p 3000:3000 ncdejito/frontend:local-arm64
```