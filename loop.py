# loop.py

# for loop - over a list
print("=== FOR LOOP ===")
for i in range(1, 6):
    print("Number:", i)

# for loop - over a list
print("=== My servers ===")
servers = ["web server-1", "web server-2","db-server"]
for server in servers:
   print("checking:", server)

# while loop - condition 
print("=== countdown ===")
count = 3
while count > 0:
  print(count, "...")
  count = count - 1
print("done!")
