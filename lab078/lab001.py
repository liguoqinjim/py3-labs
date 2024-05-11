import requests
from datetime import datetime
from datetime import timedelta


def lab001():
    """
    测试API:https://api.ctrip.com/date/api/queryRangeDat/?y1=2019&m1=6&d1=18&y2=2019&m2=7&d2=18&callback=jsonp_1547876226199_62443
    """
    range_days = 365
    base_url = "https://api.ctrip.com/date/api/queryRangeDat"
    params = {
        "y1": "2019",
        "m1": "6",
        "d1": "18",
        "y2": "2019",
        "m2": "7",
        "d2": "18",
    }
    response = requests.get(base_url, params=params)
    print(response.text)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")


def is_workday(date=None):
    """
    查询日期为假日还是工作日
    """
    if date is None:
        date = datetime.now()

    base_url = "https://api.ctrip.com/date/api/queryRangeDat"
    range_days = 5
    start_date = date - timedelta(days=range_days)
    end_date = date + timedelta(days=range_days)

    params = {
        "y1": str(start_date.year),
        "m1": str(start_date.month),
        "d1": str(start_date.day),
        "y2": str(end_date.year),
        "m2": str(end_date.month),
        "d2": str(end_date.day),
    }
    response = requests.get(base_url, params=params)
    # print(response.text)
    # print(date.strftime("%Y-%m-%d"))

    if response.status_code == 200 and response.json().get("status") == 0:
        data = response.json().get("data")
        for item in data:
            if item.get("dat") == date.strftime("%Y-%m-%d"):
                if "工作日" in item.get("desc"):
                    return True
        return False
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    # lab001()
    print(is_workday())
