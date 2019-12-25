#
# This won't run in the python scripts folder since it uses imports
# I've set it up on my data node to run every ten minutes
# since it uses http requests, location doesn't matter
#

import requests
import json

lms_url = "http://192.168.3.221:9000/jsonrpc.js"
lms_body = "{\"id\":1,\"method\":\"slim.request\",\"params\":[\"\",[\"playlists\",0,10]]}"
lms_header={"Accept": "application/json", "Content-Type": "application/json"}
ha_url = "http://192.168.3.2:8123/api/services/input_select/set_options"
ha_token="Bearer <token here>"
ha_entity = "input_select.playlists"
ha_header = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": ha_token}
ha_array = ["dummy"]
ha_array.clear()
ha_body = { "entity_id": ha_entity, "options": ha_array }

lms_response = requests.post(lms_url, data=lms_body, headers=lms_header)
json_response = lms_response.json()
for l in json_response["result"]["playlists_loop"]:
    ha_array.append("[" + str(l["id"]) + "] " +l["playlist"])

for s in ha_array:
    print(s)

ha_response = requests.post(ha_url, json=ha_body, headers=ha_header)
print(ha_response.status_code)
