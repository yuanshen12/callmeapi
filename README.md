# 酒小二API接口自动化测试框架

使用工具：python + requests | excel

选择框架：case基于excel;通过脚本读写excel表里面的case，判断出参和入参是否预期结果的接口自动化测试框架。

优势：\
1、case写在excel里面易于维护\
2、测试结果通过返回的参数写入excel\
3、测试报告可以集成在jenkins，易于分析问题

## 框架
- Base 层管理常用方法
- excel 层存放case数据
- openjson 层存放json格式的返回数据（用于依赖数据，比如token）

## case
> [case测试用例和结果]()