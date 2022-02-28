echo 'http://0.0.0.0:8080/?method=words&length=100'
echo 'http://0.0.0.0:8080/?method=characters&length=100&characterList=abcdefghijklmnopqrstuvwxyz&ban=true'

gunicorn --bind 0.0.0.0:8080 app:app