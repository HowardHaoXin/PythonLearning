# PythonLearning

> 一个用于记录 **Python 学习过程**的项目：`src/` 存放学习代码，`docs/` 存放对应的学习注解，两者一一对应，便于随时回顾查阅。

## 项目简介

本项目用于系统性地学习和复习 Python 基础语法，从零开始逐步推进。每个学习主题由两部分组成：

- **代码文件（`src/`）**：可运行的 Python 练习代码，含详细注释。
- **注解文档（`docs/`）**：对应该主题的知识点提炼、语法总结与易错点说明。

## 目录结构

```
PythonLearning/
├── src/           # 学习代码（BX_YYY.py）
├── docs/          # 学习注解与练习注解（BX_YYY.md / TX_YYY.md，中文命名）
├── practice/      # 练习代码（TX_YYY.py）
├── README.md      # 项目说明
└── CHANGELOG.md   # 变更日志
```

## 文件命名规范

| 类型 | 规则 | 说明 |
| --- | --- | --- |
| 学习代码 | `BX_YYY.py` | `X` 为时间顺序编号，`YYY` 为学习内容（使用英文） |
| 学习注解 | `BX_YYY.md` | `X` 与对应 py 一致，`YYY` 统一用中文，便于一眼定位 |
| 练习代码 | `TX_YYY.py` | `T` 表示练习题，`X` 为时间顺序编号，`YYY` 为练习内容（使用英文） |
| 练习注解 | `TX_YYY.md` | 与对应练习代码一致，`YYY` 统一用中文 |
| 专题注解 | `TX-X_YYY.md` | `X-X` 表示题目序号范围（如 `T1-3`），`YYY` 为专题名称（统一用中文） |

## 学习内容索引

| 编号 | 学习主题 | 代码文件 | 注解文档 |
| --- | --- | --- | --- |
| B1 | 注释 | [B1_Annotation.py](src/B1_Annotation.py) | [B1_注释.md](docs/B1_注释.md) |
| B2 | 输出函数 print | [B2_FunPrint.py](src/B2_FunPrint.py) | [B2_输出函数.md](docs/B2_输出函数.md) |
| B3 | 变量 | [B3_variable.py](src/B3_variable.py) | [B3_变量.md](docs/B3_变量.md) |
| B4 | 输入函数 input | [B4_FunInput.py](src/B4_FunInput.py) | [B4_输入函数.md](docs/B4_输入函数.md) |
| B5 | 运算符 | [B5_Operator.py](src/B5_Operator.py) | [B5_运算符.md](docs/B5_运算符.md) |
| B6 | 字符串 | [B6_String.py](src/B6_String.py) | [B6_字符串.md](docs/B6_字符串.md) |
| B7 | 列表 | [B7_List.py](src/B7_List.py) | [B7_列表.md](docs/B7_列表.md) |
| B8 | 元组 | [B8_Tuple.py](src/B8_Tuple.py) | [B8_元组.md](docs/B8_元组.md) |
| B9 | 字典 | [B9_Dictionary.py](src/B9_Dictionary.py) | [B9_字典.md](docs/B9_字典.md) |
| B10 | 集合 | [B10_Set.py](src/B10_Set.py) | [B10_集合.md](docs/B10_集合.md) |
| B11 | 数据类型总结 | [B11_DataType.py](src/B11_DataType.py) | [B11_数据类型.md](docs/B11_数据类型.md) |
| B12 | 条件与循环 | [B12_ConditionalAndLoop.py](src/B12_ConditionalAndLoop.py) | [B12_条件与循环.md](docs/B12_条件与循环.md) |
| B13 | 函数 | [B13_def.py](src/B13_def.py) | [B13_函数.md](docs/B13_函数.md) |
| B14 | 异常处理 | [B14_ExceptingHandling.py](src/B14_ExceptingHandling.py) | [B14_异常处理.md](docs/B14_异常处理.md) |
| B15 | 模块与包 | [B15_ModulePackets.py](src/B15_ModulePackets.py) | [B15_模块与包.md](docs/B15_模块与包.md) |

## 练习内容索引

| 编号 | 练习主题 | 代码文件 | 注解文档 |
| --- | --- | --- | --- |
| T0 | 学员管理系统 | [T0_SystemManage.py](practice/T0_SystemManage.py) | [T0_学员管理系统.md](docs/T0_学员管理系统.md) |
| T1 | 两数之和 | [T1_LeetCode1.py](practice/T1_LeetCode1.py) | [T1_两数之和.md](docs/T1_两数之和.md) |
| T2 | 字母异位词分组 | [T2_LeetCode2.py](practice/T2_LeetCode2.py) | [T2_字母异位词分组.md](docs/T2_字母异位词分组.md) |
| T3 | 最长连续序列 | [T3_LeetCode3.py](practice/T3_LeetCode3.py) | [T3_最长连续序列.md](docs/T3_最长连续序列.md) |
| T4 | 移动零 | [T4_LeetCode4.py](practice/T4_LeetCode4.py) | [T4_移动零.md](docs/T4_移动零.md) |
| T5 | 盛最多水的容器 | [T5_LeetCode5.py](practice/T5_LeetCode5.py) | [T5_盛最多水的容器.md](docs/T5_盛最多水的容器.md) |

## 专题索引

| 专题 | 覆盖题目 | 注解文档 |
| --- | --- | --- |
| 哈希表专题 | T1 ~ T3 | [T1-3_哈希表专题.md](docs/T1-3_哈希表专题.md) |

## 使用方式

- **学代码**：直接打开 `src/` 下对应 `.py` 文件运行查看结果。
- **看注解**：打开 `docs/` 下同名中文 `.md` 文档，快速回顾知识点与易错点。
