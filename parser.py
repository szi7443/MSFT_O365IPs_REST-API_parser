import requests
import uuid
import json
uid = (uuid.uuid4())

result = requests.get(f"https://endpoints.office.com/endpoints/worldwide?clientrequestid={uid}")
result_json = (result.json())
my_ip_set = set()
for i in range(0,(len(result_json))):
    try:
        current_urls = result_json[i]['urls']
        for current_url in current_urls:
            if(current_url.find('365' ) > -1 or current_url.find('outlook')>-1) :
                print(current_url)
                for q in range(0, len(result_json[i]['ips'])):

                    if '.' in result_json[i]['ips'][q]:
                        my_ip_set.add(result_json[i]['ips'][q])
                        print(result_json[i]['ips'][q])
    except:
        continue
print('-----------------------------------')
#print(my_ip_set)
for net in my_ip_set:
    print(net)