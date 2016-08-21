# RaspberryPiMessenger
A Python script to DM system info over Twitter!

This repository contains a Python file called tweet.py. When run, this script will send a direct message to the account of your choice containing current OpenVPN connections and system statistics. To get an introduction, follow the tutorial [here](http://www.instructables.com/id/Raspberry-Pi-Twitterbot/), which will get you started with the Twitter API and using the Twython library on your Pi.

Once that's setup, configure the tweet.py files with the necessary API keys. Also, be sure to follow the person you'll be DMing both ways so the script can successfully send a DM. Finally, fill in the screen name of the user you will be DMing the system info to in the Twython API call towards the end of tweet.py.

To get the OpenVPN connections info working, simply change the name of the devices that are conditionally checked in the `getRecentConnections()` method. Alter the code as you wish, although it should be very flexible.

I'd recommend placing tweet.py in the `/home/pi` directory, and then setting up a crontab (which much be initiated as root) that you can find info about [here](http://www.adminschoice.com/crontab-quick-reference).

That's it! Enjoy, and feel free to submit pull requests with improvements!
