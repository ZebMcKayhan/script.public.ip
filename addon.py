import xbmcaddon
import xbmcgui
import requests

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

LOOKUP_URL = "https://ifconfig.co/json"

def getIpInfo():
    """Get public ip information"""
    request = requests.get(LOOKUP_URL)
    info = ""
    try:
        for key, value in request.json().items():
            info = info + "{}: {}\n".format(key, value)
    except:
        info = "some error occurred :("

    return info

info = getIpInfo()

# xbmcgui.Dialog().ok accept max 3 lines as arguments
# xbmcgui.Dialog().ok(addonname, line1, line2, line3)
xbmcgui.Dialog().ok(addonname, info)
