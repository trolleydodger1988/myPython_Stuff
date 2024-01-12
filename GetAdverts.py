import asyncio
import random
from typing import Sequence

from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from bleak.backends.winrt.client import BleakClientWinRT

from bluetooth_numbers import service, company, characteristic
from bluetooth_numbers.dicts import UnknownUUIDError
from uuid import UUID

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[32m",  # Green
    "\033[35m",  # Magenta
    "\033[33m",  # Yellow
    "\033[31m",  # Red
)

async def find_all_devices_services():
    devices: Sequence[BLEDevice] = await BleakScanner.discover(timeout=5.0)

    for d in devices:
        async with BleakClient(d) as client:
            print(client.services)

async def getAdvertisements(device: BLEDevice, advertisement_data: AdvertisementData):
    #devices: Sequence[BLEDevice] = await BleakScanner.discover(timeout=5.0)
    i = random.randint(1, 5)
    deviceAddress = device.address
    localName = advertisement_data.local_name
    serviceData = advertisement_data.service_data
    manufacturingData = advertisement_data.manufacturer_data
    serviceUUIDS = advertisement_data.service_uuids
    txPower = advertisement_data.tx_power
    print(c[i] + f"Local Name, Address: {localName}, {deviceAddress}")
    print(f"ServiceData: {serviceData}")
    print(f"Manufacturing Data: {manufacturingData}")
    printManufacturer(manufacturingData)
    print(f"Service UUIDS: {serviceUUIDS}")
    printServiceCharUUID(serviceUUIDS)
    print(f"Tx Power: {txPower}")
    print( 45 * "-" + c[0])
    

def printManufacturer(manufacturingDict: dict[int, bytes]):
    for key in manufacturingDict:
        print(f"Manufacturer: {company[key]}")

def printServiceCharUUID(uuids: list[str]):
    try: 
        for uuid in uuids:
            print(service[UUID(uuid)])
            print(characteristic[UUID(uuid)])
    except UnknownUUIDError as e:
        print(f"Error, unknown UUID number: {e}")


async def main():
    """Scan for devices."""
    random.seed(4567)
    # Call back function called within the BleakScanner constructor
    # When BleakScanner detects a BLE device the call back function will be run
    scanner = BleakScanner(getAdvertisements)

    while True:
        await scanner.start()
        await asyncio.sleep(1.0)
        await scanner.stop()

if __name__ == "__main__":
    asyncio.run(main())