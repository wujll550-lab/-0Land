# -*- coding: utf-8 -*-
"""
第二周练习：asyncio 入门
目标：用同一组 URL，对比「同步逐个请求」和「异步并发请求」的耗时差距。
运行前先激活虚拟环境：source .venv/bin/activate
"""
import time
import asyncio
import httpx

# 每个请求服务器会延迟 0.5 秒才响应（10 个 URL）
URLS = [f"https://httpbin.org/delay/0.5?n={i}" for i in range(10)]


# ============ 练习 1：第一个协程 ============
# 目标：用 async def 写一个协程 fetch_one(i)，里面 await asyncio.sleep(0.5)
#       模拟网络等待，返回 f"任务{i}完成"。
#       再写 async def main()，用 asyncio.gather 并发跑 3 个 fetch_one，
#       打印返回的列表。
# 思考：3 个各等 0.5 秒的任务并发跑，总耗时是 1.5 秒还是 0.5 秒？为什么？
async def fetch_one(i: int):
    await asyncio.sleep(0.5)
    return f"任务{i}完成"


async def main_demo():
    t0 = time.perf_counter()
    results = await asyncio.gather(fetch_one(1), fetch_one(2), fetch_one(3))
    print(f"总耗时: {time.perf_counter()-t0:.2f} 秒")
    print(results)


# ============ 练习 2：同步版（对照实验）============
# 目标：sync_fetch_all()：用 with httpx.Client() as client 逐个请求 URLS，
#       打印每个请求的状态码，返回总耗时。
# 提示：client.get(url)；响应状态码在 resp.status_code
def sync_fetch_all():
    with httpx.Client() as client:
        for url in URLS:
            resp = client.get(url)
            print(f"{url} -> {resp.status_code}")


# ============ 练习 3：异步版（主角）============
# 目标：async_fetch_all()：用 async with httpx.AsyncClient() as client，
#       配合 asyncio.gather 并发请求所有 URLS，返回总耗时。
# 提示：先定义一个 async def fetch(client, url)，再 gather 一堆 fetch
async def fetch(client, url):
    resp = await client.get(url)
    return url, resp.status_code

async def async_fetch_all():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in URLS]
        results = await asyncio.gather(*tasks)
        for url, status in results:
            print(f"{url} -> {status}")


# ============ 练习 4：理解 await 的执行顺序 ============
# 先猜，再运行验证：
#   协程 A：print("A1") → await asyncio.sleep(0.1) → print("A2")
#   协程 B：print("B1") → await asyncio.sleep(0.2) → print("B2")
#   用 asyncio.gather 并发跑 A、B，输出顺序是什么？为什么？
# 提示：await 是「让出控制权」的点

# ============ 加分题 ============
# 1. 用 asyncio.as_completed 实现「谁先回来先处理谁」
# 2. 一句话回答：什么是事件循环（event loop）？
# 3. asyncio.create_task 和直接 await 一个协程有什么区别？
# 4. 为什么 time.sleep 不能用在协程里？（试试会发生什么）


if __name__ == "__main__":
    t0 = time.perf_counter()
    sync_fetch_all()
    print(f"同步总耗时: {time.perf_counter()-t0:.2f} 秒\n")
    t0 = time.perf_counter()
    asyncio.run(async_fetch_all())
    print(f"异步总耗时: {time.perf_counter()-t0:.2f} 秒")
    asyncio.run(main_demo())
    
