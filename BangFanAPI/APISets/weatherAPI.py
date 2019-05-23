import requests
from constconfig import *
import json
import traceback
from crawler_server import logger

def search_api(handler):
    city = handler.get_argument('city', '成都')
    url = const.WEATHER_API_URL
    data = {
        'city': city
    }
    try:
        response = requests.get(url, params=data)
        resp_json = json.loads(response.text)
        resp = {
            'code': 100,
            'msg': 'success',
            'data': resp_json
        }
        logger.info("sucess Response")
    except:
        resp = {
            'code': 101,
            'msg': traceback.print_exc()
        }
        logger.error("error Response")
    return resp
