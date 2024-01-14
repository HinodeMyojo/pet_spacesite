from django import template

register = template.Library()

@register.filter
def russian_pluralize(value):
    try:
        value = int(value)
    except ValueError:
        return value
    
    if value % 10 == 1 and value % 100 != 11:
        return f"{value} год"
    elif 2 <= value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20):
        return f"{value} года"
    else:
        return f"{value} лет"