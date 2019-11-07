# Home Assistant - MQTT Discovery

So I've been digging and it very much looks like there's something fishy going on, but  (at least for me) all isn't quite lost.
I set up a new WLED device, and set up MQTT.  I subscribed to the homeassistant/# topics on my MQTT broker and waited for messages to come through.  They did.
Still, nothing showed up in the MQTT integration for new devices.
I dug into the logs, and found quite a few entries saying

> "[homeassistant.components.mqtt.discovery] Component has already been discovered: light WLED_a020a6158ee8"

Restarted HA and then I saw the fateful line...

> "Found new component: light WLED_a020a6158ee8".  

Still nothing in the discovered devices, but searching for WLED2 (which was the name of the device) in the developer states tool it was there.  And set up.  And ready to go.

TL:DR - there's apparently an issue showing new devices in the integrations tab, but they do seem to show up

## Further Reading

The reason this came up for me was that I added a [WLED](https://github.com/Aircoookie/WLED) device to my network.

I updated the device from 0.8.5 to 0.8.6 and instead of updating the existing component, it added a second one.  I dug into the reason and it looks like the discovery topic has changed from 

> "homeassistant/wled_<mac address>/light/config" 
  
to  
  
> "homeassistant/<configured servername>/light/config"

Hopefully that nugget will help someone
