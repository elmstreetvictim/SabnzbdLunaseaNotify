# SabnzbdPushbullet
Python script to send a notification after post processing finishes in Sabnzbd

# Usage: 

Obtain your app token from Pushbullet.

Replace `YOUR_APP_TOKEN` with your new Pushbullet token in the python script in the `def pushbullet(stringToPush)` function, inside the single quote marks

Open your Sabnzbd configuration and navigate to the Folders tab. Determine where Sabnzbd searches for scripts.

Open the Categories tab. Set the SabnzbdPushbullet.py script on any of the categories you would like to monitor.

*This is very important -- this is not a "Notification Script", it is a Post Processing Script, so you can't configure this in the Notifications tab*

