# TleDownloader

本项目用于将 [celestrak](https://celestrak.org/NORAD/elements/) 网站提供 TLE 数据下载到本地文件中。


## 1. download_tle_by_group

本代码实现的功能是某个星座最新的TLE数据下载到本地文件当中。

> 快速开始

当你需要下载 [oneweb 全部卫星最新 TLE 数据页码](https://celestrak.org/NORAD/elements/gp.php?GROUP=oneweb&FORMAT=tle)

可以使用如下代码

```python
from download_tle_by_group import download_tle_by_group

download_tle_by_group("oneweb")
```


## 2. download_tle_by_kw

本代码实现的功能是搜索卫星名称中包含某个关键词的最新的TLE数据下载到本地文件当中。

> 快速开始

当你需要下载 [名字关键词是 lynk 的全部卫星最新 TLE 数据](https://celestrak.org/satcat/table-satcat.php?NAME=lynk&PAYLOAD=1&MAX=500)

可以使用如下代码

```python
from download_tle_by_kw import download_tle_by_kw
download_tle_by_kw("lynk")
```