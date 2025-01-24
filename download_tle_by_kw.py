import requests
import time
import os
import re


def download_tle_by_kw(keyword: str):
    domain_url = "https://celestrak.org/"
    base_url = domain_url + "satcat/table-satcat.php"
    params = {
        "NAME": keyword,
        "PAYLOAD": "1",
        "MAX": "500",
        
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(base_url, params=params, headers=headers)
    # print(response)
    # print(response.text)
    page_content = response.text
    base_url = domain_url + "NORAD/elements/gp.php"
    pattern = r'/NORAD/elements/gp\.php\?CATNR=(\d+)'
    sat_id_arr = re.findall(pattern, page_content)
    # print(sat_id_arr)
    data_str_list = []
    for sat_id in sat_id_arr:
        p = {
            "CATNR": sat_id,
        }
        try:
            response = requests.get(base_url, params=p, headers=headers)
            print(response.text)
            data_str_list.append(response.text)
        except requests.RequestException as e:
            print(f"{keyword}/{sat_id} 请求出现错误: {e}")
        time.sleep(0.5)
    # 创建文件夹 data 存放数据
    os.makedirs("./data", exist_ok=True)
    with open(f'./data/{keyword}.txt', 'w', encoding='utf-8') as f:
        f.writelines(data_str_list)
    
        

if __name__ == "__main__":
    download_tle_by_kw("lynk")
    download_tle_by_kw("spacemobile")