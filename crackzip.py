import sys
import zipfile

def extract_zip(zip_path, salt):
    try:
        password = "M$M@rvEl_" + salt
        print(password)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(pwd=password.encode())
            print("Extraction successful!")
            sys.exit(0)
    except RuntimeError:
        print("Incorrect password or corrupted file.")
    except FileNotFoundError:
        print("ZIP file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_alphabet_permutations(max_length=8):
    

    keyspace = ""

    def generate_permutations(current_string, length):
        if length == 0:
            extract_zip("flag.zip", current_string)
            return

        for char in keyspace:
            generate_permutations(current_string + char, length - 1)

    for length in range(1, max_length + 1):
        generate_permutations("", length)  

print_alphabet_permutations(6)  