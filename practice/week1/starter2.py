# -*- coding: utf-8 -*-
"""
第一周练习（下）：Python 进阶四件套
生成器 → 迭代器 → 上下文管理器 → 异常处理 → 类型标注
按 TODO 顺序完成，每完成一个就运行验证。
"""
import time
from contextlib import contextmanager
from typing import Iterator, Optional


# ============ 练习 1：生成器 ============
# 目标：用 yield 写 fib(n)，生成前 n 个斐波那契数。
# 提示：函数体里有 yield 就是生成器函数
#       验证：list(fib(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def fib(n: int) -> Iterator[int]:
    # TODO
    pass


# ============ 练习 2：迭代器协议 ============
# 目标：写 Countdown 类，从 n 倒数到 0。实现 __iter__ 和 __next__。
# 提示：__iter__ 返回 self；__next__ 数到底后 raise StopIteration
#       验证：list(Countdown(3)) == [3, 2, 1, 0]
class Countdown:
    # TODO: __init__、__iter__、__next__
    pass


# ============ 练习 3：上下文管理器（类方式）============
# 目标：Timer 类，进入 with 时记开始时间，退出时打印耗时。
# 提示：__enter__ 进入时调用；__exit__ 退出时调用（异常退出也会走到）
class Timer:
    # TODO
    pass


# ============ 练习 4：上下文管理器（contextlib 方式）============
# 目标：用 @contextmanager 把下面的函数变成上下文管理器，效果同练习 3。
# 提示：yield 之前 = __enter__；yield 之后 = __exit__
@contextmanager
def timer():
    # TODO
    pass


# ============ 练习 5：异常处理 ============
# 目标：safe_divide(a, b)：b 为 0 时返回 None（打印一句警告），
#       其他异常不管，向上抛。
#       验证：safe_divide(4, 0) is None；safe_divide(4, 2) == 2.0
def safe_divide(a: int, b: int) -> Optional[float]:
    # TODO
    pass


# ============ 加分题 ============
# 1. 写一个生成器 read_lines(path)，逐行 yield 大文件（体会惰性求值省内存）
# 2. 思考：try/except/else/finally 四种块各自在什么时机执行？
# 3. 思考：为什么生成器处理大文件比 readlines() 省内存？


if __name__ == "__main__":
    # TODO: 完成练习后取消注释验证
    # print(list(fib(10)))
    # print(list(Countdown(3)))
    # with Timer():
    #     time.sleep(0.5)
    # with timer():
    #     time.sleep(0.5)
    # print(safe_divide(4, 0), safe_divide(4, 2))
    pass
