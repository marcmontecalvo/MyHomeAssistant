"""Turn off devices that are on unless ignored."""

# Use the following JSON to ignore a particular item that is on
#{
#"entities_ignore": "switch.master_bedroom_light"
#}

ignore = data.get("entities_ignore","fan.mbr_fan_level").split(",")
domains = ['light','switch','fan','media_player']
device = []

for domain in domains:
    for entity_id in hass.states.entity_ids(domain):
        state = hass.states.get(entity_id)
        if state.state == 'on' and entity_id not in ignore:
            device.append(state.entity_id)

if device:
    data = { "entity_id" : device }
    hass.services.call('homeassistant', 'turn_off', data)