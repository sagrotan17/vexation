from django import template
import random


register = template.Library()

# Tag to create random Fador for Bootstrap Cards
@register.simple_tag
def fader():
    faderValues = ["fadeInLeft", "fadeInRight", "fadeInUp", "fadeInDown"]
    f = random.choice(faderValues)
    return f
