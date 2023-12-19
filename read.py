import smbus2
import bme280
import time
import json

I2C_address = 0x77

bus = smbus2.SMBus(1)

calibration_params = bme280.load_calibration_params(bus, I2C_address)

data = bme280.sample(bus, I2C_address, calibration_params)

temperature_celsius = round(data.temperature,2)
humidity = round(data.humidity,2)
pressure = round(data.pressure,2)
timestamp = str(data.timestamp)
data = {
    "temperature_celsius": temperature_celsius,
    "humidity": humidity,
    "pressure": pressure,
    "timestamp": timestamp
}

# Convert Python data to JSON string
json_string = json.dumps(data, indent=2)  # Optional: 'indent' for pretty formatting

# Print or use the JSON string
print(json_string)

