import httpx
from onlinesimru import GetNumbers

from keys import onlim_api_key

numbers = GetNumbers(onlim_api_key)


def get_number(attempt=0):
    try:
        response = httpx.post("http://onlinesim.ru/api/getNum.php",
                              params={
                                  "apikey": onlim_api_key,
                                  "service": 3223,
                                  "number": True,
                                  "country": 7,
                                  "extension": False
                              }).json()
        id = response["tzid"]
        phone = response["number"]
    except Exception:
        id = None
        phone = None

    return phone, id


def get_key(id, attempt=0):
    code = None
    try:
        code = numbers.wait_code(id, timeout=5)
    except Exception:
        pass
    completed_phone(id)
    return code


def completed_phone(id):
    try:
        numbers.close(id)
    except Exception:
        pass