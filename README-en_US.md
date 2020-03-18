<div lang="en-US">

# opencc-python3

## Basic Concepts

See [_An Overview of Traditional Chinese and Simplified Chinese Conversion_](https://zhuanlan.zhihu.com/p/104314323) (in **Simplified Chinese (Mainland China)**).

```sh
$ pip install opencc-python3
```

## Usage

### In Python Code

From **Simplified Chinese (Mainland China)** to **Traditional Chinese (Taiwan)** (with phrases):

```python
>>> import opencc
>>> cc = opencc.Converter(from_variant='cn', to_variant='twp')
>>> cc.convert('头发，发展，内存')
'頭髮，發展，記憶體'
```

From **Traditional Chinese (Taiwan)** to **Simplified Chinese (Mainland China)** (with phrases):

```python
>>> import opencc
>>> cc = opencc.Converter(from_variant='twp', to_variant='cn')
>>> cc.convert('乾坤，乾燥，計程車')
'乾坤，干燥，出租车'
```

`opencc.Converter` accepts the following arguments：

* `from_variant`: Type of variant of the original text. Default to **Simplified Chinese (Mainland China)**
* `to_variant`: Type of variant of the target text. Default to **Traditional Chinese (Taiwan)**
* `with_phrases`: Whether to enable phrase conversion (e.g. convert <span lang="zh-CN">内存</span> to <span lang="zh-TW">記憶體</span>). Default to `True`

### In Command Line

From **Simplified Chinese (Mainland China)** to **Traditional Chinese (Taiwan)** (with phrases):

```sh
$ echo 头发，发展，内存 | opencc-python3 -f cn -t twp
頭髮，發展，記憶體
```

From **Traditional Chinese (Taiwan)** to **Simplified Chinese (Mainland China)** (with phrases):

```sh
$ echo 乾坤，乾燥，計程車 | opencc-python3 -f twp -t cn
乾坤，干燥，出租车
```

See `opencc-python3 -h` for details.

## Supported Types of Variant

Supported types of variant are as follows:

* **Traditional Chinese (OpenCC 2)** (t)
* **Simplified Chinese (Mainland China), Simplified Chinese (Singapore)** (cn, sg)
* **Traditional Chinese (Hong Kong)** (hk)
* **Traditional Chinese (Taiwan)** (tw)
* **Traditional Chinese (Taiwan)** (with phrases) (twp)

## License

* Code: MIT
* Dictionary: Apache-2.0

</div>
