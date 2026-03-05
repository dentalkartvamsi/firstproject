import datetime

print("Hello from Python script")

current_time = datetime.datetime.now()

print("Script executed at:", current_time)

with open("test_log.txt", "a") as f:
    f.write(f"Script executed at {current_time}\n")
