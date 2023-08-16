import os

def read(filePath='',option=''):
    if filePath == None or option == None :
        return False 
    elif option  not in ['read','readline','readlines']:
        return False
    elif os.path.isfile(filePath):
        with open(filePath, 'r') as file:
            content = eval(f'file.{option}()') 
            return content
    else:
        return False


def write(filePath='',content=''):
    if filePath == None or content == None :
        return False
    else:
        try:
            with open(filePath, "w") as file:
                file.write(content)
        except:
            return False