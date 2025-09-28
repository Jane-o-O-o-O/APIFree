 ```python
# tests/__init__.py

import pytest
from unittest.mock import patch, Mock

# 假设我们有一个示例模块 example.py，包含一个函数需要测试
# example.py
# def add(a, b):
#     return a + b

# tests/example_test.py
from example import add

# 定义一个fixture，用于提供测试数据
@pytest.fixture
def test_data():
    return [1, 2, 3], [4, 5, 6]

# 定义一个fixture，用于模拟外部依赖
@pytest.fixture
def mock_add():
    with patch('example.add') as mock:
        yield mock

# 测试正面用例
def test_add_positive(test_data, mock_add):
    """
    测试 add 函数的正面用例
    """
    # 准备测试数据
    a, b = test_data
    expected_results = [5, 7, 9]

    # 调用被测试函数
    for a_val, b_val, expected in zip(a, b, expected_results):
        mock_add.return_value = expected
        result = add(a_val, b_val)

        # 断言验证
        assert result == expected, f"Expected {expected}, but got {result}"

# 测试负面用例
def test_add_negative(mock_add):
    """
    测试 add 函数的负面用例
    """
    # 准备测试数据
    a = 10
    b = -5
    expected_result = 5

    # 调用被测试函数
    mock_add.return_value = expected_result
    result = add(a, b)

    # 断言验证
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

# 测试异常处理
def test_add_exception(mock_add):
    """
    测试 add 函数的异常处理
    """
    # 准备测试数据
    a = 10
    b = '5'
    expected_exception = TypeError

    # 调用被测试函数并捕获异常
    with pytest.raises(expected_exception):
        mock_add.side_effect = expected_exception
        add(a, b)
```

这个测试文件使用了pytest框架，并包含了完整的单元测试、测试装置（fixtures）、正面和负面测试用例、mock对象、断言验证和文档字符串。假设 `example.py` 文件中有一个 `add` 函数，测试文件 `tests/example_test.py` 中包含了对 `add` 函数的正面和负面测试用例。