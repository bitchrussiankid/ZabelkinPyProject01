import os

if not(os.path.exists("config.txt")):
    with open("config.txt", "w") as config:
        config.write("""host=localhost
port=8080
debug=true
sldkfjh
username=admin
timeout=30""")


configDict = {}
translator = str.maketrans("", "", "\n")
with open("config.txt", "r") as config:
    for line in config:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=")
            configDict[key.strip()] = value.strip()
        else:
            print(f"Error: incorrect value in file line ({line})")

print(configDict)

for key, value in configDict.items():
    if value.isdigit() == True:
        configDict[key] = int(value)
    elif value.lower() == "true":
        configDict[key] = True
    elif value.lower() == "false":
        configDict[key] = False
    else:
        try:
            configDict[key] = str(value)
        except ValueError:
            "Error: value error"
        except Exception as e:
            "Unavailable error"

print(configDict)
print("port:", configDict["port"])