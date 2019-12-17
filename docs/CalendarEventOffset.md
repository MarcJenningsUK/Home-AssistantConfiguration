# Google Calendar Offsets

It's not uncommon to want to be alerted to an event before it actually happens.  How do we do that with the Home Assistnt Google Calendar Event integrations?

## Set up your calendar integration

By default, once you've set up your calendar according to the [HA Docs](https://www.home-assistant.io/integrations/calendar.google/) you'll have an offset already set up.  This defaults to a setting of "!!"

By having this set you can rename the events in you calednar in the format

> Event name !!-minutesoffset

So, as an example, the event with a title of "My shiny event !!-60" would have an offset in HA of 60 minutes before the start of the "My shiny Event" event.

## OK, so how do we build that into an automation?  

It's not obvious, but if you start a new automation with a trigger type of "template", and set the template value to be 

    '{{ is_state_attr("calendar.my_calendar_name", "offset_reached", true) }}' 

That will trigger when the "offset rreached" attribute becomes true.  In other words for the example above, 60 minutes before the event starts.

## And how do we know what the event is?

To get the event title to send in the event, you don't need to do anything special to strip the offset marker off.  HA does that for you, and stores the event name in the "message" attribute.

To pull that out to, for example, a persistent notification, you can use the following YAML.

    action:
     - data_template:
         message: '{{ state_attr("calendar.my_calendar_name", "message") }}'
         title: Pats game!
       service: persistent_notification.create

