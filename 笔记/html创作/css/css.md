# 属性

## rel

用于

| 标签     | 是否支持 `rel` | 说明                                                         |
| -------- | -------------- | ------------------------------------------------------------ |
| `<link>` | ✅ 标准用法     | 引入样式表、图标、预加载等。                                 |
| `<a>`    | ✅ 标准用法     | 描述“当前页面”与“目标链接”之间的关系，如 `rel="nofollow"`、`rel="external"`。 |
| `<area>` | ✅ 标准用法     | 与 `<a>` 类似，用于图像映射里的可点击区域。                  |
| `<form>` | ✅ HTML 标准    | `rel` 描述目标地址与表单之间的关系（极少用）。               |

是 **relationship** 的缩写，用来告诉浏览器「当前引用的这个外部资源与 HTML 文档之间是什么关系」。

常用值：

| 取值                     | 作用说明                                       |
| ------------------------ | ---------------------------------------------- |
| `stylesheet`             | 引入 CSS 样式表（最常用）。                    |
| `icon` / `shortcut icon` | 指定网站小图标（favicon）。                    |
| `preload`                | 提前加载关键资源（字体、脚本等），提升性能。   |
| `prefetch`               | 空闲时预加载未来可能用到的资源。               |
| `canonical`              | SEO 用，告诉搜索引擎“这是规范的 URL”。         |
| `alternate`              | 指向同一内容的不同版本，如 RSS、不同语言页面。 |

## boder-bottom

border-bottom 是 CSS 的「简写属性」，**任何支持盒模型的元素都能用**（块级元素、行内块、表格单元格、Flex/Grid 子项等）。
一句话作用：给元素的==**下边框**==一次设定「粗细、样式、颜色」。

可用于多种盒子标签

```html
<div>, <p>, <h1>–<h6>, <ul>, <li>, <table>, <td>, <th>, <span>, <img>, <button>, <input>, <a> … 
```

### 作用

- 只影响下边框，其余三边不受影响。
- 可用于分隔线、导航条下划线、按钮悬停效果等。

### 可取值

| 分量                             | 合法取值                                                     | 初始值            |
| -------------------------------- | ------------------------------------------------------------ | ----------------- |
| **宽度** `<border-bottom-width>` | `thin`, `medium`, `thick`, 或任何长度：`1px`, `0.5em`, `2rem` … | `medium`          |
| **样式** `<border-bottom-style>` | `none`, `hidden`, `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset` | `none`            |
| **颜色** `<color>`               | 颜色名、十六进制、`rgb()`, `hsl()`, `currentColor`, `transparent` … | 元素的 `color` 值 |

直接将合法取值并列，并用空格隔开即可，当然，也可以输入表格里的内容指定，以下代码等价，不过第二行代码可以用于只改变单个分量，其它继承的情况

```css
border-bottom-style: dotted;
border-bottom: dotted
```

##font

### font-weight

#### 形式语法

```css
font-weight = 
  <font-weight-absolute>  |
  bolder                  |
  lighter                 

<font-weight-absolute> = 
  normal             |
  bold               |
  <number [1,1000]> <!number的值非整百数会进行四舍五入至整百> 
```

#### 作用：

指定字体粗细

#### 作用范围：

所有显示文本的元素（从 `<body>` 到 `<span>`、`<button>`、`<input>` 等）

#### 可取值

| 类别       | 具体取值                                                     | 说明                                              |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------- |
| **关键字** | `normal`（默认 400）<br>`bold`（700）<br>`lighter`<br>`bolder` | 相对当前继承值再变细 / 变粗                       |
| **数值**   | **100–900** 且必须是 100 的整数倍                            | 100 最细，900 最粗；常用 400（正常）、700（加粗） |
| **全局值** | `inherit` / `initial` / `unset` / `revert`                   | 与通用 CSS 关键字一致                             |

### font-size

#### 形式语法

```html
font-size = 
  <absolute-size>            |
  <relative-size>            |
  <length-percentage [0,∞]>  |
  math                       

<length-percentage> = 
  <length>      |
  <percentage>  
```

####可取值

- [`xx-small`、`x-small`、`small`、`medium`、`large`、`x-large`、`xx-large`、`xxx-large`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size#xx-small)

  基于用户默认字体大小（`medium`）的绝对大小关键字。

- [`larger`、`smaller`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/font-size#larger)

  相对大小关键字。字体大小将相对于父元素的字体大小变大或变小，大致按照上面用于区分绝对大小关键字的比率。

- [`<length>`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/length)

  一个正的 [`<length>`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/length) 值。对于大多数相对于字体的单位（例如 `em` 和 `ex`），字体大小相对于父元素的字体大小。对于基于根元素的字体相关单位（例如 `rem`），字体大小相对于 [`<html>`](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Reference/Elements/html)（根）元素使用的字体大小。

- [`<percentage>`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/percentage)

  一个正的 [`<percentage>`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/percentage) 值，相对于父元素的字体大小。

- `math` 实验性 使用特殊的[数学缩放规则](https://w3c.github.io/mathml-core/#the-math-script-level-property)来确定 `font-size` 属性的计算值。
