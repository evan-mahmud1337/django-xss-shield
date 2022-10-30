from django import template
from shield.the_shield import bruter, protect


register = template.Library()

register.filter('protect', protect)
register.filter('bruter', bruter)
