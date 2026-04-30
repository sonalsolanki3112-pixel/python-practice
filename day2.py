# Day 2 -list and dictionaries 

# =========== LISTS ===========
servers = ["web-server:1", "web-server:2", "db-server"]

print("All servers:", servers)
print("First server:", servers[0])
print("Total servers:", len(servers))

#add server
servers.append("backup-server")
print("after adding:" , servers)

#loop throught list 
print("=== Checking servers ======")
for server in servers:
    print("checking:", server)


# ======== DICTIONARY ========
print("\n=== Dictionary Practice ===")

# Create Dictionary
server = {
   "name": "web-server-1",
   "ip": "192.163.1.10",
   "status": "running",
   "cpu": "45%"
   }

# print value
print("server name:", server["name"])
print("server ip:", server["ip"])
print("server status:", server["status"])

# add one key
server["ram"] = "70%"
print("RAM added:", server["ram"])

# loop through dictionary
print("=== Full Server Report ===")
for key, value in server.items():
    print(key, ":", value)
# =========  LIST OF DICTIONARIES =========
print("\n=== multiple servers ===")

servers = [ 
    {"name": "web-server-1", "status": "running", "cpu": "45%"},
    {"name": "web-server-2", "status": "stopped", "cpu": "0%"},
    {"name": "db-server",    "status": "running", "cpu": "78%"},
]
# loop through all servers
for server in servers:
    print(f"servers: {server['name']} | status: {server['status']} | CPU: {server['cpu']}")

# find running server 
print("\n=== Running server only ====")
for server in servers:
    if server["status"] == "running":
        print(f"{server['name']} is running")
