echo 'http://0.0.0.0:8080/?method=words&length=100'
echo 'http://0.0.0.0:8080/?method=characters&length=5&characterList=abcd&character_selection_method=must&desired_entropy=11'
echo 'http://0.0.0.0:8080/?method=sentence&length=10&lang=fre&word_delimitor=_'
echo 'http://0.0.0.0:8080/?method=words&length=10&word_delimitor=_'

gunicorn --bind 0.0.0.0:8080 app:app