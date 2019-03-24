import requests
import json
import pandas as pd

guangdong=['广州','潮州','东莞','东莞','佛山','河源','惠州','江门','揭阳','茂名','梅州','清远','汕头','汕尾','韶关','深圳','阳江','云浮','湛江','肇庆','中山','珠海']
guangxi=['南宁','百色','北海','崇左','防城港','桂林','贵港','河池','贺州','来宾','柳州','钦州','梧州','玉林']
guizhou=['贵阳','安顺','毕节地区','六盘水','铜仁地区','遵义','黔西南州']
hunan=['长沙','常德','郴州','衡阳','怀化','娄底','邵阳','湘潭','益阳','永州','岳阳','张家界','株洲']
yunnan=['昆明','保山','楚雄州','大理州','德宏州','迪庆州','红河州','丽江','临沧','怒江州','普洱','曲靖','昭通','文山','西双版纳','玉溪']



def query(a,b):
      for city in b:
            ak="wcyd2tuTGz394FsGbRZbGkGCszokPegi"  # 百度地图AK，需要自己申请应用
            url = "http://api.map.baidu.com/place/v2/search?query="+a+"&page_size=20&scope=1&region="+city+"&output=json&ak="+ak
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
            df.to_csv(a+"_"+city+"_info.csv", header=True, index=False,encoding="utf_8_sig")

	


