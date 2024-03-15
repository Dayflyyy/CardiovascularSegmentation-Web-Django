### 接口文档

#### 认证
- **登录**
  - URL: `/doctors/login/`
  - 方法: `POST`
  - 描述: 医生登录端点。
  - 请求体:
    ```json
    {
        "name": "string",
        "password": "string"
    }
    ```
  - 响应:
    - 成功:
      - 状态码: 200
      - 返回体:
        ```json
        {
            "token": "string"
        }
        ```
    - 错误:
      - 状态码: 400
      - 返回体:
        ```json
        {
            "error": "请输入用户名和密码"
        }
        ```
      - 状态码: 401
      - 返回体:
        ```json
        {
            "error": "用户名或密码不正确"
        }
        ```

- **登出**
  - URL: `/doctors/logout/`
  - 方法: `POST`
  - 描述: 医生登出端点。
  - 响应:
    - 成功:
      - 状态码: 200
      - 返回体:
        ```json
        {
            "success": "成功退出登录"
        }
        ```

- **注册**
  - URL: `/doctors/register/`
  - 方法: `POST`
  - 描述: 医生注册端点。
  - 请求体:
    ```json
    {
        "username": "string",
        "password": "string",
        "email": "string"
    }
    ```
  - 响应:
    - 成功:
      - 状态码: 201
      - 返回体:
        ```json
        {
            "token": "string"
        }
        ```
    - 错误:
      - 状态码: 400
      - 返回体:
        ```json
        {
            "field_name": ["error message"]
        }
        ```

#### 医生
- **医生列表**
  - URL: `/doctors/`
  - 方法: `GET`
  - 描述: 获取所有医生列表。
  - 权限: `AllowAny`

- **医生个人信息**
  - URL: `/doctors/{id}/profile/`
  - 方法: `GET`
  - 描述: 获取特定医生的个人信息。
  - 权限: `IsAuthenticated`

- **更新医生信息**
  - URL: `/doctors/{id}/`
  - 方法: `PUT`
  - 描述: 更新医生个人信息。
  - 权限: `IsAuthenticated`

#### 病人
- **病人列表**
  - URL: `/patients/`
  - 方法: `GET`
  - 描述: 获取所有病人列表。
  - 权限: `IsAuthenticated, IsDoctorPatient`

- **创建病人**
  - URL: `/patients/`
  - 方法: `POST`
  - 描述: 创建新病人。
  - 请求体:
    ```json
    {
        "name": "string",
        "age": "integer",
        "gender": "string",
        "doctor": "integer"
    }
    ```
  - 权限: `IsAuthenticated, IsDoctorPatient`

- **病人信息**
  - URL: `/patients/{id}/`
  - 方法: `GET`
  - 描述: 获取特定病人信息。
  - 权限: `IsAuthenticated, IsDoctorPatient`

- **更新病人信息**
  - URL: `/patients/{id}/`
  - 方法: `PUT`
  - 描述: 更新特定病人信息。
  - 权限: `IsAuthenticated, IsDoctorPatient`

- **删除病人**
  - URL: `/patients/{id}/`
  - 方法: `DELETE`
  - 描述: 删除特定病人。
  - 权限: `IsAuthenticated, IsDoctorPatient`

#### 病历
- **病历列表**
  - URL: `/records/`
  - 方法: `GET`
  - 描述: 获取所有病历列表。
  - 权限: `IsAuthenticated`

- **创建病历**
  - URL: `/records/`
  - 方法: `POST`
  - 描述: 创建新病历。
  - 请求体:
    ```json
    {
        "patient": "integer",
        "doctor": "integer",
        "diagnosis": "string",
        "prescription": "string"
    }
    ```
  - 权限: `IsAuthenticated`

- **病历信息**
  - URL: `/records/{id}/`
  - 方法: `GET`
  - 描述: 获取特定病历信息。
  - 权限: `IsAuthenticated`

- **更新病历信息**
  - URL: `/records/{id}/`
  - 方法: `PUT`
  - 描述: 更新特定病历信息。
  - 权限: `IsAuthenticated`

- **删除病历**
  - URL: `/records/{id}/`
  - 方法: `DELETE`
  - 描述: 删除特定病历。
  - 权限: `IsAuthenticated`

#### URL

- **管理后台**
  - URL: `/admin/`
  - 描述: Django 管理后台界面。

- **API 根路径**
  - URL: `/`
  - 描述: API 根路径，包含可用端点链接。

- **API 文档**
  - URL: `/docs/`
  - 描述: 交互式 API 文档。

- **API Schema**
  - URL: `/schema/`
  - 描述: API 的 OpenAPI Schema。

#### 注意事项
- 大多数端点需要医生认证。
- 权限设置确保医生只能访问自己的病人和病历。
- API 提供了医生登录、注册、管理病人和管理病历的端点。