import csv
import numpy as np

#Q1
def read_csv_into_2d_array(file_path):
    file_path = csv.reader(open(file_path))
    data = np.array(list(file_path))
    return (data)


def find_treasure(file_path_map):
    data = read_csv_into_2d_array(file_path_map)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "x":
                return (i, j)


# print(find_treasure('treasure.csv'))

#Q2
def read_translation_guide_into_dictionary(file_path_translation):
    key={}
    data=read_csv_into_2d_array(file_path_translation)
    for i in range(len(data)-1):
        for j in range (len(data[i])):
            i1=data[i+1][0]
            j1=data[i+1][1]
            key[i1]=j1
    return (key)

# print (read_translation_guide_into_dictionary('translation.csv'))

#Q3
def read_message(file_path_message):
    with open(file_path_message, 'r') as f:
        data = (f.read())
        return (data)
def decipher_message(translation_guide, message):
    newlist = []
    translation_guide_dictionary = read_translation_guide_into_dictionary(translation_guide)
    data1 = read_message(message)
    for i in range(len(data1)):
        if not (data1[i] in translation_guide_dictionary):
            newlist.append(data1[i])
        else:
            newlist.append(translation_guide_dictionary[data1[i]])
    return (''.join(newlist))

print(decipher_message('translation.csv', 'message.txt'))

#Q4
def decrypt_map(file_path_encrypted_map, file_path_translation_guide):
    decrypted_message = decipher_message(file_path_translation_guide, file_path_encrypted_map)
    with open('decrypted_map.txt', 'w') as d:
        d.write(decrypted_message)

decrypt_map('encrypted_map.txt', 'map_code.csv')