sudo -u postgres dropdb hacksaude
sudo -u postgres createdb hacksaude
sudo -u postgres psql -c "DROP USER IF EXISTS arise;"
sudo -u postgres psql -c "CREATE USER arise WITH PASSWORD 'arise';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hacksaude TO arise;"
exit
