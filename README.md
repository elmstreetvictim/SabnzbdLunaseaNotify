# SabnzbdPushbullet
Python script to send a notification for events within Sabnzbd

# Usage: 

The integrated Pushbullet support in Sabnzbd is currently lacking. The built in options leave a little to be desired. When using the default config, notification events via Pushbullet do not display what prompted the notification on the *iOS Lockscreen*. So, I cooked up this small Python program. It will notify your Pushbullet account of Sabnzbd events, along with the name of the item in the queue. 

First, sign up for Pushbullet and obtain your API key.

![](https://78.media.tumblr.com/58bc0f844e7a560e631cfaa41b678165/tumblr_inline_p577cg8Xy01vdpnpk_540.png)

Next, open `SabnzbdPushbullet.py` file in your text editor and change the API key inside the single quotes

`appToken = 'YOUR_APP_TOKEN_HERE'` - leave the single quote marks but replace `YOUR_APP_TOKEN_HERE` with the long string of characters that Pushbullet provides you.

![image](https://78.media.tumblr.com/bae8cf132f838542e75e0fe2492548d4/tumblr_inline_p5g6jsgR0M1vdpnpk_540.png)

Save the python file wherever Sabnzbd looks for scripts. You will be able to select the notification script by turning on the custom notification script option in the Sabnzbd settings.

Voila, now you will get notified the name of the job instead of a plain status message with no context.



