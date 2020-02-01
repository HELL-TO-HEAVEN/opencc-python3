# 开放中文转换 (OpenCC) 2

## 基本概念

见《[繁简中文转换概说](https://zhuanlan.zhihu.com/p/104314323)》。

## 用法

### 在代码中使用

从大陆简体转换为台湾繁体（台湾正体）：

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='cn', to_region='tw')
>>> cc.convert('头发，发展，内存')
'頭髮，發展，記憶體'
```

从台湾繁体（台湾正体）转换为大陆简体：

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='tw', to_region='cn')
>>> cc.convert('乾坤，乾燥，計程車')
'乾坤，干燥，出租车'
```

`opencc2.Converter` 接受以下参数：

* `from_region`: 原文本的类型（详见下方列表）。默认为大陆简体
* `to_region`: 目标文本的区域（详见下方列表）。默认为台湾繁体（台湾正体）
* `phrases`: 是否启用词汇转换（如将「<span lang="zh-CN">内存</span>」转换为「<span lang="zh-TW">記憶體</span>」）。默认为「是」
* `fast`: 是否启用快速转换（但准确率降低）。默认为「否」

### 在命令行中使用

从大陆简体转换为台湾繁体：

```sh
$ echo 头发，发展，内存 | opencc2 -f cn -t tw
頭髮，發展，記憶體
```

从台湾繁体转换为大陆简体：

```sh
$ echo 乾坤，乾燥，計程車 | opencc2 -f tw -t cn
乾坤，干燥，出租车
```

详见 `opencc2 -h`。

## 支持的区域

支持的区域/标准如下：

* OpenCC 2 繁体 (t)
* 大陆简体 (cn)
* 大陆繁体 (cnt)
* 新加坡简体 (sg)
* 马来西亚简体 (my)
* 香港繁体 (hk)
* 台湾繁体（台湾正体） (tw)

目前不支持大陆繁体、马来西亚简体；新加坡简体、香港繁体不支持词汇转换。
