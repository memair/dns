# ![alt text](https://github.com/memair/dns/raw/master/Memair%20DNS%20logo.png "Memair Logo")Memair DNS

Pseudorandomly block social media on 50% of days. Blocking occurs at the DNS level, affecting both social media websites & their apps. Social media apps will still open, however they will not have connectivity which prevents new content, notifications, etc.

Use cases:
 * Conducting A/B tests on the effect of social media
 * Noticing the influence of social media usage
 * Reducing social media usage

Private DNS: dns.memair.com  
IP DNS: 35.224.0.214

## Blocked Social Media Sites

 * Facebook
 * Imgur
 * Instagram
 * LinkedIn
 * MySpace
 * Pinterest
 * Reddit
 * Tumblr
 * Twitter

Please [create a pull request](https://github.com/memair/dns/edit/master/block.list) if you would like to block additional social media sites or domains. See the [Full Block List here](https://github.com/memair/dns/blob/master/block.list).

## Experimenting

We're currently working on a framework to make experimenting easier. Follow us on [Twitter](https://twitter.com/memair) to get updates (we will only be posting on unblocked days).

## How it works

Each day at 00:00 UTC, the state has a 25% chance of changing state from blocked to unblocked or vice versa. Details on how this is calculated can be seen in [update.py](https://github.com/memair/dns/blob/master/update.py). The status of each day in 2019 is available [here](https://github.com/memair/dns/blob/master/daily_status.txt).

## Setup

Updates to operating systems occur frequently, please [update](https://github.com/memair/dns/edit/master/README.md) these instructions if they have become outdated or are not easily understandable.

### Android 9 (Pie) or later

 1. Go to **Settings** > **Network & Internet** > **Advanced** > **Private DNS**
 2. Select **Private DNS provider hostname**
 3. Enter `dns.memair.com` as the hostname of the DNS provider
 4. Click **Save**

note: Android versions prior to 9 (Pie) do not allow system level DNS settings.

### iPhones & iPad (iOS)

Unfortunately iOS doesn't support system wide DNS settings. You can set the DNS settings for each wifi & cellular network you connect to or alternatively you can use an app like [DNS Override](https://itunes.apple.com/us/app/dns-override/id1060830093?mt=8)

### Mac OS

1. Click the **Apple Symbol** > **System Preferences** > **Network**
2. Click **Advanced** in the bottom right
3. Select the **DNS** tab
4. Remove all current DNS servers
5. Add `35.224.0.214` as your DNS server
6. Click **OK** > **Apply**

### Router

1. In your browser, enter the IP address to access the router's administration console.
2. When prompted, enter the password to access network settings.
3. Find the screen in which DNS server settings are specified.
4. If there are IP addresses specified in the fields for the primary and seconday DNS servers, write them down for future reference.
5. Replace those addresses with the `35.224.0.214`
6. Save and exit.
7. Restart your browser.

### Windows 7

1. Open Control Panel
2. Click **Network and Internet** > **Network and Sharing Center** > **Change adapter settings**
3. Right click on the network interface connected to the Internet and select **Properties**
4. If you are prompted for an administrator password or confirmation, type the password or provide confirmation
5. Select the **Networking** tab. Under *This connection uses the following items*, select Internet Protocol Version 4 (TCP/IPv4) then click **Properties**
6. Select **Use the following DNS server addresses** and enter `35.224.0.214` as the *Preferred DNS server*
7. Click **OK** & **OK**

### Windows 10

1. Open Control Panel
2. Click **Network and Internet**
3. Click **Network and Sharing Center**
4. On the left pane click **Change adaptor settings**
5. Right click on the network interface connected to the Internet and select **Properties**
6. Under *This connection uses the following items*, select Internet Protocol Version 4 (TCP/IPv4) then click **Properties**
7. Select **Use the following DNS server addresses** and enter `35.224.0.214` as the *Preferred DNS server*
8. Click **OK** & **OK**

## Contributors

A big thank you to [@jasonmwhite](https://github.com/jasonmwhite) & [@camdavidsonpilon](https://github.com/camdavidsonpilon) for letting me ([@gregology](https://github.com/gregology)) pick their brains when starting this project.
