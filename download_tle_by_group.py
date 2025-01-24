import requests
import time
import os


def download_tle_by_group(group_name):
    base_url = "https://celestrak.org/NORAD/elements/gp.php"
    params = {
        "GROUP": group_name,
        "FORMAT": "tle"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()
        # 创建文件夹 data 存放数据
        os.makedirs("./data", exist_ok=True)
        with open(f'./data/{group_name}.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"{group_name} TLE 数据下载并保存成功")
    except requests.RequestException as e:
        print(f"{group_name} 请求出现错误: {e}")
    except IOError as e:
        print(f"{group_name} 文件写入出现错误: {e}")
    time.sleep(1)


    
if __name__ == "__main__":
    group_list = ["starlink", "oneweb", "orbcomm", "globalstar", "iridium", "iridium-next"]
    for group in group_list:
        download_tle_by_group(group)
        