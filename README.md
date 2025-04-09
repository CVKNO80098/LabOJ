# LabOJ Frontend

## 项目概述

LabOJ 是一个在线评测系统，旨在为学生提供编程题目、代码提交和评测功能。该项目的前端部分使用 Vue.js 构建，提供友好的用户界面和流畅的用户体验。

## 技术栈

### 前端
- **框架**: Vue.js 3
- **路由**: Vue Router
- **样式**: 
  - CSS
  - UI 框架（Bootstrap、Element Plus 或 Ant Design）
- **HTTP 请求**: Axios
- **构建工具**: Vite
- **图标库**: Font Awesome 或 Element Icons
- **数据可视化**: ECharts 或 Chart.js（如有需要）

### 后端
- **框架**: Django
- **REST API**: Django REST framework
- **数据库**: 
  - MySQL
  - SQLite（开发阶段可用）
- **认证**: Token 认证
- **消息队列**: Celery（如有需要）
- **环境管理**: 
  - Python Virtual Environment（venv）
  - pip 或 poetry（依赖管理）

## 功能

- 用户注册和登录
- 题目浏览和筛选
- 代码提交和评测
- 个人提交记录查看

## API 说明

前端与后端使用 RESTful API 进行交互。后端使用 Django REST framework 实现 API，主要接口如下：

### 1. 用户注册
- **请求**: `POST /api/auth/register/`
- **请求体**:
  ```json
  {
    "username": "example",
    "password": "yourpassword",
    "email": "example@example.com"
  }
  ```

### 2. 用户登录
- **请求**: `POST /api/auth/login/`
- **请求体**:
  ```json
  {
    "username": "example",
    "password": "yourpassword"
  }
  ```
- **响应**:
  ```json
  {
    "token": "eb05900e652838248d8dc0a5a76f2c7be84e165a"
  }
  ```

### 3. 注销用户
- **请求**: `POST /api/auth/logout/`
- **请求头**:
  ```
  Authorization: Token <your_token>
  ```

### 4. 获取题目列表
- **请求**: `GET /api/problems/`

### 5. 提交代码
- **请求**: `POST /api/submissions/`
- **请求体**:
  ```json
  {
    "user": 1,  // 用户 ID
    "problem": 2,  // 题目 ID
    "code": "print('Hello World')",
    "status": "Pending"
  }
  ```

## 目录结构

```
/LabOJ
├── /public             
├── /src                # 源代码
│   ├── /components     # 组件
│   ├── /views          # 页面
│   ├── /router         # 路由配置
│   ├── /assets         # 图片和其他资源
│   ├── App.vue         # 根组件
│   └── main.ts         # 入口文件
├── package.json        # 项目信息及依赖
└── vite.config.ts      # Vite 配置文件
```

## 安装和使用


1. 克隆项目到本地：

   ```bash
   git clone https://github.com/CVKNO80098/LabOJ.git
   ```

### 前端（）
2. 进入项目目录：

   ```bash
   cd LabOJ
   ```

3. 安装依赖：

   ```bash
   npm install
   ```

4. 启动开发服务器：

   ```bash
   npm run dev
   ```

5. 在浏览器中访问 `http://localhost:5173` 查看应用。

### 后端
2. 进入项目目录：

   ```bash
   cd LaboratoryOJ
   ```
3. 创建虚拟环境：

   ```bash
   python -m venv .venv
   ```

4. 激活虚拟环境：

   - Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

5. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

6. 进行数据库迁移：

   ```bash
   python manage.py migrate
   ```

7. 创建超级用户（可选）：

   ```bash
   python manage.py createsuperuser
   ```

8. 启动开发服务器：

   ```bash
   python manage.py runserver
   ```

9. 在浏览器中访问 `http://127.0.0.1:8000` 查看后端应用。

## 配置

- **Token 存储**: 前端 Token 应使用 `localStorage` 储存与调用，名称为“token”。

## 许可证

本项目使用 MIT 许可证，详细信息请参阅 [LICENSE](LICENSE) 文件。

## 联系

如有任何问题或建议，请随时联系我：

- **邮箱**: [CVKNO80098@outlook.com]
- **GitHub**: [你的 GitHub 个人主页链接](https://github.com/CVKNO80098)
