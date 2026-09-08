# -*- coding: utf-8 -*-
"""
第一周练习：装饰器
任务：按顺序完成三个练习，每完成一个就运行验证效果。
提示：先完成 log_time，再写 retry，最后叠加使用。
"""
import random
import time
import functools


# ============ 练习 1：计时装饰器（无参装饰器）============
# 目标：写一个 @log_time 装饰器，函数执行前后各取一次时间，
#       打印「函数名 执行耗时: X.XX 秒」，并返回原函数的返回值。
def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed_time = time.perf_counter() - start_time
            print(f"{func.__name__} 执行耗时: {elapsed_time:.2f} 秒")
   
    return wrapper


# ============ 练习 2：重试装饰器（带参装饰器，三层结构）============
# 目标：@retry(times=3, delay=1) —— 被装饰函数抛出异常时自动重试，
#       times 次后仍失败则抛出最后一次的异常。
#       每次重试前打印「重试第 n 次...」，并 sleep(delay) 秒。
def retry(times=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
                    print(f"重试第 {attempt} 次...")
                    time.sleep(delay)

        return wrapper

    return decorator


# ============ 练习 3：叠加使用 ============
# 下面的函数模拟不稳定网络：30% 概率失败。
# 要求：把 @retry 和 @log_time 同时叠在 fetch_url 上（注意顺序！），
#       运行几次，观察输出：失败时自动重试 + 整体耗时统计。
# 思考题：两种叠加顺序（@retry 在上 vs @log_time 在上）输出有什么不同？为什么？
@log_time
@retry(times=3, delay=1)
def fetch_url(url):
    time.sleep(0.5)  # 模拟网络延迟
    if random.random() < 0.3:  # 30% 概率失败
        raise ConnectionError(f"网络抖动：{url}")
    return f"成功获取 {url}"


if __name__ == "__main__":
    for i in range(5):
        try:
            print(fetch_url("https://example.com"), end="\n\n")
        except ConnectionError as e:
            print(f"最终失败: {e}", end="\n\n")

