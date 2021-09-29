This repository hosts most (if not all) course material for **ENGR 3421: Robotics 1** in Fall, 2021. Find lecture slides in folders named after dates. The useful technical resources can be found in this `README` file. 

# Technical Resources

## LiPo Battery
A.K.A. Lithium Polymer battery. It is powerful. It is efficient. **IT IS DANGEROUS**. Please read through this [guide](https://rogershobbycenter.com/lipoguide) before you use it.

![lipo_numbers](https://github.com/linzhangUCA/robotics1-2021/blob/main/images/lipo_numbers.jpeg)

Note:
1. Use a LiPo battery charger with a balancing module.
2. **NEVER** Leave a Battery Charging Unattended!
3. The safest charge rate is the capacity of battery in Amps.
4. A LiPo cell should NEVER be discharged below 3.0V.
5. Don't throw your LiPo battery in the trash after discharging it - seek out a recycler.

## Remote access via VNC
Refer to this [article](https://www.makeuseof.com/raspberry-pi-set-static-ip/) for setting up static ip address for your RaspberryPi.
And this [guide](https://magpi.raspberrypi.org/articles/vnc-raspberry-pi) for VNC Viewer style remote accessing. 
1. Set Static IP Address
Edit `/etc/dhcpcd.conf` with the following property configured
```bash
interface NETWORK  # "NETWORK": eth0 for wired connection, wlan0 for wireless
static ip_address=STATIC_IP/24  # "STATIC_IP": e.g. 192.168.0.111
static routers=ROUTER_IP  # "ROUTER_UP": usually change the last segment in "STATIC_IP" to 1
static domain_name_servers=DNS_IP  # "DNS_IP": find in /etc/resolv.conf
```
2. Enable VNC
In Raspbian, click the applications menu icon (raspberry) at the top-left of the screen and select **Preferences** > **Raspberry Pi Configuration**. In **Interfaces** tab, set VNC to Enabled. Click OK.
> If you haven’t changed Raspbian’s password from the default ‘raspberry’, now is a good time to do so. 
3. Download VNC Viewer
[https://www.realvnc.com/en/connect/download/viewer/](https://www.realvnc.com/en/connect/download/viewer/) on your laptop or personal computer.
4. Remote Control
Enter the IP address of your Raspberry Pi into the search bar of VNC Viewer (the part saying ‘Enter a VNC Server address or search’). Press RETURN to connect to Raspberry Pi.
The first time you do this, a window will appear with a warning: ‘VNC has no record of connecting to this VNC Server so its identity cannot be checked’. Click Continue.
You need to enter the username (typically ‘pi’) and password for your Raspberry Pi. 

