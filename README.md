# SabnzbdPushbullet
Python script to send a notification after post processing finishes in Sabnzbd

# Usage: 

*This is very important -- this is not a "Notification Script", it is a Post Processing Script, so you can't configure this in the Notifications tab*

The integrated Pushbullet support in Sabnzbd is currently lacking. The built in options leave a little to be desired. When using the default config, job completion notifications don’t have any detail on what was downloaded. So, I cooked up this small Python program. It will notify your Pushbullet account when a download finishes, along with the name of the item in the queue. 

First, sign up for Pushbullet and obtain your API key.

![](https://78.media.tumblr.com/58bc0f844e7a560e631cfaa41b678165/tumblr_inline_p577cg8Xy01vdpnpk_540.png)

Next, open SabnzbdPushbullet.py file in your text editor and change the API key inside the single quotes

![](https://78.media.tumblr.com/2fc7776e25d31942adaf915279de711a/tumblr_inline_p577chp6hY1vdpnpk_540.png)

Go to your Sabnzbd web settings and visit the “Folders” page, and point to where you saved the SabnzbdPushbullet.py file

![](https://78.media.tumblr.com/fa5e68f54a360ca64e96c15d4fe41f2d/tumblr_inline_p577cg4Uay1vdpnpk_540.png)

Go to the Categories page of the Sabnzbd settings and change the script that is associated with any of your categories, or the default. 

![](https://78.media.tumblr.com/ed0788658f576f2835603296f69e0143/tumblr_inline_p577cgBHhV1vdpnpk_540.png)

Voila, now you will get notified the name of the job instead of a plain “Sabnzbd: Job complete".



