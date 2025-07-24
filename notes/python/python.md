<h1><span style = "color:blue">python</span></h1>

## Something to care
1. 赋值顺序
>a , b = c , d 
该表达式优先计算 c , d 二表达式后进行赋值

2.函数与简单的内置语句(if)等的区别:

```python
if只有在条件成立时才会
```

3.and&or

> 与C++相同，在能够判断出表达式结果后不会对后续表达式进行评估
>
> ex. 1 < 0 & sqrt(-4)    不会报错

4.标准交互式环境中字符串输出为‘内容’（单引号必须有）

5.print的返回值为None

6.sum函数可以对列表的列表求和：

```python
>>>sum([[0 , 1] , [2 , 3]],[])#当然，需要指定求和起始值为空列表
[0 , 1 , 2 , 3]
```



### Some specific languages

**一、**接受任意数量的参数

> 可使用**\*args**(arguments)指代和引用任意数量的参数，ex:
> ```python
def printed(f):
    	def print_and_return(*args):  #这是一个可以带入任意数量参数的函数
			result = f(*args)  # 引用上文的*args作为参数
			print('Result:', result)
		return result
	return print_and_return
	```

**二、**and 和 or

> 与C++不同，python中and和or返回的并非逻辑值，而是**最后处理的操作数**，如下：
>
> ```python
> 1 or 2 # 返回1
> 1 and 2 # 返回2
> 0 or 3 #返回3
> 0 and 3 #返回0
> ```
>

**三、**assert

> **assert** + bool表达式+ ,"错误信息"（有个小逗号）
>
> 在bool表达式不成立时终止，给出错误信息
>
> ```python
> assert 1 > 2 , "1 is not bigger than 2"
> ```

**四、**lambda表达式（匿名函数）

>基本语法
>
>```python
>lambda arguments: expression
>```
>
>arguments中可含多个参数（用逗号隔开）
>
>expression只能是单个表达式
>
>```python
>add = lambda a , b : a + b # 不使用return语句返回
>```
>
>这是一个按字符串长度排序的例子
>
>```python
>words = ["apple", "zoo", "banana", "kiwi"]
>sorted_words = sorted(words, key=lambda s: len(s))
>print(sorted_words) 
># 输出: ['zoo', 'kiwi', 'apple', 'banana']
>```
>lambda无函数名（如def add()具有函数名add）

**五、**List列表

> 定义语法
>
> ```python
> list = [3//2 , 4 , 5] #列表会优先对其内元素进行运算后进行定义
> ```
>
> 元素获取
>
> ```python
> list[1]# 当索引不存在时会给出第一个元素的值
> getitem(list , 1)
> ```
>
> 列表合并和重复
>
> ```python
> 合并：list1 + list2
> 重复：list * n
> 同时，operator中的add和mul同样适用
> ```
>
> 此外，列表元素多样，例如
>
> ```python
> list = [[1 , 2] , 3 , 4]
> >>>list[1]
> [1 , 2]
> ```
>
> 查找元素是否位于列表中
>
> ```python
> >>>list=[[1 , 2 ] , 3 , 4]
> >>>[1 , 2] in list #可用于判断列表等是否位于列表中
> True
> >>>[3 , 4] in list#不可用于判断连续元素是否位于列表
> False
> >>>'3' not in list
> True
> #此外，in仅检查列表当层元素，嵌套过深无法检测
> ```
>
> 使用for进行的序列迭代
>
> ```python
> for <name> in <expression>
> 	<suit>
> 首先评估<expression>是否为可迭代表达式
> for x in [1 , 2 , 3 , 4]:
> for x , y in [[1 , 2] , [3 , 4] , [5 , 6]] #这里[x,y]依次绑定其中每个列表
> #这个语法真的很奇怪
> ```
>
> 列表推导
>
> ```python
> #语法：
> [<elements> <conditions>]
> odds = [1 , 3 , 5 , 7 , 9]
> >>>[x + 1 for x in odds]
> [2 , 4 , 6 , 8 , 10]
> >>>[x for x in odds if 25 % x == 0]
> [1 , 5]
> #python里的这些神奇的后置条件语法真的抽象
> ```
>
> 列表剪切
>
> ```python
> list[start:end]
> #获取一个包含list中start(含)到end(不含)的列表
> #省略start或end则默认从开头读取或读取至末尾
> odds = [1 , 2 , 3 , 4]
> >>>odds[1:3]
> [2,3]
> >>>odds[:3]
> [1,2,3]
> 
> ```

列表迭代

