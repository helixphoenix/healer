#!/bin/bash
# run as root

#[ "$USER"= "root"] || exec sudo "$0" "$@" ]

# Assumed mac user

echo " *** $BASH_SOURCE on $(hostname -f) at $(date)" >&2
sudo passwd postgres

echo start the postgres

brew services start postgresql

echo creating db and user
create_db="$(<"db.sql")"

if ! command -v psql > /dev/null; then
  echo "Please install postgress"
  exit 1
fi 
echo "almost there"
psql postgres -c "${create_db}"
