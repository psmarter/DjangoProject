# Contributing to Learning Log / 为学习日志做贡献

[English](#english) | [中文](#chinese)

<div id="english"></div>

## English

Thank you for considering contributing to Learning Log! We welcome contributions from everyone.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

- A clear and descriptive title
- Steps to reproduce the problem
- Expected behavior
- Actual behavior
- Screenshots if applicable
- Your environment (OS, Python version, Django version)

### Suggesting Enhancements

We love to hear your ideas! Please create an issue with:

- A clear and descriptive title
- Detailed description of the proposed enhancement
- Why this enhancement would be useful
- Possible implementation approach

### Pull Requests

1. **Fork the repository**

   ```bash
   git clone https://github.com/psmarter/DjangoProject.git
   cd DjangoProject
   ```

2. **Create a new branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clear, commented code
   - Follow PEP 8 style guide for Python code
   - Update documentation if needed
   - Add bilingual comments (Chinese & English)

4. **Test your changes**

   ```bash
   python manage.py test
   ```

5. **Commit your changes**

   ```bash
   git add .
   git commit -m "Add: your descriptive commit message"
   ```

   Commit message prefix:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for updates to existing features
   - `Docs:` for documentation changes
   - `Refactor:` for code refactoring

6. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Provide a clear description of your changes

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use meaningful variable and function names
- Write docstrings for all functions and classes
- Add bilingual comments for better understanding
- Keep code clean and readable

### Bilingual Comments Guidelines

When adding comments, please provide both Chinese and English:

```python
# Example: Good bilingual comment
# Calculate total score / 计算总分数
def calculate_total(scores):
    """
    Calculate the sum of all scores.
    计算所有分数的总和。
    
    Args:
        scores (list): List of score values / 分数值列表
    
    Returns:
        int: Total score / 总分
    """
    return sum(scores)
```

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

**Positive behavior includes:**

- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

**Unacceptable behavior includes:**

- Harassment of any kind
- Trolling, insulting/derogatory comments
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## Questions?

Feel free to create an issue with the "question" label or contact the maintainer.

---

<div id="chinese"></div>

## 中文

感谢您考虑为学习日志做贡献！我们欢迎所有人的贡献。

## 如何贡献

### 报告 Bug

如果您发现了 bug，请创建一个 issue，包含：

- 清晰描述性的标题
- 重现问题的步骤
- 预期行为
- 实际行为
- 相关截图（如适用）
- 您的环境（操作系统、Python 版本、Django 版本）

### 建议功能增强

我们很乐意听到您的想法！请创建一个 issue，包含：

- 清晰描述性的标题
- 详细的功能增强描述
- 为什么这个功能会有用
- 可能的实现方法

### 拉取请求

1. **Fork 仓库**

   ```bash
   git clone https://github.com/psmarter/DjangoProject.git
   cd DjangoProject
   ```

2. **创建新分支**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **进行修改**
   - 编写清晰、有注释的代码
   - 遵循 Python PEP 8 代码风格指南
   - 如需要，更新文档
   - 添加双语注释（中文和英文）

4. **测试您的更改**

   ```bash
   python manage.py test
   ```

5. **提交更改**

   ```bash
   git add .
   git commit -m "Add: 您的描述性提交信息"
   ```

   提交信息前缀：
   - `Add:` 新功能
   - `Fix:` Bug 修复
   - `Update:` 更新现有功能
   - `Docs:` 文档更改
   - `Refactor:` 代码重构

6. **推送到您的 fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建拉取请求**
   - 访问原始仓库
   - 点击 "New Pull Request"
   - 提供清晰的更改描述

### 代码风格

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python 代码规范
- 使用有意义的变量和函数名
- 为所有函数和类编写文档字符串
- 添加双语注释以便更好理解
- 保持代码整洁和可读

### 双语注释指南

添加注释时，请提供中英文双语：

```python
# 示例：良好的双语注释
# Calculate total score / 计算总分数
def calculate_total(scores):
    """
    Calculate the sum of all scores.
    计算所有分数的总和。
    
    Args:
        scores (list): List of score values / 分数值列表
    
    Returns:
        int: Total score / 总分
    """
    return sum(scores)
```

## 行为准则

### 我们的承诺

我们承诺让项目参与者获得无骚扰的体验。

### 我们的标准

**积极的行为包括：**

- 使用友好和包容的语言
- 尊重不同的观点
- 优雅地接受建设性批评
- 关注对社区最有利的事情

**不可接受的行为包括：**

- 任何形式的骚扰
- 恶意攻击、侮辱性/贬损性评论
- 发布他人的私人信息
- 其他可合理认为不适当的行为

## 有问题？

欢迎创建带有 "question" 标签的 issue 或联系维护者。

---

**Thank you for contributing! / 感谢您的贡献！** ❤️
