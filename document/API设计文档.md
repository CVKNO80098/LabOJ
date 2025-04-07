# 在线评测（OJ）平台 API 设计文档

## 1. 需求分析

### 1.1 项目背景

为了提升学生编程能力和算法水平，学校计划开发一个在线评测（OJ）平台，提供编程题目、代码提交、评测反馈等功能。

### 1.2 目标用户

- **学生**：提交代码并查看评测结果。
- **教师**：管理题目、查看学生提交记录。
- **管理员**：管理用户、系统配置。

### 1.3 核心功能

- **用户管理**（注册、登录、权限管理）
- **题目管理**（增删改查、题目分类）
- **代码提交**（代码上传、编译、执行）
- **评测系统**（自动化测试、判题机制）
- **结果查询**（提交记录、运行状态、执行时间）
- **答题评分**（按提交结果评分）
- **排行榜**（排名系统、积分规则）

## 2. 系统架构

### 2.1 技术栈

- **后端**：Django REST framework（DRF）
- **数据库**：MySQL
- **判题系统**：Docker + 沙箱环境（如 `QEMU` 或 `NSJail`）
- **前端**：Vue3
- **消息队列**：RabbitMQ / Redis（用于异步评测）

### 2.2 模块划分

1. **用户管理模块**（认证、权限）
2. **题目管理模块**（增删改查）
3. **提交评测模块**（代码上传、执行、返回结果）
4. **评测系统模块**（沙箱执行代码、返回结果）
5. **评分系统模块**（按正确率和效率计算得分）
6. **统计分析模块**（提交记录、排行榜）

## 3. API 设计

### 3.1 认证接口

#### 3.1.1 用户注册

- **URL**：`POST /api/auth/register/`
- **请求参数**：

```json
{
  "username": "test_user",
  "password": "securepassword",
  "email": "user@example.com"
}
```

- **响应示例**：

```json
{
  "message": "User registered successfully",
  "user_id": 1
}
```

#### 3.1.2 用户登录

- **URL**：`POST /api/auth/login/`
- **请求参数**：

```json
{
  "username": "test_user",
  "password": "securepassword"
}
```

- **响应示例**：

```json
{
  "token": "jwt-token-string",
  "user_id": 1
}
```

#### 3.1.3 Token 认证机制

- **测试环境**：所有 API 访问均需身份验证。
- **正式环境**：除了获取题目列表（`GET /api/problems/`）外，所有 API 访问均需身份验证。
- 服务器返回的 `token` 用于后续请求身份验证，前端需将 `token` 存储在 `localStorage` 或 `sessionStorage` 中。
- 访问受保护 API 时，需在 `Authorization` 头部携带 `token`：

```http
Authorization: Bearer jwt-token-string
```

- 服务器解析 `token` 以获取用户身份信息。
- `token` 过期后，需重新登录或使用 **refresh token** 获取新 `token`。

### 3.2 题目管理接口

#### 3.2.1 获取题目列表

- **URL**：`GET /api/problems/`
- **认证要求**：
  - **测试环境**：需身份验证
  - **正式环境**：无需身份验证
- **响应示例**：

```json
[
  {
    "id": 1,
    "title": "两数之和",
    "difficulty": "easy"
  },
  {
    "id": 2,
    "title": "最长回文子串",
    "difficulty": "medium"
  }
]
```

#### 3.2.2 获取题目详情

- **URL**：`GET /api/problems/{problem_id}/`
- **认证要求**：
  - **测试环境**：需身份验证
  - **正式环境**：需身份验证
- **响应示例**：

```json
{
  "id": 1,
  "title": "两数之和",
  "description": "给定一个整数数组和一个目标值，返回两个数的索引，使得它们的和等于目标值。",
  "input_format": "整数数组",
  "output_format": "索引数组",
  "difficulty": "easy"
}
```

### 3.3 代码提交接口

#### 3.3.1 提交代码

- **URL**：`POST /api/submissions/`
- **认证要求**：需身份验证
- **请求参数**：

```json
{
  "problem_id": 1,
  "language": "python",
  "code": "print(\"Hello, World!\")"
}
```

- **响应示例**：

```json
{
  "submission_id": 101,
  "status": "pending"
}
```

#### 3.3.2 获取评测结果

- **URL**：`GET /api/submissions/{submission_id}/`
- **认证要求**：需身份验证
- **响应示例**：

```json
{
  "submission_id": 101,
  "status": "Accepted",
  "execution_time": "12ms",
  "memory_used": "1.2MB",
  "score": 80
}
```

### 3.4 排行榜接口

#### 3.4.1 获取排行榜

- **URL**：`GET /api/leaderboard/`
- **认证要求**：需身份验证
- **响应示例**：

```json
[
  { "rank": 1, "username": "alice", "score": 1500 },
  { "rank": 2, "username": "bob", "score": 1400 }
]
```

## 4. 异常处理

| 错误代码 | 描述                       |
| -------- | -------------------------- |
| 400      | 请求参数错误               |
| 401      | 未授权（token 失效或缺失） |
| 403      | 权限不足                   |
| 404      | 资源不存在                 |
| 500      | 服务器错误                 |

## 5. 未来扩展

- **支持更多语言**（C、C++、Java、Go）
- **实时评测状态推送**（WebSocket）
- **比赛模式**（ACM/ICPC 赛制）
- **OAuth2 登录支持**（支持 GitHub、Google 账户登录）