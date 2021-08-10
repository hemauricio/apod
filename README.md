# APOD

Application that shows the APOD (Astronomy Picture Of the Day).

Powered by [Google App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard)

Browse more NASA APIs [here](https://api.nasa.gov/index.html#browseAPI)

You can deploy this yourself if you:
1. Get your own API Key to consume the NASA API.
2. Create an `unknown` folder with a `config.py` folder.

You should have the following hierarchy.
```
apod
│   LICENSE
│   README.md  
│   app.yaml    
│   main.py    
│   nasa.py    
│   requirements.txt    
│
└───templates
│   │   apod.html
│
└───unknown
│   │   __init__.py
│   │   config.py
```
3. The `config.py` file should look like this

```
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = "YOUR_API_KEY"
```
4. Then you can just run `gcloud app deploy`.
