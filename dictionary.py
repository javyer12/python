# learning about dictionaries
def run():
  my_dict = {
      'key1': 1,
      'key2': 2,
      'key3': 3
  }
  for key, value in my_dict.items():
   print(key,'=', value)


if __name__ == '__main__':
  run()