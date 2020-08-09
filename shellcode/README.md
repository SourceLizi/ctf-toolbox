# Shellcode手动生成脚本
依赖：pwntools，nasm，ld  
除了使用shellcraft.sh()和msfvenom外，还可以手动汇编获得shellcode。  
shellcode_parser.py可以将shellcode.s文件汇编与链接生成ELf，再将ELF中的二进制shellcode直接提取，生成的ELF可供调试  
shellcode_generator.py可以在python内直接生成对应shellcode，但无ELF
