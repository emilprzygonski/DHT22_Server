# DHT22 Server - in progress

## General information
Welcome to my small project! The main goal is to read temperature and relative humidity, save it and then draw a diagram.

## Description
First of all I used DHT22 sensor to get informations. It was connected to Raspberry Pi 4. As soon as I started reading data in real time I created server using Flask library for Python. As I didn't want to create any database to store data from DHT22 sensor, I created "State" class that does it. I wanted to check temperature every minute and see the collection from last 12h so class "State" store data of maximum length 720. To draw dynamic graph I used javascript's Chartist library and async functions. After all, I downloaded model on RPi4 and it is running until now.

Server is working but, project is NOT finished.

On main branch - testing server with no real data, but randomly generated numbers, because I don't always have my RPi4 with me. 
On DHT22_Server - ready to download code.
