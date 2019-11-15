import requests

URI = "http://192.168.1.21:9000/jsonrpc.js"

data = '{"id":1,"method":"slim.request","params":["",["playlists","0",10]]}'

r = requests.post(url = URI, data = data)

data = r.json()

jsonout = '{"playlists":['

for r in data['result']['playlists_loop']:
  jsonout += '{"id":"'+ str(r['id']) +'","name":"' + r['playlist'] + '"},'
jsonout = jsonout[:-1]
jsonout += "]}"
print jsonout

data2 = '{"id":1,"method":"slim.request","params":["",["favorites","items",0,10]]}'
r = requests.post(url = URI, data = data2)

data2 = r.json()
jsonout2 = '{"favorites":['

for r in data2['result']['loop_loop']:
  jsonout2 += '{"id":"'+ str(r['id']) +'","name":"' + r['name'] + '"},'

jsonout2 = jsonout2[:-1]
jsonout2 += "]}"
print jsonout2

