# Open Chinese Convert (OpenCC) 2

## Basic Concepts

See [An Overview of Traditional Chinese and Simplified Chinese Conversion](https://zhuanlan.zhihu.com/p/104314323) (in **Simplified Chinese (Mainland China)**).

## Usage

### In Python Code

From **Simplified Chinese (Mainland China)** to **Traditional Chinese (Taiwan)**:

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='cn', to_region='tw')
>>> cc.convert('头发，发展，内存')
'頭髮，發展，記憶體'
```

From **Traditional Chinese (Taiwan)** to **Simplified Chinese (Mainland China)**:

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='tw', to_region='cn')
>>> cc.convert('乾坤，乾燥，計程車')
'乾坤，干燥，出租车'
```

`opencc2.Converter` accepts the following arguments：

* `from_region`: Type of variant of the original text. Default to **Simplified Chinese (Mainland China)**
* `to_region`: Type of variant of the target text. Default to **Traditional Chinese (Taiwan)**
* `phrases`: Whether to enable phrase conversion (e.g. convert <span lang="zh-CN">内存</span> to <span lang="zh-TW">記憶體</span>). Default to `True`
* `fast`: Whether to enable fast conversion (with lower accuracy). Default to `False`

### In Command Line

From **Simplified Chinese (Mainland China)** to **Traditional Chinese (Taiwan)**:

```sh
$ echo 头发，发展，内存 | opencc2 -f cn -t tw
頭髮，發展，記憶體
```

From **Traditional Chinese (Taiwan)** to **Simplified Chinese (Mainland China)**:

```sh
$ echo 乾坤，乾燥，計程車 | opencc2 -f tw -t cn
乾坤，干燥，出租车
```

See `opencc2 -h` for details.

## Supported Types of Variant

Supported types of variant are as follows:

* **Traditional Chinese (OpenCC 2)** (t)
* **Simplified Chinese (Mainland China)** (cn)
* **Traditional Chinese (Mainland China)** (cnt)
* **Simplified Chinese (Singapore)** (sg)
* **Simplified Chinese (Malaysia)** (my)
* **Traditional Chinese (Hong Kong)** (hk)
* **Traditional Chinese (Taiwan)** (tw)

Currently **Traditional Chinese (Mainland China)** and **Simplified Chinese (Malaysia)** is not supported. Phrase conversion is not supported for **Simplified Chinese (Singapore)** and **Traditional Chinese (Hong Kong)**.
