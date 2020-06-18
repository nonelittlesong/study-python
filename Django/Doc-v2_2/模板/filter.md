参考：  
- [Django template模板中过滤器使用介绍](https://blog.csdn.net/weixin_43465312/article/details/98316077)  

1. 可以通过过滤器来修改变量的显示，形式是： {{ variable|filter }}。  
1. 过滤器可以采用链式的方式： {{ text|escape|linebreaks ||。  
1. 过滤器可以带参数： {{ bio|truncatewords:30 }}。  
1. 过滤器参数如果有空格，要用引号括起来： {{ list|join:", " }}
