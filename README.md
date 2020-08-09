# ctf-toolbox
一些CTF相关的小工具的合集
## maze_run
依赖：tkinter  
一些逆向题中可能有符号组成的迷宫，这个工具可以记录dump下来的迷宫图的路线。
将迷宫图放入下方大文本框中，用四个方向键控制光标走完整个迷宫，上方的小文本框中就会出现用wasd代表的四个方向的数据，esc键清除内容
## img_solve
依赖：PIL  
显示二进制文件保存在内存中的图片数据。确定图片尺寸大小，将图片数据dump下来保存为img_dump.mem文件，执行脚本即可显示
## arm_dbg
依赖：unicorn，capstone  
不限平台的arm二进制调试器，导入代码请修改THUMB变量  
支持的命令：  
```
 set reg <regname> <value>  
 set bpt <addr>  
 n[ext]  
 s[etp]  
 r[un]  
 dump <addr> <size>  
 list bpt  
 del bpt <addr>  
 stop  
 a/t arm/thrumb切换  
 f 显示指令流  
```
## pwn_libcleak_template，pwn_template
依赖：pwntools  
pwn脚本模板  
## burforce-VM
依赖：angr  
虚拟机混淆的爆破解法脚本  
