# UpCloud API-Calls
# Configure Arch Linux cloud settings after arch_host_install script
import http.client
from base64 import b64encode
from getpass import getpass

user = input("Username:")
pswd = getpass("Password:")
login = b64encode((user + ":" + pswd).encode())
conn = http.client.HTTPSConnection("api.upcloud.com")
headers = {
"Authorization"	: "Basic " + login.decode(),
"Content-Type"	: "application/json"
}

# Server's uuid is needed to modify it
uuid = ""

# Change boot_options to boot from primary HD
# Display adapter is Cirrus?
body = open("bootfromHD.json", "r")
conn.request("PUT", "/1.3/server/" + uuid, body, headers)
print(conn.getresponse().read().decode(encoding="UTF-8"))
body.close()

# Detach installation ISO
body = open("detachISO.json", "r")
conn.request("POST", "/1.3/server/" + uuid + "/storage/detach", body, headers)
print(conn.getresponse().read().decode(encoding="UTF-8"))
body.close()

# Start the server
conn.request("POST", "/1.3/server/" + uuid + "/start", None, headers)
print(conn.getresponse().read().decode(encoding="UTF-8"))

conn.close()
