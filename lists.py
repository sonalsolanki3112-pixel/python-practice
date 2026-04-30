
# lists.py

# creat a list
servers = ["web-server-1", "web-server-2", "db-server"]

# print whole list
print("all server:", servers)

# print one item - starts from 0!
print("first server:", servers[0])
print("second server:", servers[1])

# add item to list
servers.append("backup-server")
print("after adding:", servers)

# count items
print("total servers:", len(servers))

# loop through list
print("=== checking all server ===")
for server in servers:
   print("checking:", server)
