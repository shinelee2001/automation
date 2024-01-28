from flask import Flask, render_template, request
import os, hashlib, re, openpyxl
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/webshell_analyzer", methods=["POST"], endpoint="webshell_analyzer")
def websehll_anaylzer():
    file = request.files["file"]
    file_name = file.filename
    file_path = os.path.join("uploads", file_name)
    file.save(file_path)

    # Check if file is a web shell
    web_shell_strings = ["base64_decode(", "exce(", "system(", "cmd"]
    is_web_shell = "Malware Not Detected"
    with open(file_path, "r") as f:
        contents = f.read()
        for web_shell_string in web_shell_strings:
            if web_shell_string in contents:
                is_web_shell = "Malware Detected!!!"
                break

    # Check file hash value
    file_hash = "not defined"
    with open(file_path, "r") as f:
        hasher = hashlib.sha1()
        content = f.read()
        hasher.update(content.encode("utf-8"))
        file_hash = hasher.hexdigest()

    # Check file type
    file_type = file.content_type

    # Check the file creation and file access times
    file_ctime = datetime.fromtimestamp(os.path.getctime(file_path))
    file_atime = datetime.fromtimestamp(os.path.getatime(file_path))

    return render_template(
        "malware_check.html",
        file_name=file_name,
        file_hash=file_hash,
        is_web_shell=is_web_shell,
        file_type=file_type,
        file_ctime=file_ctime,
        file_atime=file_atime,
    )


@app.route("/email_analyzer", methods=["POST"])
def email_analyzer():
    file = request.files["file"]
    file_name = file.filename
    file_extension = file_name.split(".")[-1]
    file_path = os.path.join("uploads", file_name)
    file.save(file_path)

    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    emails = []

    if file_extension == "xlsx":
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active
        for row in sheet.iter_rows():
            for cell in row:
                match = re.search(email_pattern, str(cell.value))
                if match:
                    emails.append(match.group())
    elif file_extension == "txt":
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            matches = re.findall(email_pattern, content)
            emails = list(set(matches))

    return render_template("email_check.html", file_name=file_name, emails=emails)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
