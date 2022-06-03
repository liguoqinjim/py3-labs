import requests
from requests.adapters import HTTPAdapter, Retry


def lab001():
    """

    :return:
    """

    s = requests.Session()

    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])

    s.mount('http://', HTTPAdapter(max_retries=retries))

    s.get('http://httpstat.us/500')


if __name__ == '__main__':
    lab001()
