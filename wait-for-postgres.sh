#!/bin/sh

set -e

host="$1"
name_db="$2"
user_db="$3"
shift
cmd="$@"

until PGPASSWORD="$PASSWORD" psql -h "$host" -d "$name_db" -U "$user_db" -c '\q' 2>&1 >/dev/null; do
  >&2 echo "PostgresQL - sleeping"
  sleep 1
done

>&2 echo "PostgresQL - up"