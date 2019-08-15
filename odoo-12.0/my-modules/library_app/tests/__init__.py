# -*- coding: utf-8 -*-
# 测试代码文件名应以test_开头，并通过tests/__init__.py引用。
# 但测试目录（也即 Python 子模块）不应在模块的外层__init__.py
# 中引入，因为仅在测试执行时才会自动查找和加载它。

from . import test_book
