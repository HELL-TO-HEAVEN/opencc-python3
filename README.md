# OpenCC 2

開放中文轉換

## 用法

### API 用法

從大陸簡體轉換爲臺灣繁體：

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='cn', to_region='tw')
>>> cc.convert('头发，发展，内存')
'頭髮，發展，記憶體'
```

從臺灣繁體轉換爲大陸簡體：

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='tw', to_region='cn')
>>> cc.convert('乾坤，乾燥，計程車')
'乾坤，干燥，出租车'
```

### 命令行用法

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

## 支持的地區

OpenCC 2 標準 (t)，中國大陸 (cn)，中國大陸繁體 (cnt)，新加坡 (sg)，香港 (hk)，臺灣 (tw)

## Q&A

如何序列化詞典？

OpenCC 2 不提供序列化功能，請自行使用 pickle。

