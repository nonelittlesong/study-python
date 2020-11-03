# [正则表达式](https://docs.python.org/zh-cn/3/library/re.html?highlight=re#module-re)

| 特殊字符 | 含义 |
| --- | --- |
| . | 默认匹配除了换行的任意字符。如果指定了 `DOTALL`，则匹配任意字符。 |
| ^ | 匹配字符串开头。`MULTILINE` 模式也匹配换行后的首个字符。 |
| $ | 匹配字符串尾部。 |
| * | 对它前面的正则式匹配0到任意次重复 |

## [re.split(pattern, string, maxsplit=0, flags=0)](https://docs.python.org/zh-cn/3/library/re.html?highlight=re#re.split)
用 pattern 分开 string。  
如果 pattern 中有括号，那么所有的组里的文字也会包含在列表里。  
```
>>> re.split(r'\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
```
