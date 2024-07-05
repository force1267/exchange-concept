# Example API

## how to run
on a `linux` os do:
```bash
docker compose up -d
```
this `docker compose` runs a cronjob, and to run it, docker daemon's unix socket must be `/var/run/docker.sock`. otherwise change the `docker-compose.yaml` accordingly.

## The API
The api is available at port `:8080` at `/api/buy`

## Adminer
An instance of `adminer` ui is available at port `:8081`

## Postgres
A postgresql instance populated with data from `./db_versions` is available with user:pass `postgres:12345678`
