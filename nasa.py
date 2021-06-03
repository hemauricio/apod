from unknown import config
import requests
import json

def apod():

    r = requests.get(config.NASA_APOD_URL,
                    params={
                        "api_key": config.NASA_API_KEY
                    })

    if not r.ok:
        return {
            "message": "Unfortunately, there was an error retrieving the APOD",
            "code": r.status_code,
            "error": True
        }

    return json.loads(r.text)
