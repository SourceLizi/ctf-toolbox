section .text
global _start
_start:
    ;write your code here
    xor eax, eax
    push 0x0068732f ;"/sh\x00"
    push 0x6e69622f ;"/bin"
    mov ebx, esp
    push eax
    push ebx
    mov ecx, esp
    xor edx, edx
    mov al, 0xb
    int 0x80
    ret
