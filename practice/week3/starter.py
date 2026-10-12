# -*- coding: utf-8 -*-
"""
第三周练习：FastAPI —— 你的第一个 HTTP 服务
目标：从零写一个 TODO 应用的后端 API，最终跑通完整 CRUD。

运行方式（在 practice/week3 目录下）：
    uvicorn starter:app --reload
然后浏览器打开 http://127.0.0.1:8000/docs 查看交互式文档
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


# ============ 练习 1：Hello World ============
# 目标：一个 GET / 路由，返回 {"message": "Hello FastAPI"}。
# 提示：@app.get("/") 是装饰器——想起第一周了吗？知识闭环了。
# @app.get("/")
# def hello():
#     return {"message": "Hello FastAPI"}


# ============ 练习 2：路径参数与查询参数 ============
# 目标 A：GET /hello/{name} → 返回 {"hello": name}
#         （路径参数：URL 里的一部分，用花括号声明）
# 目标 B：GET /double?num=5 → 返回 {"result": 10}
#         （查询参数：问号后面的 key=value；FastAPI 会按你声明的类型自动转换）
# 思考：路径参数和查询参数在语义上有什么区别？
# @app.get("/hello/{name}")
# def hello_name(name: str):
#     return {"hello": name}


# @app.get("/double")
# def double(num: int):
#     return {"result": num * 2}


# ============ 练习 3：请求体 + Pydantic 模型 ============
# 目标：定义 TodoItem 模型（title: str, done: bool = False），
#       POST /todos 接收 JSON 请求体，返回「创建成功」+ 数据。
# 提示：class TodoItem(BaseModel) —— 类型标注即校验：
#       传错类型 FastAPI 自动返回 422，不信你试试。
class TodoItem(BaseModel):
    title: str
    done: bool = False

# @app.post("/todos")
# async def create_todo(item: TodoItem):
#     return {"message": "创建成功", "data": item}


# ============ 练习 4：SQLite 完整 CRUD（本周核心）============
# 目标：用标准库 sqlite3 把 TODO 存进数据库（文件 todos.db）：
#   POST   /todos        创建（自动分配自增 id）
#   GET    /todos        列出全部
#   GET    /todos/{id}   查单个（不存在时 raise HTTPException(404)）
#   PUT    /todos/{id}   更新 title/done
#   DELETE /todos/{id}   删除
# 提示：sqlite3.connect("todos.db")；
#       CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, done INTEGER)
#       用 conn.execute(...) + conn.commit()；查询用 .fetchall() / .fetchone()
# 注意：不要在全局变量里存数据——要用数据库（服务器重启数据还在）
def init_db():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        done INTEGER)'''
    )
    conn.commit()
    cursor.close()
    conn.close()

init_db()

@app.post("/todos")
async def create_todo(item: TodoItem):
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO todos (title, done) VALUES (?, ?)", (item.title, int(item.done)))
        conn.commit()
        todo_id = cursor.lastrowid
        cursor.close()
    return {"message": "创建成功", "data": {"id": todo_id, "title": item.title, "done": item.done}}

@app.get("/todos")
async def list_todos(done:bool|None = None):
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        if done is not None:
            cursor.execute("SELECT id, title, done FROM todos WHERE done = ?", (int(done),))
        else:
            cursor.execute("SELECT id, title, done FROM todos")
        todos = [{"id": row[0], "title": row[1], "done": bool(row[2])} for row in cursor.fetchall()]
        cursor.close()
    return {"todos": todos}

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, done FROM todos WHERE id = ?", (todo_id,))
        row = cursor.fetchone()
        cursor.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"id": row[0], "title": row[1], "done": bool(row[2])}    

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, item: TodoItem):
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE todos SET title = ?, done = ? WHERE id = ?", (item.title, int(item.done), todo_id))
        conn.commit()
        cursor.close()
    return {"message": "更新成功", "data": {"id": todo_id, "title": item.title, "done": item.done}}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    with sqlite3.connect("todos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        conn.commit()
        cursor.close()
    return {"message": "删除成功", "id": todo_id}


# ============ 加分题 ============
# 1. GET /todos 支持 ?done=true / ?done=false 过滤
# 2. 查资料：HTTP 状态码 200/201/400/404/422/500 分别是什么意思？
# 3. 用 /docs 页面把每个接口都点一遍，观察请求和响应


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
