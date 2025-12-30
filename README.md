# Learning Log / 学习日志

[English](#english) | [中文](#chinese)

<div id="english"></div>

## 📚 About / 关于项目

**Learning Log** is a web application built with Django that allows users to track and organize their learning journey. Users can create topics they're learning about and make entries to document what they've learned.

**学习日志** 是一个基于 Django 构建的 Web 应用程序，允许用户跟踪和组织他们的学习过程。用户可以创建他们正在学习的主题，并添加条目来记录他们学到的内容。

![Learning Log Demo](docs/images/demo.png)

## ✨ Features / 功能特性

### Core Features / 核心功能

- 🔐 **User Authentication** / **用户认证**
  - Secure registration and login system / 安全的注册和登录系统
  - User-specific data isolation / 用户数据隔离
  
- 📝 **Topic Management** / **主题管理**
  - Create and organize learning topics / 创建和组织学习主题
  - Personal topic ownership / 个人主题所有权
  
- 📖 **Entry System** / **条目系统**
  - Add detailed learning entries for each topic / 为每个主题添加详细的学习条目
  - Edit existing entries / 编辑现有条目
  - Chronological entry organization / 按时间顺序组织条目
  
- 🎨 **Modern UI** / **现代化界面**
  - Bootstrap 5 responsive design / Bootstrap 5 响应式设计
  - Clean and intuitive interface / 简洁直观的界面

## 🖼️ Screenshots / 应用截图

> **Note / 注意**: Add your actual screenshots here / 在此处添加实际截图
>
> See [Contributing Screenshots](#contributing-screenshots) section below.

## 🚀 Quick Start / 快速开始

### Prerequisites / 前置要求

- Python 3.8+ / Python 3.8 或更高版本
- pip (Python package manager) / pip（Python 包管理器）
- Virtual environment (recommended) / 虚拟环境（推荐）

### Installation / 安装步骤

1. **Clone the repository / 克隆仓库**

   ```bash
   git clone https://github.com/psmarter/DjangoProject.git
   cd DjangoProject
   ```

2. **Create and activate virtual environment / 创建并激活虚拟环境**

   **Windows:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies / 安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables / 设置环境变量**

   Copy `.env.example` to `.env` and update the values:

   复制 `.env.example` 为 `.env` 并更新配置：

   ```bash
   cp .env.example .env
   ```

   **Important / 重要**: Update `SECRET_KEY` with a new random key / 使用新的随机密钥更新 `SECRET_KEY`

5. **Run migrations / 执行数据库迁移**

   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional) / 创建超级用户（可选）**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server / 启动开发服务器**

   ```bash
   python manage.py runserver
   ```

8. **Open your browser / 打开浏览器**

   Navigate to / 访问: `http://127.0.0.1:8000/`

## 📖 Usage Guide / 使用指南

### Getting Started / 开始使用

1. **Register an account / 注册账户**
   - Click "Register" on the homepage / 点击首页的"注册"按钮
   - Fill in your username and password / 填写用户名和密码

2. **Create a topic / 创建主题**
   - After logging in, click "New Topic" / 登录后，点击"新建主题"
   - Enter the name of what you're learning / 输入您正在学习的内容名称

3. **Add entries / 添加条目**
   - Click on a topic to view its details / 点击主题查看详情
   - Click "Add new entry" to document what you've learned / 点击"添加新条目"记录您学到的内容

4. **Edit entries / 编辑条目**
   - Click "Edit entry" next to any entry to modify it / 点击条目旁的"编辑条目"来修改

## 🛠️ Technology Stack / 技术栈

- **Backend / 后端**: Django 5.2.4
- **Database / 数据库**: SQLite (default) / SQLite（默认）
- **Frontend / 前端**:
  - HTML5
  - Bootstrap 5 / Bootstrap 5
  - django-bootstrap5
- **Authentication / 认证**: Django built-in authentication / Django 内置认证系统

## 📁 Project Structure / 项目结构

```
DjangoProject/
├── DjangoProject/          # Project configuration / 项目配置
│   ├── settings.py         # Django settings / Django 设置
│   ├── urls.py             # Main URL configuration / 主 URL 配置
│   └── wsgi.py             # WSGI configuration / WSGI 配置
├── learning_log/           # Main application / 主应用
│   ├── models.py           # Data models / 数据模型
│   ├── views.py            # View functions / 视图函数
│   ├── forms.py            # Forms / 表单
│   └── urls.py             # App URL configuration / 应用 URL 配置
├── accounts/               # User authentication app / 用户认证应用
│   ├── views.py            # Auth views / 认证视图
│   └── urls.py             # Auth URLs / 认证 URL
├── templates/              # HTML templates / HTML 模板
│   ├── learning_log/       # Learning log templates / 学习日志模板
│   └── registration/       # Auth templates / 认证模板
├── db.sqlite3              # SQLite database / SQLite 数据库
├── manage.py               # Django management script / Django 管理脚本
└── requirements.txt        # Python dependencies / Python 依赖
```

For detailed architecture, see [ARCHITECTURE.md](docs/ARCHITECTURE.md)

详细架构请参见 [架构文档](docs/ARCHITECTURE.md)

## 🤝 Contributing / 贡献指南

Contributions are welcome! / 欢迎贡献！

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

请阅读 [贡献指南](CONTRIBUTING.md) 了解我们的行为准则和提交拉取请求的流程。

### Contributing Screenshots / 贡献截图

To add screenshots to this README:

要为此 README 添加截图：

1. Create `docs/images/` directory / 创建 `docs/images/` 目录
2. Add your screenshots (PNG/JPG) / 添加您的截图（PNG/JPG）
3. Update image references in README / 更新 README 中的图片引用

## 📄 License / 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 Acknowledgments / 致谢

- Django Framework / Django 框架
- Bootstrap 5 / Bootstrap 5
- All contributors / 所有贡献者

## 📧 Contact / 联系方式

- GitHub: [@psmarter](https://github.com/psmarter)
- Project Link / 项目链接: [https://github.com/psmarter/DjangoProject](https://github.com/psmarter/DjangoProject)

---

<div id="chinese"></div>

## 🌟 Star History / Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=psmarter/DjangoProject&type=Date)](https://star-history.com/#psmarter/DjangoProject&Date)

---

**Made with ❤️ by psmarter / 由 psmarter 用心制作**
