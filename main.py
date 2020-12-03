import sys
from os import path, getcwd
from time import perf_counter

def read_file(filename):
  try:
    with open(filename) as f:
        content = f.readlines()

    # I converted the file data to integers because I know 
    # that the input data is made up of numbers greater than 0
    content = [info.strip() for info in content]

  except:
    print('Error to read file')
    sys.exit()

  return content

def handle_get_info_item(item):
  """
  Expected format: n1-n2 letter: "password"
  Being n1 < n2
  """

  data_sliced = item.split(': ')

  data_part_one = data_sliced[0].split(' ')
  n1, n2 = data_part_one[0].split('-')

  return data_sliced[1], data_part_one[1], int(n1), int(n2)

def find_valid_passwords(data):
  count_valid_passwords = 0

  for item in data:
    password, letter, n1, n2 = handle_get_info_item(item)

    first_slice = password[n1 - 1]
    first_verify = (first_slice == letter)

    second_slice = password[n2 - 1]
    second_verify = (second_slice == letter)

    if (first_verify or second_verify) and (first_slice != second_slice) :
      count_valid_passwords += 1    

  return count_valid_passwords

if __name__ == "__main__":
    start_timer = perf_counter()

    filename = path.join(getcwd(), 'inputData.txt')
    input_data = read_file(filename)

    result = find_valid_passwords(data=input_data)

    print(f'Result: {result}')

    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)