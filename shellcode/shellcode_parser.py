from pwn import *
import os

SHELLCODE_ELF="./shellcode"
SHELLCODE_SRC = SHELLCODE_ELF+".s"

def str_to_hex(s):
    return r"/x"+r'/x'.join([hex(ord(c)).replace('0x', '') for c in s])

#assemble
os.system("nasm -f elf "+SHELLCODE_SRC)
os.system("ld -m elf_i386 -o "+SHELLCODE_ELF+" "+SHELLCODE_ELF+".o")

#read from elf
elf=ELF(SHELLCODE_ELF,checksec=False)
shellcode=elf.section(".text")
print("Read shellcode from elf, len:%d" % len(shellcode))
print(str_to_hex(shellcode))
