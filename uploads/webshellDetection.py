import os
import re
import hashlib

# Hashes for known signatures.
# We can improve by storing these values in db.
webshell_signatures = {
    "hashforsomephp": "PHP webshell",
    "hashforsomeasp": "ASP webshell",
    "hashforsomejsp": "JSP webshell",
}


def detect_signature(file_path):
    with open(file_path, "rb") as file:
        file_contents = file.read()
        md5_hash = hashlib.md5(file_contents).hexdigest()

    if md5_hash in webshell_signatures:
        return True

    return False


def detect_webshell(file_path):
    # Open the file and read its contents
    with open(file_path, "r") as file:
        file_contents = file.read()

    # Check for keywords associated with ewebshells
    if re.search(r"(system|eval|base64_decode)", file_contents):
        return True

    # Check for other malicious functions
    if re.search(r"(shell_exec|exec|passthru|proc_open|popen)", file_contents):
        return True

    return False


def check_directory(directory):
    # Get a list of all files in the directory
    # os.walk(dir) returns 3-tuple: (dirpath, dirnames, filenames)
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            # Check if the file has a php extension
            if (
                file_name.endswith(".php")
                or file_name.endswith(".php3")
                or file_name.endswith(".phtml")
            ):
                file_path = os.path.join(root, file_name)
                if detect_webshell(file_path) or detect_signature(file_name):
                    print("Webshell detected in file: ", file_path)

    print("Finished checking directory: ", directory)


# Example usage
directory = "C:\Users\LG\Desktop\정보보안\자동화"
check_directory(directory)
