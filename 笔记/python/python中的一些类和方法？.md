# python中的一些类和方法？

```math
\begin{align}
\left{

\right}
\end{align}
```



## list

```python
>>>list = ['a' , 'b' , 'c' , 'd']
>>>list.pop() # 返回列表末尾值并弹出
'd'
>>>list.remove('a') # 删除指定元素
>>>list.append('e') #列表末尾插入元素
>>>list.extend(['f' , 'g']) #列表末尾添加列表
>>>list
['b' , 'c' , 'e' , 'f' , 'g']
#此外，与C++不同的是，列表赋值直接绑定地址，而非值？？？
>>>list1 = list #此时无论list如何更改，二者储存相同值，占用相同地址
#但是当使用==等运算符号时根据的是具体元素而非绑定的列表地址
a == b #检查两可变序列元素是否相同
a is b #检查两可变序列是否绑定到同一可变序列
```

此外，python中可变元素作为参数的调用只在第一次调用时创建新对象，此后一直使用同一对象(也就是说，你甚至可以在一个函数内存储信息(抽象))

```python
def f(s=[]):
    s.append(3)
    return len(s)
>>>f()
1
>>>f()
2 # 没有创建新对象，也没有重新赋值导致的
```



## dictionary

```python
>>>numerals = {'I' : 1 , 'V' : 5 , 'X' : 10}
>>>numerals['X'] = 11 #可直接改变字典中键对应的键值
>>>numerals['L'] = 50 #此外，也可通过该方式直接增添键与键值
>>>numerals.pop
```

不可变序列

## taple

```python
taple = (1,2,3,4)#或taple = 1,2,3,4(括号可省略)

```

