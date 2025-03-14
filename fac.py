def factorial(n):
    # 处理 n 为负数的情况，阶乘只定义于非负整数
    if n < 0:
        return None
    # 递归终止条件：0 的阶乘为 1
    if n == 0:
        return 1
    # 递归调用
    return n * factorial(n - 1)
