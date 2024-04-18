# WorWatch (for MacOS only)

Taking advantage of launchd plist to monitor the everyday commands.

## About `launchctl`

If the interval was changed, we need to unload and reload the service
using commands:

```shell
cd ~/Library/LaunchAgents/
launchctl unload -w com.workwatch.plist
launchctl load -w com.workwatch.plist
```
then the new interval will take effect.