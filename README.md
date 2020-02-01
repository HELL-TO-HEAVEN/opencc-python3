# OpenCC 2

開放中文轉換

## 用法

### API 用法

從大陸簡體轉換爲臺灣繁體：

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='cn', to_region='tw')
>>> cc.convert('头发，发展')
'頭髮，發展'
```

從臺灣繁體轉換爲大陸簡體：

```python
>>> import opencc2
>>> cc = opencc2.Converter(from_region='tw', to_region='cn')
>>> cc.convert('乾坤，乾燥')
'乾坤，干燥'
```

### 命令行用法

從大陸簡體轉換爲臺灣繁體：

```sh
$ echo 头发，发展 | python opencc2.py -f cn -t tw
頭髮，發展
```

從臺灣繁體轉換爲大陸簡體：

```sh
$ echo 乾坤，乾燥 | python opencc2.py -f tw -t cn
乾坤，干燥
```

## Q&A

如何序列化詞典？

OpenCC 2 不提供序列化功能，請自行使用 pickle。

