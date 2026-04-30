# write to file
with open("servers.txt", "w") as f:
    f.write("web-server-1\n")
    f.write("web-server-2\n")
    f.write("db-server\n")
print("File created!")

# read whole file
print("\n=== file content ===")
with open("servers.txt", "r") as f:
    content = f.read()
    print(content)

#read line by line
print("==== read line by line ====")
with open("servers.txt", "r") as f:
    for line in f:
        print("server:", line.strip())

# Aeppend new server
with open("servers.txt", "a") as f:
    f.write("backup-server\n")

print("new server added!")
# read final file
print("\n=== Final content ===")
with open("servers.txt", "r") as f:
    for line in f:
        print(line.strip())

# ===== REAL DEVOPS USE CASE =====
print("\n ==== Server Health Check ====")

# read server for file
with open("servers.txt", "r") as f:
    servers = f.readlines()

# Check each server:
for server in servers:
    server = server.strip()
    if "web" in server:
        print(f"{server} - web server")
    elif "db" in server:
        print(f"{server} - Database server")
    elif "backup" in server:
        print(f"{server} - backup server")
    else:
        print(f"{server} - unknown server")