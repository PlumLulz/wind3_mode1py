# This is the (mode=1) algorithm of zcfgBeWlanGenDefaultKey_Wind from libzcfg_be.so in the VMG8828 firmware.
# not sure about the format of the input hash, could also be some other hexadecimal string.
# much thanks to Selenium on the hashkiller forum for getting the library cross-compiled and running inside QEMU.
# so far no router is actually using this algorithm to generate the default WIFI password.

import hashlib
import argparse

def wind3_mode1(serial, mac, pwd_len, input_hash):

	if input_hash == None:
		md5 = hashlib.md5()
		md5.update(serial.encode())
		input_hash = md5.hexdigest()
		
	half_len = int(pwd_len / 2)
	char_multiple = mac[11-half_len]
	multiplier = int(char_multiple, 16)

	password = ""

	for i in range(half_len):
		mac_char = mac[i+12-half_len]
		mac_value = int(mac_char, 16)
		
		sn_char = serial[i+13-half_len]
		sn_value = int(sn_char, 16)
		
		hash_byte_a = input_hash[(i)*4:2+(i)*4]
		hash_byte_b = input_hash[2+(i)*4:4+(i)*4]

		hash_byte_value_a = int(hash_byte_a, 16)
		hash_byte_value_b = int(hash_byte_b, 16)
		hash_value = hash_byte_value_a * 16 + hash_byte_value_b - 17 * 48

		new_value = multiplier * mac_value + sn_value + hash_value
		new_value = new_value & 255
		new_value = hex(new_value)[2:].upper()

		password += new_value

	char1_source = 257 * ord(mac[1])
	char1_pos = char1_source % 7
	charset = '3456789'
	char1 = charset[char1_pos]
	password = char1 + password[1:].lower()

	print(password)


parser = argparse.ArgumentParser(description='(mode=1) algorithm of zcfgBeWlanGenDefaultKey_Wind from libzcfg_be.so in the VMG8828 firmware')
parser.add_argument('serial', help='Serial Number.')
parser.add_argument('mac', help='Mac address.')
parser.add_argument('-input_hash', help='Input hash.')
parser.add_argument('-pwd_len', help='Password length.', default=16, type=int)
args = parser.parse_args()

wind3_mode1(args.serial, args.mac, args.pwd_len, args.input_hash)