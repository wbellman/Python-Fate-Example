
def as_int(str):
  try:
    return int(str)
  except:
    return None

def as_float(str):
  try:
    return float(str)
  except:
    return None

def get_string(prompt, chars=0):
  return input(prompt.ljust(chars) + ": ")

def get_number(prompt, chars=0, convert = as_int):
  response = get_string(prompt,chars)
  return convert(response)

def get_upper(prompt, chars=0):
  response = get_string(prompt,chars)
  return response.upper()