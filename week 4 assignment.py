def fileHandle(filename, content):
    pre_data = ""
    post_data = ""
    try:
        with open(filename, 'r') as file:
            pre_data = file.read()
    except FileNotFoundError:
        pre_data = "File did not exist before."

    with open(filename, 'w') as file:
        file.write(content)

    with open(filename, 'r') as file:
        post_data = file.read()

    return pre_data, post_data


file_name = input('Please enter the name of the file: ')
content = input('Please enter what you want to write: ')
# try:
result = fileHandle(file_name, content)
print(f'File before editing: {result[0]}')
print(f'File after editing: {result[1]}')
# except Exception as e:
    # print(f'An error occurred: {e}')
