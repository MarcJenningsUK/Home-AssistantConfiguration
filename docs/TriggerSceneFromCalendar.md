#Placehold until I can write this up toimorrow.  It's too late anbd I dont want to spend too much time on it.

```
- id: '1576013979239'
  alias: Activate home calendar offset description
  trigger:
  - entity_id: calendar.home
    platform: state
    to: 'on'
  condition:
  - condition: template
    value_template: '{{ "scene" in  state_attr("calendar.home","description") }}'
  action:
  - data:
      message: Called
    service: persistent_notification.create
  - delay: 00:00:11
  - data_template:
      message: '{{ state_attr("calendar.home","description")| regex_findall_index(
        "scene.\w+", ignorecase=false) }}'
    service: persistent_notification.create
  - data_template:
      entity_id: '{{ state_attr("calendar.home","description")| regex_findall_index("scene.\w+",
        ignorecase=false) }}'
    service: scene.turn_on
```