>sum函数：用于迭代整个列表求和
>
>```python
>sum(iterable , start)or sum(iterable)
>#start用于指定初始值的类型和值，若iterable中元素类型与start不同则报错
>#若省略start默认为数字0
>#将list中元素依次进行start = start + iterable[i]直至迭代整个序列
>```
>
>max函数：根据给定函数计算元素的值，得出最大值
>
>```python
>max(iterable [, key = function])
>max(a,b,c,... [, key = function])
>
>```
>
>all函数：判断iterable中元素是否均为真值
>
>```python
>all(iterable)
>>>>all([True , False , True])
>False
>```
>
>此外，还有min和any函数，用法对应max和all

**六、**range序列

> 获取：
>
> ```python
> range(x , y)#获取一个从x（含）开始，到y(不含)结尾的整数序列
> range(y)#获取一个从0(含)开始，到y(不含)结尾的整数序列
> ```
>
> range可通过[]直接引用,这方面性质与list一致
>
> ```python
> range(2,4)[0] = 2
> ```
>
> 但**range**返回的是一个无法直接打印的类型，若打印，会得到
>
> ```python
> >>>range(2 , 4)
> range(2 , 4)# 打印原字符格式
> ```
>
> 
>
> 
>
> range列表可通过list()函数显式转换为list
>
> ```python
> >>>list(range(1 , 3))
> [1 , 2]
> ```
>
> range可作为for语法中的迭代元素
>
> ```python
> for i in range(n):
> for _ in range(n):#当不需要使用迭代的元素时，可以直接用_代替
> ```
>

**七、**String字符串

'x' , "x"  与"""  x  """

>'x'中字符串中不能出现  '
>
>“x"中字符串中可出现  ’
>
>"""x"""中x的内容可以显示使用换行符多行输入，如
>
>```python
>>>> """
>asds
>asd"""
>```

对字符串进行元素选取，得到的仍是字符串，只是其只含一个字符

此外，字符串可用于查找连续序列

```python
s = 'asdcxz'
>>>s[2]
d
>>>'asd' in s
True
```

**八、**字典

表示方法

```python
{'Dem':key}如
numerals = {'I': 1, 'V': 5, 'H': 7}
```

字典可用于查找元素对应键值，但不可反向查找

```python
>>>numerals['I']
1
>>>numerals[1]
error
```

values方法：返回键值序列

```python
>>>numerals.values()
dict_values([1, 5, 10])
```

字典也可通过推导构建

```python
{<key exp>: <value exp> for <name> in <iter exp> if <filter exp>}
```



字典的键和键值均可以为很多东西（比如列表之类的玩意），但不可以重复使用同一个建

此外，列表与字典不可作为建，但可作为键值

**四、**可变序列与不可变序列

```math
\begin{align}
\left\{
\begin{aligned}
&可变序列:序列中元素可以不通过方法直接修改某个值，包括list,dictionary...\\
&不可变序列：序列中元素不可以直接修改某个元素值
\end{aligned}
\right.
\end{align}
```

> eg.
>
> ```python
> >>>s = ([1 , 2] , 3)
> >>>s[0] = 4 #不可直接修改某个元素的值
> ERROR
> >>>s[0][0] = 3 #但当序列中含有可变序列时，可以修改不可变序列中可变序列中的元素的值
> ```
>

### iterator

创建：使用iter函数

```python
>>>s = [3 , 4 , 5]
>>>iterator = iter(s)
>>>next(t) #返回t指代的当前元素，并将t指向下一个元素
3
>>>next(t)
4
>>>list(t) #从迭代器当前元素开始，遍历后续元素，形成列表
```

字典迭代器:(注：在python3.6以后字典才是一个有序表)

```python
iter(dictionary)/iter(dictionary.keys()) #迭代键
iter(dictionary.values()) #迭代值
```

当字典的结构改变（如增添或删减元素）时，原先的iterator会失效

迭代器可用于循环

```python
for i in iterator:
    print(i)
#迭代器可用于for，但该行为会使迭代器向前迭代，而当使用可迭代作为范围则不会
```

函数：

![image-20250722201132254](E:\笔记\python\image-20250722201132254.png)

对于惰性函数，其返回一定规则，不直接返回对象，只有在实际使用时才会进行迭代等操作

```python
f = lambda x : True if x > 0 else False
t
```

###Generators

Generators are created by generator functions.

Differ from formal functions,it uses ==yield== to return values.

```python
def plus_minus(x): # This function creates a generator
    yield x
    yield -x
>>>t = plus_minus(3)
>>>next(t)
3
>>>next(t)
-3
```

The generator function is a ==lazy function== ,so only when the generator is used , the next value will  be computed.

We can use ==yield from== to build a generator using all the values in generators or iterators.

```python
def a_then_b(a , b):
    yield from a
    yield from b
'''
this equals to
def a_then_b(a , b):
	for i in a:
		yield i
	for i in b:
		yield i
'''
# also,you can use this to build a recursion
def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
```

