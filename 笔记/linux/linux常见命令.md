<h1><div style="text-align:center"><span style='color:Blue'>常用命令</span></div></h1>

### Directories

> ```bash
> ls dir0 #打印指定文件夹内文件目录（后未跟文件时默认打开打印当前目录）
> ```
>
> ```bash
> mkdir dir0 #创建文件夹
> ```
>
> ```bash
> cd dir0 #打开指定目录，特别的“cd ..”返回上一级目录
> ```
>
> ```bash
> rm -r dir0 #删除指定文件夹
> ```

### Files

> ```bash
> cat file.txt #打印文件内容到屏幕上
> ```
>
> ```bash
> mv file0 file1 #将该文件/文件夹移动到另一位置
> ```
>
> ```bash
> cp file0 file1 #将该文件/文件夹复制到另一位置，不删除原文件
> ```
>
> ```bash
> rm file0.txt #删除该文件
> ```

### Miscellaneous

> ```bash
> echo 1 #打印内容到屏幕
> ```
>
> ```bash
> man rm #打开某命令的帮助页面
> ```

### Python 有关的一些小命令

> ```bash
> python3 -i lab00.py#以交互方式运行程序（此时你可以进行输入等内容，这些操作不改变文件），诸如输入操作等需要通过“-i”方式运行
> ```
>
> ```bash
> python3 -m doctest lab00.py#"-m doctest，在我们运行的文件中可能包含一些测试片段>>>，表示输出，若输出与>>>的示例一致则不显示任何输出，若出错则报错"
> ```
>
> 例子
>
> ```python
> 
> print("hello")
> >>>1#该输出正确
> >>>kill#该输出不存在，最终结果报错
> ```