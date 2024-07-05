# Example API

## how to run
on a `linux` os do:
```bash
docker compose up -d
```
this `docker compose` runs a cronjob, and to run it, docker daemon's unix socket must be `/var/run/docker.sock`. otherwise change the `docker-compose.yaml` accordingly.

## The API
The api is available at port `:8080` at `/api/buy`

## Request using curl
here is an example:
```bash
curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"user": 3, "crypto": "ABAN", "amount": 1}' \
    'http://localhost:8080/api/buy'
```
- `user` is user_id
- `crypto` must be a valid crypto name (currently `ABAN`, `BTC`, `USDT`)
- `amount` is the number of coins

## Adminer
An instance of `adminer` ui is available at port `:8081`

## Postgres
A postgresql instance populated with data from `./db_versions` is available with user:pass `postgres:12345678`
