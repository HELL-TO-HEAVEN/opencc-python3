# 開放中文轉換 (OpenCC) 2

[简体中文（中国大陆）](https://github.com/sgalal/opencc2/blob/master/README-zh_CN.md) - [繁體中文（臺灣）](https://github.com/sgalal/opencc2/blob/master/README-zh_TW.md) - [English (United States)](https://github.com/sgalal/opencc2/blob/master/README-en_US.md)

## 基本概念

見《[繁簡中文轉換概說](https://zhuanlan.zhihu.com/p/104314323)》（原文爲大陸簡體）。

## 用法

### 在代碼中使用

從大陸簡體轉換爲臺灣繁體（臺灣正體）：

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='cn', to_region='tw')
>>> cc.convert('头发，发展，内存')
'頭髮，發展，記憶體'
```

從臺灣繁體（臺灣正體）轉換爲大陸簡體：

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='tw', to_region='cn')
>>> cc.convert('乾坤，乾燥，計程車')
'乾坤，干燥，出租车'
```

`opencc2.Converter` 接受以下參數：

* `from_region`: 原文本的類型（詳見下方列表）。默認爲大陸簡體
* `to_region`: 目標文本的類型（詳見下方列表）。默認爲臺灣繁體（臺灣正體）
* `phrases`: 是否啓用詞彙轉換（如將「<span lang="zh-CN">内存</span>」轉換爲「<span lang="zh-TW">記憶體</span>」）。默認爲「是」
* `fast`: 是否啓用快速轉換（但準確率降低）。默認爲「否」

### 在命令行中使用

從大陸簡體轉換爲臺灣繁體：

```sh
$ echo 头发，发展，内存 | opencc2 -f cn -t tw
頭髮，發展，記憶體
```

從臺灣繁體轉換爲大陸簡體：

```sh
$ echo 乾坤，乾燥，計程車 | opencc2 -f tw -t cn
乾坤，干燥，出租车
```

詳見 `opencc2 -h`。

## 支持的區域

支持的區域/標準如下：

* OpenCC 2 繁體 (t)
* 大陸簡體 (cn)
* 大陸繁體 (cnt)
* 新加坡簡體 (sg)
* 馬來西亞簡體 (my)
* 香港繁體 (hk)
* 臺灣繁體（臺灣正體） (tw)

目前不支持大陸繁體、馬來西亞簡體；新加坡簡體、香港繁體不支持詞彙轉換。
