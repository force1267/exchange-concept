#!/bin/bash


HELP='''
    run this script to apply all sql files in this directory to a postgres database
    ./migrate.sh localhost 5432
    or without any arguments to default to postgres:5432
    ./migrate.sh

    --wait 5          waits 5 seconds before starting

    local dev version:
    PGPASSWORD=12345678 ./migrate.sh localhost 5432

    with docker compose:
    ./migrate.sh --wait
    
    production environment:
    ./migrate.sh $HOST $PORT
'''

DEFAULT_WAIT=5
WAIT=0
POSITIONAL_ARGS=()
while [[ $# -gt 0 ]]; do
  case $1 in
    --wait)
        if [[ "$2" == "" ]]; then
            WAIT=$DEFAULT_WAIT
        else
            WAIT=$2
            shift
        fi
        shift
        ;;
    -h|--help)
      echo $HELP
      exit 0
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
    *)
      POSITIONAL_ARGS+=("$1")
      shift
      ;;
  esac
done

set -- "${POSITIONAL_ARGS[@]}"


HOST=${1:-postgres}
PORT=${2:-5432}

if [[ "$WAIT" != "0" ]]; then
    echo waiting 5 seconds for database to come up
fi
sleep $WAIT

psql --host=$HOST --port=$PORT --user=postgres -c "CREATE DATABASE exchange;"

for sql in $(ls | grep .sql); do
    echo runing $sql:
    psql --host=$HOST --port=$PORT --user=postgres --dbname=exchange --file=$(realpath $sql)
done
