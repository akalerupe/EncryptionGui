import pandas as pd

encryptionKey=pd.read_csv(r<"/home/akal/Documents/EncryptionGui/decodekeynew.csv>",
                          sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

data_frame=DataFrame(data=encryptionKey)
data_frame['Character'] = data_frame['Character'].astype(str)
data_frame['Byte'] = data_frame['Byte'].astype(str)

def split(message):
    return [char for char in message]

message = '' 

message_split = split(message)


def encrypted_message():
    encrypted_message=""
    for character in range(len(message_split)):
        result=message_split[character]
        try:
            coded_char = encryptionKey.loc[encryptionKey['Character'] == result, 'Byte'].iloc[0]
        except:
            print('unrecognized character')
            coded_char = '@@@'
        encrypted_message = encrypted_message + coded_char
    return encrypted_message