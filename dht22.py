import Adafruit_DHT

# Set the sensor type and the GPIO pin
sensor = Adafruit_DHT.DHT22
pin = 4  # Replace 4 with the actual GPIO pin number you've connected the DHT22 to

try:
    while True:
        # Attempt to get sensor reading
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # Print the readings if they are valid
        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.2f} °C")
            print(f"Humidity: {humidity:.2f} %")
        else:
            print("Failed to retrieve data from DHT22 sensor")

except KeyboardInterrupt:
    print("Exiting...")
