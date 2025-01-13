from django import template

register = template.Library()

@register.filter(name='dictslot')
def dictslot(availability_list, target_start_time):
    """
    Finds the availability dictionary in a list that matches the target start time.

    Args:
        availability_list: A list of dictionaries, where each dictionary has a 'start' key (time object).
        target_start_time: The time object to search for.

    Returns:
        The 'availability' value from the matching dictionary, or None if no match is found.
    """
    if not availability_list:
        return None

    for item in availability_list:
        if item.get('start') == target_start_time:
            return item.get('availability')
    return None