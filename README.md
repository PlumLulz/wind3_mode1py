# wind3_mode1py
(mode=1) algorithm of zcfgBeWlanGenDefaultKey_Wind from libzcfg_be.so in the VMG8828 firmware.

This is the (mode=1) algorithm of zcfgBeWlanGenDefaultKey_Wind from libzcfg_be.so in the VMG8828 firmware.\
not sure about the format of the input hash, could also be some other hexadecimal string.\
much thanks to Selenium on the hashkiller forum for getting the library cross-compiled and running inside QEMU.\
so far no router is actually using this algorithm to generate the default WIFI password.\

Usage: python3 wind3_mode1.py S090Y87654321 abcdef123456 -input_hash 00112233445566778899aabbccddeeff -pwd_len 16

Credit to drsnooker for his Matlab script that this was converted from: https://forum.hashkiller.io/index.php?threads/unpublished-wpa-key-algorithms.19944/post-342096
