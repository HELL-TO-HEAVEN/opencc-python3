<div lang="zh-CN">

# opencc-python3

## 基本概念

见《[繁简中文转换概说](https://zhuanlan.zhihu.com/p/104314323)》。

```sh
$ pip install opencc-python3
```

## 用法

### 在代码中使用

从大陆简体转换为台湾繁体（台湾正体）（带词汇转换）：

```python
>>> import opencc
>>> cc = opencc.Converter(from_variant='cn', to_variant='twp')
>>> cc.convert('头发，发展，内存')
'頭髮，發展，記憶體'
```

从台湾繁体（台湾正体）转换为大陆简体（带词汇转换）：

```python
>>> import opencc
>>> cc = opencc.Converter(from_variant='twp', to_variant='cn')
>>> cc.convert('乾坤，乾燥，計程車')
'乾坤，干燥，出租车'
```

`opencc.Converter` 接受以下参数：

* `from_variant`: 原文本的变体类型（详见下方列表）。默认为大陆简体
* `to_variant`: 目标文本的变体类型（详见下方列表）。默认为台湾繁体（台湾正体）
* `with_phrases`: 是否启用词汇转换（如将「<span lang="zh-CN">内存</span>」转换为「<span lang="zh-TW">記憶體</span>」）。默认为「是」

### 在命令行中使用

从大陆简体转换为台湾繁体（台湾正体）（带词汇转换）：

```sh
$ echo 头发，发展，内存 | opencc-python3 -f cn -t twp
頭髮，發展，記憶體
```

从台湾繁体（台湾正体）转换为大陆简体（带词汇转换）：

```sh
$ echo 乾坤，乾燥，計程車 | opencc-python3 -f twp -t cn
乾坤，干燥，出租车
```

详见 `opencc-python3 -h`。

## 支持的变体类型

支持的变体类型如下：

* OpenCC 2 繁体 (t)
* 大陆简体、新加坡简体 (cn, sg)
* 香港繁体 (hk)
* 台湾繁体（台湾正体） (tw)
* 台湾繁体（台湾正体）（带词汇转换） (twp)

## 开源协议

* 代码：MIT
* 词库：Apache-2.0

</div>
