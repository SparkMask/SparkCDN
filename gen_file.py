import argparse
import random
import string

def generate_random_filename(length, extension=""):
  """
  Generates a random filename with the specified length and optional extension.

  Args:
    length: The desired length of the filename (excluding extension).
    extension: The desired file extension (e.g., ".txt", ".jpg"). 
               Optional, defaults to an empty string.

  Returns:
    The generated random filename with the extension.
  """

  letters_and_digits = string.ascii_letters + string.digits
  random_string = ''.join(random.choice(letters_and_digits) for _ in range(length))
  if extension:
    filename = random_string + extension
  else:
    filename = random_string
  return filename

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Generate a random filename.")
  parser.add_argument("length", type=int, help="Length of the filename (excluding extension)")
  parser.add_argument("extension", type=str, help="File extension (e.g., '.txt', '.jpg'). Optional.", nargs='?')

  args = parser.parse_args()

  random_filename = generate_random_filename(args.length, args.extension)
  print("Random filename:", random_filename)