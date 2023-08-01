{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import Adafruit_DHT\
\
# Set the sensor type and the GPIO pin\
sensor = Adafruit_DHT.DHT22\
pin = 4  # Replace 4 with the actual GPIO pin number you've connected the DHT22 to\
\
try:\
    while True:\
        # Attempt to get sensor reading\
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)\
\
        # Print the readings if they are valid\
        if humidity is not None and temperature is not None:\
            print(f"Temperature: \{temperature:.2f\} \'b0C")\
            print(f"Humidity: \{humidity:.2f\} %")\
        else:\
            print("Failed to retrieve data from DHT22 sensor")\
\
except KeyboardInterrupt:\
    print("Exiting...")\
}