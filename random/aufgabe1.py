import zipfile

target = "challenge.zip"

while 1:
    handle = zipfile.ZipFile(target)
    handle.extractall(r"C:\Users\michi\PycharmProjects\random")
    print(handle.namelist())
    target = handle.namelist()[0]
    print(target)
