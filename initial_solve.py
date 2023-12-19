from mocr import decodeMorse
import zipfile

def main():
    level = 999
    image_file = './pwd.png'
    password = decodeMorse(image_file)
    file_path = f"flag_{level}.zip"

    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        try:
            print("Current Password: ", password)
            zip_ref.extractall(pwd=password.encode())  # Provide the password to extract the contents
            print("Extraction successful at Level ", level)
            level -= 1
        except Exception as e:
            print("Extraction failed: ", e)

if __name__ == "__main__":
    main()
