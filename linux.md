# Linux

ctrl+alt+f1/f2/f3/f4/f5/f6 新建多个终端

**1.命令语法格式： 命令 【选项】 【参数】*****

命令：告诉系统要做什么

选项：说明命令运行的方式（可以改变命令的功能）选项部分是以“ - ”开始的

参数：说明命令影响（操作）的什么（如一个文件，一个目录）

例子   ls 浏览文件    ls -l /boot

**2.whoami 命令，查看当前登录的用户**

who 查看当前登录的用户

exit 退出用户

**3.date命令 查看日期**

date ' 月日时分年‘

cal 命令 查看日历

cal  24 7 1997

**4.hwclock -s 同步硬件时间**

**5.clear 清屏 快捷键 ctrl+l**

**6.ctrl+c终止命令**

**7.su和passwd命令**

useradd + 用户名 新建用户

passwd 修改账户密码

passwd 用户名

su 切换用户 su  -  用户名

**8.man 获得命令的帮助信息**

或者命令 --help   例： useradd --help 

**9.cd 命令** 

cd .. 返回上一层

cd ~ 切换到当前用户的home目录

cd - 切换到上一次所在的目录

cd  切换到当前目录的Home目录

pwd 显示当前所在目录

ls 列出当前目录所有的文件

ls -a 显示隐藏文件

ls -l 显示长文件

 . 开头的文件都是隐藏文件

合起来 ls -al

**10 .  重要目录**

bin目录：用来放常用的可执行文件

sbin:用来存放系统的可执行文件

家目录：用来存放用户自己的文件或目录

管理员在 root文件夹中

普通用户的都在 home目录下

dev目录：存放设备文件目录

etc目录：存放配置文件目录

mnt opt media 目录

tmp 目录 临时文件目录

#### ******绝对路径和相对路径：******

绝对路径-->从头开始找，精准定位，以斜杠开头都是绝对路径  一定是完整的路径

相对路径-->相对于当前的路径，找到某个文件 不是以斜杠开始的

cp命令 拷贝文件 

cp 源文件路径 目标文件路径

cp -i   覆盖前询问   平时用的cp 都是用 alias cp= 'cp -i'alsi

cp -r 递归式拷贝  如果目标文件路径没有源文件路径中的文件夹，就会按照源文件夹递归式拷贝到目标文件路径

Cp -f 强制拷贝

mv 移动文件

mkdir 创建目录命令

mkdir -p dir2/dir1/dir0  创建一整个目录树

touch 命令 创建文件

 rm 删除文件

rm -f 没有提示直接删除

rm -r 删除目录

cat 命令 查看文件内容

head 显示头几行  head -n 可以显示前n行

tail 显示后几行  tail -n 可以显示后n行

tail -f 动态查看文件的变化（用来查看日志）

more 命令浏览文件 百分比 回车向下浏览

less 查看文件 但是不动时不加载

**权限管理：**

密码：7段

1. 用户名
2. 密码
3. user id:0 为 root用户
4. group id
5. 用户的描述信息
6. 家目录
7. 用户登录后第一条执行的命令（是否可以登录系统（/bin/bash或/sbin/nologin)）

看到26p