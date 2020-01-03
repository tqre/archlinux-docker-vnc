# UpCloud API-Calls
# Templatize created Arch Linux VM and deploy one while getting
# rid of the initial VM
#
# Before templatization, change the password for sudo user!

import http.client
import json
import time
from base64 import b64encode
from getpass import getpass

# Server's uuid is needed to modify it, server has to be shut down
uuid = input("Server UUID:")

user = input("Username:")
pswd = getpass("Password:")
login = b64encode((user + ":" + pswd).encode())
conn = http.client.HTTPSConnection("api.upcloud.com")
headers = {
	"Authorization"	: "Basic " + login.decode(),
	"Content-Type"	: "application/json"
}

# Change boot_options to boot from primary HD
body = open("bootfromHD.json", "r")
conn.request("PUT", "/1.3/server/" + uuid, body, headers)
print(conn.getresponse().read().decode(encoding="UTF-8"))
body.close()

# Detach installation ISO
body = open("detachISO.json", "r")
conn.request("POST", "/1.3/server/" + uuid + "/storage/detach", body, headers)
print(conn.getresponse().read().decode(encoding="UTF-8"))
body.close()

# Get the attached storage UUID from the server
conn.request("GET", "/1.3/server/" + uuid, None, headers)
response = json.loads(conn.getresponse().read().decode(encoding="UTF-8"))
storageuuid = response["server"]["storage_devices"]["storage_device"][0]["storage"]

# Templatize the storage
body = open("template_config.json", "r")
conn.request("POST", "/1.3/storage/" + storageuuid + "/templatize", body, headers)
body.close()

# Wait for the template to be created
print("Templatizing...")
time.sleep(10)

# This returns the template uuid
response = json.loads(conn.getresponse().read().decode(encoding="UTF-8"))
templateuuid = response["storage"]["uuid"]

# Editing clones.json to reflect the new template uuid
with open("clones.json", "r") as file:
	data = json.load(file)

with open("clones.json", "w") as file:
	data["server"]["storage_devices"]["storage_device"][0]["storage"] = templateuuid
	json.dump(data, file, indent=2)

# We can ditch the original server  now
conn.request("DELETE", "/1.3/server/" + uuid + "/?storages=1", None, headers)
print(conn.getresponse().read().decode(encoding="UTF-8"))

# Then start making servers out of the template
# Have to wait a bit until the template becomes available
print("Creating a clone from the template")
time.sleep(20)

body = open("template_config.json", "r")
conn.request("POST", "/1.3/server", body, headers)
print(conn.getresponse().read().decode(encoding="UTF-8"))
body.close()

conn.close()
