---
sidebar_position: 4
title: Parameters
description: FastAPI Parameters & Request Body Deep Dive
---

# 🧠 FastAPI Parameters & Request Body – Full Deep Dive 🚀

FastAPI makes parameter handling intuitive, type-safe, and well-documented. Let's break down everything!

## 🔸 1. Path & Query Parameters

### ✅ Path Parameters

Defined in the URL path like `/items/{item_id}`.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

* `item_id` is **mandatory**
* Automatically converted to `int`

### ✅ Query Parameters

Passed via the URL like `/items?name=phone`.

```python
@app.get("/items/")
def read_item(name: str, price: float = 0.0):
    return {"name": name, "price": price}
```

* **Optional** if default value is provided
* FastAPI infers types and validates them

Continue reading for complete parameter handling...