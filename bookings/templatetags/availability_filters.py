from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter(name='dictslot')
def dictslot(availability_list, target_start_time):
    if not isinstance(availability_list, list): # Check if the availability_list is a list
        return None
    for item in availability_list:
        if isinstance(item, dict) and item.get('start') == target_start_time: # Check if item is a dictionary
            return item.get('availability')
    return None

@register.filter(name='get_availability_for_court')
def get_availability_for_court(availability_data, court):
    """Gets the availability list for a specific court."""
    for item in availability_data:
        if item['court'] == court:
            return item['availability']
    return None # Return None if court not found, NOT an empty list