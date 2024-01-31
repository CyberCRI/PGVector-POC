# PGVector-POC
PGvector exploration


# References
https://www.youtube.com/watch?v=FDBnyJu_Ndg&list=PL-2EBeDYMIbTw2NtO8DCubf4U7q52l6il&index=3
https://www.youtube.com/watch?v=65uPqs-qttw&list=PL-2EBeDYMIbTw2NtO8DCubf4U7q52l6il&index=4

# Install
For a rapid setup
This repo requires a PostgreSQL database with vector.
 ```bash
# get the image
docker pull ankane/pgvector
# display the images
docker images
#run the docker image
docker run --name pgvector-demo -e POSTGRES_PASSWORD=test -p 5432:5432 <IMAGE_ID>
```
Just in case, you might also need
```bash
CREATE EXTENSION vector;
```
