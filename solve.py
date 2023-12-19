from mocr import decodeMorse
import os
import zipfile

def extract_files(level, image_file):
    while True:
        dir_path = 'flag/' * (level != 999)
        img_path = f"{dir_path}pwd.png"  # Set the image file path based on the level

        file_path = f"{dir_path}flag_{level}.zip"
        if not os.path.exists(file_path):
            print(f"\nFile '{file_path}' not found. Exiting extraction loop.")
            break  # Break the loop if the zip file doesn't exist

        password = decodeMorse(img_path)

        print(f"Extracting '{file_path}' with password: {password}")

        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            try:
                zip_ref.extractall(pwd=password.encode())  # Provide the password to extract the contents
                print(f"Extraction successful at Level {level}", end="\n\n")
                level -= 1

            except Exception as e:
                print(f"Extraction failed at Level {level}: {e}")
                break  # Break the loop if extraction fails

    print("Extraction completed.")
    flag_file = 'flag/flag' # Need to extract all zips before knowing this filename
    if os.path.isfile(flag_file):
        with open(flag_file, 'r') as f:
            print(f"\nTHE FLAG IS: {f.read()}")

if __name__ == "__main__":
    starting_level = 999
    starting_image = './pwd.png'
    extract_files(starting_level, starting_image)


