# UpCloud API-Call to create a host Arch Linux live ISO instance
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
body = open("arch_ISO.json", "r")
conn.request("POST", "/1.3/server", body, headers)
print(conn.getresponse().read().decode(encoding="UTF-8"))
body.close()
conn.close()
