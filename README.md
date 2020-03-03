# opencc-python3

**This repository is NOT ready for production!**

[<span lang="zh-CN">简体中文（中国大陆）</span>](https://github.com/sgalal/opencc-python3/blob/master/README-zh_CN.md) - [<span lang="zh-TW">繁體中文（臺灣）</span>](https://github.com/sgalal/opencc-python3/blob/master/README-zh_TW.md) - [<span lang="en-US">English (United States)</span>](https://github.com/sgalal/opencc-python3/blob/master/README-en_US.md)

```sh
$ pip install opencc-python3
```

## 基本概念

見《[繁簡中文轉換概說](https://zhuanlan.zhihu.com/p/104314323)》（原文爲大陸簡體）。

## 用法

### 在代碼中使用

從大陸簡體轉換爲臺灣繁體（臺灣正體）：

```python
>>> import OpenCC
>>> cc = OpenCC.Converter(from_variant='cn', to_variant='tw')
>>> cc.convert('头发，发展，内存')
'頭髮，發展，記憶體'
```

從臺灣繁體（臺灣正體）轉換爲大陸簡體：

```python
>>> import OpenCC
>>> cc = OpenCC.Converter(from_variant='tw', to_variant='cn')
>>> cc.convert('乾坤，乾燥，計程車')
'乾坤，干燥，出租车'
```

`OpenCC.Converter` 接受以下參數：

* `from_variant`: 原文本的變體類型（詳見下方列表）。默認爲大陸簡體
* `to_variant`: 目標文本的變體類型（詳見下方列表）。默認爲臺灣繁體（臺灣正體）
* `with_phrases`: 是否啓用詞彙轉換（如將「<span lang="zh-CN">内存</span>」轉換爲「<span lang="zh-TW">記憶體</span>」）。默認爲「是」

### 在命令行中使用

從大陸簡體轉換爲臺灣繁體（臺灣正體）：

```sh
$ echo 头发，发展，内存 | opencc-python3 -f cn -t tw
頭髮，發展，記憶體
```

從臺灣繁體（臺灣正體）轉換爲大陸簡體：

```sh
$ echo 乾坤，乾燥，計程車 | opencc-python3 -f tw -t cn
乾坤，干燥，出租车
```

詳見 `opencc-python3 -h`。

## 支持的變體類型

支持的變體類型如下：

* OpenCC 2 繁體 (t)
* 大陸簡體 (cn)
* 大陸繁體 (cnt)
* 新加坡簡體 (sg)
* 馬來西亞簡體 (my)
* 香港繁體 (hk)
* 臺灣繁體（臺灣正體） (tw)

目前不支持大陸繁體、馬來西亞簡體；新加坡簡體、香港繁體不支持詞彙轉換。

## 開源協議

* 代碼：MIT
* 詞庫：Apache-2.0
