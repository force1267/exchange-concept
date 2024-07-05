FROM postgres:latest

WORKDIR /versions

COPY . .

ENTRYPOINT [ "bash", "migrate.sh" ]
