![ezgif com-video-to-gif](https://user-images.githubusercontent.com/60979458/111596012-f43d9500-87e1-11eb-9b58-f8d23c3691a8.gif)
# Django-Weather-App

Django app using openweathermap.org API. (Django is big for this project, but it's just for my resume)<br />
Back-End: [Mohsen](https://github.com/Mohsen-Khodabakhshi)<br />
Front-End: [Mehran](https://github.com/Mehranlip)

## Usage

It works in Python3.

First:
```bash
git clone https://github.com/Mohsen-Khodabakhshi/Django-Weather-App.git
cd Django-Weather-App
pip install -r requirements.txt

```

settings.py:
```python
...
# You must create account in openweathermap.org to get appid or API_KEY.
WEATHER_API_KEY = <yourAppIdHere>
...
```

End:
```bash
./manage.py runserver
```

It's better if make virtualenv.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
You can fork and do changes then send pull request.

## License
[MIT](https://choosealicense.com/licenses/mit/)
