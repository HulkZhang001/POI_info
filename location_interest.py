import requests
import json
import pandas as pd


def request_data(a,b):
      ak="wcyd2tuTGz394FsGbRZbGkGCszokPegi"  # 百度地图AK，需要自己申请应用
      url = "http://api.map.baidu.com/place/v2/search?query="+a+"&page_size=20&scope=1&region="+b+"&output=json&ak="+ak
      #url="http://api.map.baidu.com/place/v2/search?query="+a+"&location=22.573921,114.062175&radius=500&output=json&ak=wcyd2tuTGz394FsGbRZbGkGCszokPegi"
      params = {'page_num':0}   # 请求参数，页码
      request = requests.get(url,params=params)   # 请求数据
      total = json.loads(request.text)['total']    # 数据的总条数
      total_page_num = (total+19) // 20    # 每个页面大小是20，计算总页码
      items = []    # 存放所有的记录，每一条记录是一个元素
      for i in range(total_page_num):
            params['page_num'] = i
            request = requests.get(url,params=params)
            for item in json.loads(request.text)['results']:
                 name = item['name']
                 lat = item['location']['lat']
                 lng = item['location']['lng']
                 address = item.get('address', '')
                 street_id = item.get('street_id', '')
                 telephone = item.get('telephone', '')
                 detail = item.get('detail', '')
                 uid = item.get('uid', '')
                 new_item = (name, lat, lng, address, street_id, telephone, detail, uid)
                 items.append(new_item)

# 使用pandas的DataFrame对象保存二维数组    
      df = pd.DataFrame(items, columns=['name', 'lat', 'lng', 'adderss', 'street_id', 'telephone', 'detail', 'uid'])
      df.to_csv(a+"_"+b+"_info.csv", header=True, index=False,encoding="utf_8_sig")

