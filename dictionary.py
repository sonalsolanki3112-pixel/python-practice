

# dictionary.py

# creat a dictionary
server = { 
   "name": "web-server-1",
   "ip": "192.168.1.10",
   "status": "running",
   "cpu": "45%"
}

# print whole dictionary
print("server info:", server)

# print one value by key
print("server name:", server["name"])
print("server ip:", server["ip"])
print("server status:", server["status"])

# add new key-value
server["ram"] = "70%"
print("after adding RAM:", server)

# loop through dictionary
print("=== full server report ===")
for key, value in server.items():
    print(key, ":", value)
