import requests

api = 'http://127.0.0.1:1000/dy_sign'

def call_seven_shen(params_json):

    try:

        response = requests.post(url=api, data=params_json, verify=False)

    except Exception:

        return None

    return response.text