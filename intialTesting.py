import json

def check(entry):
    try:
        ret=entry
    except:
        ret=None
    return ret

def main():
    data=json.load(open('requestExample.json',))

    #check if response has stores
    stores=check(data["body"]["PickupMessage"]["stores"])

    # print(stores)
    # print(data["body"]==None)
    # print(data["body"]["PickupMessage"]==None)
    # print(data["body"]["PickupMessage"]["stores"]==None)

    if(stores != None):
        for store in range(len(stores)):
            #check if response has parts available
            parts=check(stores[store]["partsAvailability"])
            if(parts != None):
                for part in parts:
                    print("==============================")
                    print(parts[part]["pickupDisplay"]," - ",(str)(parts[part]["storePickupProductTitle"].replace("Â","")))
                    #check if response has address available
                    address=check(stores[store]["address"])
                    if(address != None):
                        fullAddress=""
                        for line in address:
                            if address[line]!= None:
                                fullAddress+= address[line]+" "
                    print(fullAddress)
                

            
                    
                
            


main()

