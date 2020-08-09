from pwn import *
#from LibcSearcher import *

#context(os='linux',arch='i386')

#elf = ELF("./pwn")
#libc_elf = ELF("./libc-2.19.so") #remote libc
#libc_elf = ELF('/lib/i386-linux-gnu/libc.so.6') #local libc

#r=process("./pwn") #local file
#r=remote("ip_address",port) #remote server

#LIBC_START_MAIN = elf.got['__libc_start_main']
#WRITE_GOT = elf.got['write']
#WRTITE_FUN = elf.plt['write']
#FUNCTION = elf.symbols['function']

#leak libc address by read/write

#payload=...

#r.recvline()
#r.send(payload)
#leaked_addr=u32(r.recv(4))
#log.info("Leaked libc address,  write: %s" % hex(leaked_addr))

#libc_elf.address = leaked_addr - libc_elf.sym["__libc_start_main"]
#BIN_SH_STR_ADDR = next(libc_elf.search("/bin/sh"))
#SYSTEM_ADDR = libc_elf.sym["system"]
#log.info("bin/sh string:%s " % hex(BIN_SH_STR_ADDR))
#log.info("system entry:%s " % hex(SYSTEM_ADDR))

#or leak libc address by DynELF

#def leak(addr):
#	
#	return leaked_data

#dynelf=DynELF(leak,elf=elf)
#SYSTEM_ADDR = dynelf.lookup('system','libc')

#get shell

#payload=...

#r.recvline()
#r.send(payload)

#r.interactive()
