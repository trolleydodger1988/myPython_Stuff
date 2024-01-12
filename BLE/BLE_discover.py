import asyncio
from bleak import BleakScanner, BleakClient, BleakError

MODEL_NBR_UUID = "2A24"
bleAddress = "78:F2:38:C7:99:21"
uuid_battery_service = '0000180f-0000-1000-8000-00805f9b34fb'
uuid_battery_level_characteristic = '00002a19-0000-1000-8000-00805f9b34fb'
genericAccessProfile = "00001800-0000-1000-8000-00805f9b34fb"
vendorSpecific_1 = "0000fe03-0000-1000-8000-00805f9b34fb"
unknown_1 = "dc405470-a351-4a59-97d8-2e2e3b207fbb"

async def scanBLEdevices():
    # Scan for and return a list of BLE addresses
    bleDeviceAddresses = []
    devices = await BleakScanner.discover(timeout=7) # Use return_adv=True for adversisementData
    for d in devices:
        print(d.name, d.address, d.metadata)
        if len(d.metadata["uuids"]) > 0:
            #print(f"Address: {d.address}\n")
            bleDeviceAddresses.append(d.address)

    return bleDeviceAddresses


async def scanBLEAdvertisements():
    # Scan for BLE advertisements 
    devices = await BleakScanner.discover(timeout=7,return_adv=True) # Use return_adv=True for adversisementData
    for d in devices:
        # Prints the BLE address i.e., 55:5A:07:A9:08:4C
        print(d)
        # Get the services for a BLE address; not working timeout error
        # asyncio.run(await getServices(d))
        # print the AdvertismentData
        print(devices[d][1])
        # print the manufacturer_data dict of key=76
        print(devices[d][1][1].get(76))
        # Create a data variable for the value at key 76
        adv_data = devices[d][1][1].get(76)
        """
        if adv_data != None:
            decoded_adv_data = bleak.decode_advertising_data(adv_data)
            print(decoded_adv_data)
        """
        print(45 * "-")
        

async def getModelNumber(add):
    async with BleakClient(add) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))


async def getServices(add):
    bleServiceList = []
    try:
        print("Getting services...")
        async with BleakClient(add) as client:
            svcs = await client.services()
            print(f"Services for {add}:")
            for service in svcs:
                print(service)
                bleServiceList.append(str(service).split(" ")[0])
        return bleServiceList
    
    except BleakError as fuck:
        print(fuck)
        pass


async def getAttribute(add, attr):
    async with BleakClient(add) as client:
        svcs = await client.services()
        attribute_characteristic = await client.read_gatt_char(attr)
        print(int.from_bytes(attribute_characteristic,byteorder='big'))


def main():
    asyncio.run(scanBLEAdvertisements())
    addList = asyncio.run(scanBLEdevices())
    #print(addList)
    # asyncio.run(getModelNumber(addList))
    """
    for address in addList:
        asyncio.run(getServices(address))
        #asyncio.run(getAttribute(add, unknown_1))
    """
if __name__ == "__main__":
    asyncio.run(main())