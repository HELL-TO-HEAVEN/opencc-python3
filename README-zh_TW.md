<div lang="zh-TW">

# opencc-python3

## 基本概念

見《[繁簡中文轉換概說](https://zhuanlan.zhihu.com/p/104314323)》（原文為大陸簡體）。

```sh
$ pip install opencc-python3
```

## 用法

### 在程式碼中使用

從大陸簡體轉換為臺灣繁體（臺灣正體）：

```python
>>> import OpenCC
>>> cc = OpenCC.Converter(from_variant='cn', to_variant='tw')
>>> cc.convert('头发，发展，内存')
'頭髮，發展，記憶體'
```

從臺灣繁體（臺灣正體）轉換為大陸簡體：

```python
>>> import OpenCC
>>> cc = OpenCC.Converter(from_variant='tw', to_variant='cn')
>>> cc.convert('乾坤，乾燥，計程車')
'乾坤，干燥，出租车'
```

`OpenCC.Converter` 接受以下引數：

* `from_variant`: 原文字的變體類型（詳見下方列表）。預設為大陸簡體
* `to_variant`: 目標文字的變體類型（詳見下方列表）。預設為臺灣繁體（臺灣正體）
* `with_phrases`: 是否啟用詞彙轉換（如將「<span lang="zh-CN">内存</span>」轉換為「<span lang="zh-TW">記憶體</span>」）。預設為「是」

### 在命令列中使用

從大陸簡體轉換為臺灣繁體（臺灣正體）：

```sh
$ echo 头发，发展，内存 | opencc-python3 -f cn -t tw
頭髮，發展，記憶體
```

從臺灣繁體（臺灣正體）轉換為大陸簡體：

```sh
$ echo 乾坤，乾燥，計程車 | opencc-python3 -f tw -t cn
乾坤，干燥，出租车
```

詳見 `opencc-python3 -h`。

## 支援的變體類型

支援的變體類型如下：

* OpenCC 2 繁體 (t)
* 大陸簡體 (cn)
* 大陸繁體 (cnt)
* 新加坡簡體 (sg)
* 馬來西亞簡體 (my)
* 香港繁體 (hk)
* 臺灣繁體（臺灣正體） (tw)

目前不支援大陸繁體、馬來西亞簡體；新加坡簡體、香港繁體不支援詞彙轉換。

## 開源協議

* 程式碼：MIT
* 詞庫：Apache-2.0

</div>
