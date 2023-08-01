Here's the step-by-step guide for setting up the DHT22 sensor on a Raspberry Pi without an LCD screen, presented in a cleaner format:

Setting up DHT22 Sensor on Raspberry Pi Without LCD Screen

Step 1: Update the Raspberry Pi

Power on your Raspberry Pi and open the terminal.
 Run the following command to update the package lists:


    sudo apt update

Step 2: Upgrade the Raspberry Pi

After the update is complete, run the following command to upgrade the installed packages:


    sudo apt upgrade

Reboot the Raspberry Pi after the upgrade:

    sudo reboot

Step 3: Configure the Raspberry Pi

To configure the Raspberry Pi settings, run the following command:

    sudo raspi-config

Use the arrow keys to navigate and select "Interfacing Options."
Select "I2C" and choose "Yes" to enable the I2C interface.
Select "SPI" and choose "Yes" to enable the SPI interface (required for some LCD modules).
Select "GPIO" and choose "Yes" to enable the GPIO interface.
If prompted to reboot, select "Yes" to apply the changes and reboot your Raspberry Pi.

Step 4: Install Necessary Drivers

Install the necessary driver for the I2C interface used by the LCD module:

    sudo apt install python3-smbus i2c-tools

Step 5: Clone the GitHub Repository

On your Raspberry Pi, open the terminal.
Clone the GitHub repository containing the DHT22 Python script:

    git clone https://github.com/wrabaa/dht22_sensor.git

Step 6: Navigate to the Project Directory

Change to the dht22_sensor directory where the Python script is located:

    cd dht22_sensor

List the files in the directory:

    ls

You will find the dht22.py file in the list.

Step 7: Run the Python Script

 Now, run the Python script using the following command:

    python3 dht22_sensor.py

The script will start reading temperature and humidity from the DHT22 sensor and display the data in the terminal.

Step 8: Verify the Functionality
Verify that the sensor readings are displayed correctly in the terminal. If everything works as expected, it means the setup and installation process from the GitHub repository is successful.

    To exit the program, press Ctrl + C.

Congratulations! You have now successfully set up the DHT22 sensor on your Raspberry Pi without an LCD screen
