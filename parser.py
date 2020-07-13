import requests
import uuid
import json
uid = (uuid.uuid4())

result = requests.get(f"https://endpoints.office.com/endpoints/worldwide?clientrequestid={uid}")
result_json = (result.json())
my_ip_set = set()
for i in range(0,(len(result_json))):
    try:
        #print(result_json[i]['urls'])
        pass
    except:
        continue
    try:
        for q in range( 0, len(result_json[i]['ips']) ):
                #print( result_json[i]['ips'][q] )
                if '.' in result_json[i]['ips'][q]:
                    my_ip_set.add(result_json[i]['ips'][q])
    except:
        continue
        """
        try:
            print(result_json[i]['urls'])
    
            for q in range(0,len(result_json[i]['ips'])):
                    print(result_json[i]['ips'][q])
        except:
            continue
        """
#print(my_ip_set)
for net in my_ip_set:
    print(net)