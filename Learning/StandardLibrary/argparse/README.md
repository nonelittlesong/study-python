
## 示例
```py
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

## add_argument()

### type


## [退出方法](https://docs.python.org/zh-cn/3.8/library/argparse.html#exiting-methods)
- ArgumentParser.exit(status=0, message=None)  
- ArgumentParser.error(message)  
