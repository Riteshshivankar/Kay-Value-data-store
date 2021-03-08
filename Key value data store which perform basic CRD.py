import json
import time
import datetime


def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()

def Create(key,timeout):
    value = input("Enter the value: ")

    json_object[key] = [value,str(timeout)]
    json_data = json.dumps(json_object)

    with open(FileName + ".json", "w") as WriteToFile:
        WriteToFile.write(json_data)
    print("The data is added at key " + key )


def Read(key):
    if key in json_object.keys():
        timeout = json_object[key][1]
        datetime_object = datetime.datetime.strptime(timeout, '%H:%M:%S')
        if datetime_object.time() > a:
            print(key + " " + json_object[key][0] + " Expire at " + json_object[key][1])
        else:
            print("The key is expire you do not have access to read..")
            json_object.pop(key)
            json_data = json.dumps(json_object)
            with open(FileName + ".json", "w") as WriteToFile:
                WriteToFile.write(json_data)
    else:
        print("This key is not present in this file")


def Delete(key):
    if key in json_object.keys():
        timeout = json_object[key][1]
        datetime_object = datetime.datetime.strptime(timeout, '%H:%M:%S')
        if datetime_object.time() > a:
            json_object.pop(key)
            json_data = json.dumps(json_object)
            with open(FileName + ".json", "w") as WriteToFile:
                WriteToFile.write(json_data)
            print("The Key is deleted succesfully...")
        else:
            print("The key is expire you do not have access to delete..")
            json_object.pop(key)
            json_data = json.dumps(json_object)
            with open(FileName + ".json", "w") as WriteToFile:
                WriteToFile.write(json_data)

    else:
        print("This key is not present in this file")



a = datetime.datetime.now().time()
X = input("Do you want import file: (yes/no): ")
if X.lower() == "yes":
    FileName = input("Enter the file name: ")
    with open(FileName + ".json","r") as readFile:
        json_object = json.load(readFile)
        print(json_object)
else:
    FileName = input("Enter the file name: ")
    json_object = {}


while True:
    print("Enter 1 for Create , 2 for Read , 3 for Delete, 4 for Exit: ")
    x = int(input("Enter the option: "))
    if (x == 1):
        key = input("Enter the Key: ")
        if key in json_object.keys():
            print("Key is Already Present ")
        else:
            expiry_time = int(input("Enter the expiry time in seconds: "))
            b = addSecs(a, expiry_time)
            Create(key,b)

    if (x == 2):
        key = input("Enter the Key: ")
        Read(key)

    if (x == 3):
        key = input("Enter the Key: ")
        Delete(key)

    if (x == 4):
        print("Thank you...")
        break

    if (x > 4):
        print("Option not found..")
