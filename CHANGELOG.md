# 变更日志（CHANGELOG）

> 记录本项目的更新历史与改动说明，按时间倒序排列。

## [2026-09-01][v1.4]

### 新增

- 新增练习注解：
  - 练习 T3：最长连续序列（[docs/T3_最长连续序列.md](docs/T3_最长连续序列.md)）。
  - 练习 T4：移动零（[docs/T4_移动零.md](docs/T4_移动零.md)）。
  - 练习 T5：盛最多水的容器（[docs/T5_盛最多水的容器.md](docs/T5_盛最多水的容器.md)）。
- 新增专题注解 [docs/T1-3_哈希表专题.md](docs/T1-3_哈希表专题.md)：整合 T1~T3 的哈希表最优解，提炼哈希表的使用场景。
- 更新 [README.md](README.md)：练习内容索引补充 T3/T4/T5，新增「专题索引」小节，并在文件命名规范中新增「专题注解 `TX-X_YYY.md`」格式。

## [2026-08-31][v1.3]

### 新增

- 新增学习文件 [src/B15_ModulePackets.py](src/B15_ModulePackets.py)：模块与包（模块分类、三种导入方式、`if __name__ == "__main__"`、包的创建与导入、`__all__` 的使用），并生成注解文档 [docs/B15_模块与包.md](docs/B15_模块与包.md)，同时在 [README.md](README.md) 学习内容索引中将 B15 主题更新为「模块与包」。
- 在 [README.md](README.md) 中新增「练习内容索引」小节，登记练习代码与对应注解：
  - 练习 T0：学员管理系统（[practice/T0_SystemManage.py](practice/T0_SystemManage.py) / [docs/T0_学员管理系统.md](docs/T0_学员管理系统.md)）。
  - 练习 T1：两数之和（[practice/T1_LeetCode1.py](practice/T1_LeetCode1.py) / [docs/T1_两数之和.md](docs/T1_两数之和.md)）。
  - 练习 T2：字母异位词分组（[practice/T2_LeetCode2.py](practice/T2_LeetCode2.py) / [docs/T2_字母异位词分组.md](docs/T2_字母异位词分组.md)）。
- 在 [docs/B6_字符串.md](docs/B6_字符串.md) 中补充 `join` 的用法（`分隔符.join(可迭代对象)`，`split` 的逆操作）。

## [2026-08-28][v1.2]

### 新增

- 新增学习文件 [src/B15_ExceptingHandling.py](src/B15_ExceptingHandling.py)：异常处理（异常基础、常见异常类型、`try-except` 捕获、`else`/`finally`、异常处理核心原则）。
- 生成对应注解文档 [docs/B15_异常处理.md](docs/B15_异常处理.md)。
- 更新 [README.md](README.md) 学习内容索引，加入 B15 条目。

## [2026-08-27][v1.1]

### 新增

- 在 [src/B5_Operator.py](src/B5_Operator.py) 中添加「赋值运算的使用与理解」部分：
  - 演示整数（不可变类型）赋值后重新赋值不影响原有变量。
  - 演示列表（可变类型）赋值后原地修改会同步反映到指向同一对象的变量。
  - 补充注释，说明二者结果不同的原因是「可变 vs 不可变」的区别。

## [2026-08-25][v1.0]

### 新增

- 创建说明文档目录 `docs/`。
- 为 `src/` 下的 14 个学习文件生成对应的中文注解文档：
  `B1_注释.md` ～ `B14_学员管理系统.md`。
- 添加项目说明文档 [README.md](README.md)，含目录结构、命名规范与学习内容索引。
- 添加本变更日志文档 `CHANGELOG.md`。

### 说明

- 确立文件命名规范：代码 `BX_YYY.py`（`YYY` 可中文则中文），注解 `BX_YYY.md`（`YYY` 统一中文）。
- 将注解文档由英文命名统一改为中文命名，便于快速定位阅读内容。
