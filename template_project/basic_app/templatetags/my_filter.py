from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value,arg):

    return value.replace(arg,'')

# not using the decorator
# register.filter('cut2',cut)
