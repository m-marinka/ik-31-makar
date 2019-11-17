import requests
import json
import logging
from requests.exceptions import HTTPError
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as http_err:
        logging.error("Server is not available. Please, reboot server. Error: %s", http_err)
    except Exception as err:
        logging.error("Server is not available. Please, reboot server. Error: %s", err)
    else:
        data = json.loads(r.content)
        logging.info("Server is not available. Time on the server: %s", data['date'])
        logging.info("Requested page: : %s", data['current_page'])
        logging.info("Server response contains the following fields:")
        for key in data.keys():
            logging.info("Key: %s, Value: %s", key, data[key])

if __name__ == '__main__':
    while True:
        main("http://localhost:8000/health")
        time.sleep(60)
