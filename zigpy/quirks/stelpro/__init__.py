from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.hvac import Thermostat
from zigpy.profiles.zha import DeviceType

class StelproThermostat(CustomDevice):
    signature = {
        0x0019: {
            'profile_id': 0x104,
            'device_type': DeviceType.THERMOSTAT,
            'manufacturer': 'Stelpro',
            'model': 'ST218',
            'input_clusters': [0x0000, 0x0003, 0x0004, 0x0201, 0x0204],
            'output_clusters': [0x0402],
        },
    }

    replacement = {
        'endpoints': {
            0x0019: {
                'manufacturer': 'Stelpro',
                'model': 'ST218',
                'input_clusters': [0x0000, 0x0003, 0x0004, 0x0201, 0x0204],
                'output_clusters': [0x0402],
            }
        },
    }
