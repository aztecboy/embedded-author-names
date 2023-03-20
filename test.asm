




section .data
Authors:
db 0x41,0x52,0x4C
db "TheHydra"
db "test0000"
db 0x00
HelloWorld db "Hello World",0
HelloWorldLen equ $ - HelloWorld
section .text
global _start 
_start:
mov rax,1
mov rdi,1
mov rsi,HelloWorld
mov rdx,HelloWorldLen
syscall
mov rax,60
mov rdi,0
syscall


