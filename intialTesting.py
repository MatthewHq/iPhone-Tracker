import json

def main():
    data=json.load(open('requestExample.json',))

    #check if response has stores
    try:
        stores=data["body"]["PickupMessage"]["stores"]
    except:
        stores=None

    # print(stores)
    print(data["body"]==None)
    print(data["body"]["PickupMessage"]==None)
    print(data["body"]["PickupMessage"]["stores"]==None)

    if(stores != None):
        for store in range(len(stores)):
            #check if response has parts available
            try:
                parts=stores[store]["partsAvailability"]
            except:
                parts=None
            if(parts != None):
                for key in parts:
                    print("Key: ",key)
                
            


main()

