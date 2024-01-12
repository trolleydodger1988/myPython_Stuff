"""Scan for iBeacons.

Copyright (c) 2022 Koen Vervloesem

SPDX-License-Identifier: MIT
https://koen.vervloesem.eu/blog/decoding-bluetooth-low-energy-advertisements-with-python-bleak-and-construct/
"""
import asyncio
from uuid import UUID

from construct import Array, Byte, Const, Int8sl, Int16ub, Struct
from construct.core import ConstError

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

abbottID = 0xFE73
samsungIDs = [0xFD1D, 0xFD4B, 0xFD59, 0xFD5A, 0xFD69, 0xFD6C, 0xFD7E, 0xFDDB]

ibeacon_format = Struct(
    "type_length" / Const(b"\x02\x15"),
    "uuid" / Array(16, Byte),
    "major" / Int16ub,
    "minor" / Int16ub,
    "power" / Int8sl,
)


def device_found(
    device: BLEDevice, advertisement_data: AdvertisementData
):
    """Decode iBeacon."""
    try:
        # apple_data = advertisement_data.manufacturer_data[0x004C]
        # Manufacturing ID is company specific
        #abbott_data = advertisement_data.manufacturer_data[0xFE73] # or 0xFE72
        for id in samsungIDs:
            samsung_data = advertisement_data.manufacturer_data[id]
            #ibeacon = ibeacon_format.parse(abbott_data)
            ibeacon = ibeacon_format.parse(samsung_data)
            uuid = UUID(bytes=bytes(ibeacon.uuid))
            print(f"UUID     : {uuid}")
            print(f"Major    : {ibeacon.major}")
            print(f"Minor    : {ibeacon.minor}")
            print(f"TX power : {ibeacon.power} dBm")
            print(f"RSSI     : {device.rssi} dBm")
            print(47 * "-")
    except KeyError:
        # Abbott company ID (0xFE73) not found
        #print("Abbott company ID (0xFE73) not found")
        pass
    except ConstError:
        # No iBeacon (type 0x02 and length 0x15)
        print("No iBeacon (type 0x02 and length 0x15)")
        pass


async def main():
    """Scan for devices."""
    scanner = BleakScanner()
    scanner.register_detection_callback(device_found)

    while True:
        await scanner.start()
        await asyncio.sleep(1.0)
        await scanner.stop()

if __name__ == "__main__":
    asyncio.run(main())