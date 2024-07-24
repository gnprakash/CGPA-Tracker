from django import template

register = template.Library()

@register.filter
def get_range(value, end=None):
  """
  This filter takes a value (usually a number) and an optional end value.
  It returns a list of numbers from value (inclusive) to end (exclusive).
  """
  start = int(value)
  if end is None:
    end = start + 1  # Default to one more than start
  return list(range(start, end))
