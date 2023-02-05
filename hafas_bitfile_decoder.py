"""
Author: http://github.com/Felix3qH4
Description:
Convert the hexadecimal values from the HAFAS 'bitfile' to binary values to see on which days a service is operating
"""

hex_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

binary_to_hex = {v: k for k, v in hex_to_binary.items()} ## Same dict as 'hex_to_binary' but inversed



def decode_hex(_hex: str, decoding_values: dict = hex_to_binary) -> str:
    """
    Decodes a given hex string to a bytes string.

    :param _hex (str) -- The hex string to be decoded to binary
    :param decoding_values (dict) -- [Optional] A dictionary containing the binary values for the hex values

    :return str -- The binary version of the hex string ex.: '1111 1110 0001'
    """

    if not isinstance(_hex, str):
        raise TypeError("Expected a string for argument '_hex' !")
    
    if not isinstance(decoding_values, dict):
        raise TypeError("Expected a dictionary to convert the hex values to binary for argument 'decoding_values' !")
    

    out: str = ""
    char_index: int = 1

    for char in _hex:
        if char.upper() in decoding_values:
            out += " " + decoding_values[char.upper()]
        
        else:
            raise ValueError(f"Invalid hex character on position {char_index}!")
        
        char_index += 1

    binary_string = out[1:] ## Remove the unnecessary whitespace at the beginning of the string

    return binary_string



def encode_binary(binary: str, decoding_values: dict = binary_to_hex) -> str:
    """
    Encodes a given binary string to a bytes string.

    :param binary (str) -- The binary string to be encoded to hex
    :param decoding_values (dict) -- [Optional] A dictionary containing the hex values for the binary values

    :return str -- The hex version of the string ex.: 'FE11'
    """
    
    if not isinstance(binary, str):
        raise TypeError("Expected a string for argument 'binary' !")

    if not isinstance(decoding_values, dict):
        raise TypeError("Expected a dict to convert the binary values to hex for argument 'decoding_dict' !")


    out: str = ""
    binary = binary.replace(" ", "")

    if len(binary) % 4 != 0:
        raise ValueError("The string you provided is no valid binary! It should contain blocks of 4 numbers! Ex.: '1111 0000 0001 0101' (whitespaces are not necessary)")

    for _index in range(0, len(binary), 4):
        binary_letter = binary[_index:_index+4]

        if binary_letter in binary_to_hex:
            out += binary_to_hex[binary_letter]

        else:
            raise ValueError(f"Invalid binary in position {_index} !")

    
    return out

    

# print(decode_hex("FE10884C"))
# print(encode_binary("1111 0000 0001 1011 1100")) 
# print(encode_binary("11110000000110111100"))      Both are valid, with or without spaces