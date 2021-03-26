import time

import requests

# sms_active
from keys import sms_active_key

country_codes = [0, 0, 0, 135, 0, 2, 0, 11, 0, 115, 0, 6, 0]


# sms_active
def get_number(attempt=0):
    code = 0
    try:
        code = country_codes[attempt]
    except Exception as e:
        pass
    get_key = 'https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=getNumber&service=fb&country={}'.format(
        sms_active_key, code)
    key_info = requests.get(get_key)
    # 'ACCESS_NUMBER:325929094:77715984276'
    data_sms_active = key_info.text
    print("key")

    if data_sms_active == 'NO_BALANCE':
        raise Exception('NO_BALANCE')
    if data_sms_active == 'NO_NUMBERS':
        print("NO_NUMBERS")
        time.sleep(5)
        if attempt + 1 >= len(country_codes):
            return None, None
        else:
            return get_number(attempt + 1)

    try:
        data_split = data_sms_active.split(":")
        phone = data_split[2]
        id = data_split[1]
    except Exception:
        if attempt + 1 >= len(country_codes):
            return None, None
        else:
            return get_number(attempt + 1)
    return phone, id


# sms_active
def get_status(id):
    return requests.get(
        'https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=getStatus&id={}'.format(
            sms_active_key, id)).text


# sms_active
def get_key(id, attempt=0):
    try:
        status_text = get_status(id)
        if status_text == "STATUS_WAIT_CODE":
            print(status_text)
            time.sleep(15)
            if attempt > 5:
                deactive_phone(id)
                return None
            attempt += 1
            return get_key(id, attempt)
        if "STATUS_OK" in status_text:
            completed_phone(id)
            return status_text.split(":")[1]
    except Exception as e:
        deactive_phone(id)
        return None


# sms_active
def completed_phone(id):
    try:
        requests.get(
            'https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=setStatus&id={}&status=6'.format(
                sms_active_key, id))
    except Exception:
        pass


# sms_active
def deactive_phone(id):
    try:
        requests.get(
            'https://sms-activate.ru/stubs/handler_api.php?api_key={}&action=setStatus&id={}&status=8'.format(
                sms_active_key, id))
    except Exception:
        pass
