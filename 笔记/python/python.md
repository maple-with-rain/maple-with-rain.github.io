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

### class

创建class函数

```python
class Yourclass: # class +函数名
    def __init__(self , yourargs):#yourargs为构造需要的参数（可为空）
        
        #__init__函数为默认方法，用于对象创建时的初始化，对象中的属性可在其中被定义
        
        self.arg1 = 0 # 通过这个，构造了Yourclass对象的一个内置参数arg1
        
        #self为定义类方法时的必须参数，指代引用方法的当前Yourclass对象，但在外部调用时并不给出，自动调用
        def yourmethod(self , yourargs):
            self.arg = 1
            #在方法中调用当前对象的参数时需要使用self调用
```

注：

> + python中的属性定义记为宽松，你可以在class定义时任意函数中给出，你甚至可以在类定义之外为class对象添加属性（不过class对象的属性==好像==是在属性被使用时才产生的🤔好神奇，而\__int\_\_函数直接帮我们产生了需要的属性）
>
>   如：现在有类Account，其内部定义对象onwer，现在我们可以在使用时在外部通过
>
>   ```python
>   Account a
>   a.value = 0
>   ```
>
>   为Account对象a引入新属性

特性

python中class类似于variable变量，可异直接修改属性，而简单的赋值则是对象地址的共用，而非复制对象，此外，也可用is ，==来判断为哪种类型的相等

```python
class Type:
    def __init__(self):
        self.value = 0
>>>Type a , c
>>>b = a
>>>a == c
True
>>> a is c
False
>>>a.value = 1
>>>b is a
True
>>>a.keep = 0 #为a引入keep属性
```

####class attributes

```math
\left\{
\begin{aligned}
&类属性：在类中，函数外创建或者在类定义外通过对类直接使用'.'引用创建或修改，与实例化无关\\
&实例属性：在类的函数中或外界指定实例对象通过'.'引用创建或修改
\end{aligned}
\right.
```



```python
class Myclass:
    value1 = 1 #类属性 class attribute
    def __init__(self):
        value2 = 2 #实例属性 instance attribute
```

类属性仅储存一次，储存于类定义的部分，可以通过修改类（而非类的实例）修改，此操作会同时导致所有该类的实例中的该属性同步改变

而当通过实例操作类属性时，实际是创造了一个新的同名实例属性，此时此操作只改变当前对象的属性

```python
Myclass.value1 = 3 # 所有该类的实例（无论此时创建与否），value1的值均改变
Myclass.value3 = 5 # 为Myclass创建类属性value3
Myclass a
a.value1 = 4 # 仅改变该实例value1的值
```

#### attribute lookup

```python
<expression>.<name>
```

优先评估\<expression\>，然后评估\<name\>

\<name\>的评估顺序：$实例属性\to类属性\to函数$，也就是说，如果该类对象的一个类属性创建了同名实例属性，此时类属性的无论如何修改，该对象引用的都是==同名实例对象==

此外，当为类属性时，会返回一个绑定到该实例对象的函数，可以不通过'.'直接引用

有两个评估\<name\>的特殊函数：
```python
>>>getattr(a , 'value') # 与a.value类似，只是不能作为表达式的左值
0
>>>hasattr(a , 'value')# 查找a内是否有value属性
True
```

此外，类的函数也算是一种类属性

对类中函数的调用也有分为类本身和实例对象

```python
Myclass a
a.function() # 默认self为a,无法改变self，返回值为一个self绑定到a的函数
Myclass.function(a) # 返回值为一个self未绑定的函数，因此参数列表中需要给出self(此处为a)
```

###Inheritance继承

```python
class <name>(<base class>):
    <suite>
```

example

```python
class Account:
    def __init__(self):
        self.instrest = 0.01
        self.deposit = 0
    def withdraw(self , num):
        assert self.deposit - num > 0
        self.deposit -= num
        return self.deposit
class CheckingAccount(Account):
    withdraw_fee = 1
    def withdraw(self , num):
    	return Account.withdraw(self , amount + self.withdraw_fee)
    #由于self为CheckingAccount类的实例，因此需要使用上述方法调用
```

可以更改子类的属性，但若未更改，则默认继承基类的属性，对于子类，首先查找子类内属性，若无，查找基类内属性

### String Representation

> ==eval==
>
> This is used to evaluate a String Representation
>
> ```python
> eval()
> ```
>
> 

In Python , every object produces two representations

```python
str: # str is legible to humans
repr :  # repr is legible to Python Interpreter
```

#### repr

```python
repr(object) -> string
```

Return the ==canonical== string representation of the object

For most object types , `eval(repr(object)) == object`

Some objects do not have a simple Python-readable string

```python
>>>repr(min)
'<built-in function min>' 
#<>represent that this is not exactly a python expression
```

####str

```python
>>>from fractions import Fraction
>>>half = Fraction(1,2)
>>>repr(half)
'Fraction(1,2)'
>>>str(half)
'1/2'  # This is when you use print while get
>>>print(half)
1/2
```

###F-Strings

#### String Interpolation

```python
>>>f'pi starts with {pi} ...'
# 与'pi' + ' starts ' + 'with ' +str(pi) +'...'等价
'pi starts with 3.141592653589793...'
>>>f'2 + 2 = {2 + 2}'
'2 + 2 = 4'
```

F-String使字符串中大括号内的==值==转换为`str`字符串插入到原字符串该位置，并返回插入后得到的`str`字符串

###Polymorphic Function 多态函数

例子

> ```python
> >>>half = Fraction(1 , 2)
> #此时，可以对half使用str和repr函数，但实际上，决定str与repr的具体作用的函数内置于Fraction类，可用下面方式调用
> >>>half.__str__()/half.__repr__()
> ```
>
> 也就是说，`str`和`repr`以如下方式定义
>
> ```python
> def repr(x):
>     return type(x).__repr__(x)
> #此处直接调用的是类属性，而非实例属性
> 
> ```

###Interfaces接口

​	核心是用一个独立于类的特殊函数，由于多个类的某些同名同类型属性，可以通过一定设计，使该函数直接作用于多种不同的类

如`repr`和`str`就是这么设计的，其操作具体细节内置于不同的类，其只进行引用和一些能够共通的操作

### Special Method Names

通用格式

```python
__Name__
```

例子

```python
__init__
__repr__
__add__
__radd__#(与 add 不同，这个是将.引用里的参数作为加法的左边那项（主要有的加法可能有序）)
#此外，这个似乎有利于自定义的类位于加号右侧时定义加法（毕竟内置的类的add咋改真不知道，况且在内置类内全部添加一遍好像不现实🤔）
#如 int + class就可以通过定义__radd__实现
__bool__
__float__
```

🤔这玩意是在说我们通常使用一些的内置函数都只是==接口==，具体内置内容与类有关🤔

🤔这个思路也挺神奇

🤔不过C++到底层可能也是这样❓只不过C++目前我确实还没学过给类定义这玩意的操作不过重载运算符也差不多了吧🤔

```python
class Rate:
    def __add__(self , other):
        if 
```

## Composition

### List Link

一个例子

```python
class Link:
    empty = ()
    def __init__(self , first , rest = empty):
        assert rest is Link.empty or isinstance(rest , Link)
        self.first = first
        self.rest = rest
```

### Tree



