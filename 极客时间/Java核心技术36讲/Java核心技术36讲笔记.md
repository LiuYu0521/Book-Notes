# 第1讲|谈谈你对Java平台的理解？
## 典型回答
1. 书写一次，到处运行
2. 垃圾收集

JRE（Java Runtime Environment）：Java运行环境，包含了JVM和Java类库，以及一些模块等
JDK（Java Development Kit）：可看作是JRE的一个超集，提供了更多工具，比如编译器、各种诊断工具等

源代码->通过Javac编译成为字节码(bytecode)，即.class文件->JVM内嵌的解释器将字节码转换成为最终的机器码
[解释执行和编译执行介绍](https://www.cnblogs.com/Downtime/p/7928579.html)

## 考点分析
对于这类笼统的问题，需要尽量表现出自己的思维深入并系统化，Java知识理解得也比较全面

## 知识扩展
Java平台蓝图
![Java平台蓝图](https://github.com/LiuYu0521/Book-Notes/raw/master/极客时间/Java核心技术36讲/Java平台蓝图.png)

# 第2讲|Exception和Error有什么区别？
## 考点分析
1. 理解Throwable、Exception、Error的设计和分类
![异常类图](https://github.com/LiuYu0521/Book-Notes/raw/master/极客时间/Java核心技术36讲/异常类图.png)

其中有些子类型，最好重点理解下，比如NoClassDefFoundError和ClassNotFoundException有什么区别
2. 理解Java语言中操作Throwable的元素和实践
