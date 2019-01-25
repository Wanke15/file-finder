import os
def look_for_file(data_dir='/', file_type=None, files=None):
    '''
    file_type: str or a tuple of str(s)
    '''
    if files is None:
        files = []
    for el in os.listdir(data_dir):
        _temp = os.path.join(data_dir, el)
        if os.path.isdir(_temp)==True:
            look_for_file(_temp, file_type, files)
        else:
            if file_type is not None:
                if _temp.endswith(file_type)==True:
                    files.append(_temp)
            else:
                files.append(_temp)
    return files

"""
print(look_for_file('test_dir'))
['test_dir\\img_dir\\dd.bmp', 'test_dir\\t1.txt']

print(look_for_file('test_dir', file_type='.jpg'))
[]

print(look_for_file('test_dir', file_type='.txt'))
['test_dir\\t1.txt']

print(look_for_file('test_dir', file_type='.bmp'))
['test_dir\\img_dir\\dd.bmp']

print(look_for_file('test_dir', file_type=('.bmp', '.txt')))
['test_dir\\img_dir\\dd.bmp', 'test_dir\\t1.txt']
"""
