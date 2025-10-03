blog_system/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── posts.py
│   │   ├── users.py
│   │   ├── auth.py
│   │   └── comments.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── post.py
│   │   ├── user.py
│   │   └── comment.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── post.py
│   │   ├── user.py
│   │   └── comment.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── crud.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── jwt_handler.py
│   │   └── password_utils.py
│   └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_posts.py
│   ├── test_users.py
│   └── test_auth.py
├── requirements.txt
├── README.md
└── alembic/
    ├── README
    ├── env.py
    └── versions/

## app/main.py
- create_app()  # 创建FastAPI应用实例
- configure_routes()  # 配置应用路由

## app/routers/posts.py
- get_posts()  # 获取所有文章列表
- get_post()  # 根据ID获取单篇文章
- create_post()  # 创建新文章
- update_post()  # 更新文章内容
- delete_post()  # 删除文章

## app/routers/users.py
- get_users()  # 获取所有用户列表
- get_user()  # 根据ID获取单个用户
- create_user()  # 创建新用户
- update_user()  # 更新用户信息
- delete_user()  # 删除用户

## app/routers/auth.py
- login()  # 用户登录认证
- register()  # 用户注册
- logout()  # 用户登出
- refresh_token()  # 刷新访问令牌

## app/routers/comments.py
- get_comments()  # 获取文章的所有评论
- create_comment()  # 为文章创建新评论
- update_comment()  # 更新评论内容
- delete_comment()  # 删除评论

## app/models/post.py
- Post  # 文章数据模型类

## app/models/user.py
- User  # 用户数据模型类

## app/models/comment.py
- Comment  # 评论数据模型类

## app/schemas/post.py
- PostCreate  # 文章创建数据验证模型
- PostUpdate  # 文章更新数据验证模型
- PostResponse  # 文章响应数据模型

## app/schemas/user.py
- UserCreate  # 用户创建数据验证模型
- UserUpdate  # 用户更新数据验证模型
- UserResponse  # 用户响应数据模型
- UserLogin  # 用户登录数据验证模型

## app/schemas/comment.py
- CommentCreate  # 评论创建数据验证模型
- CommentUpdate  # 评论更新数据验证模型
- CommentResponse  # 评论响应数据模型

## app/database/db.py
- get_database()  # 获取数据库连接
- close_database()  # 关闭数据库连接
- init_database()  # 初始化数据库

## app/database/crud.py
- create()  # 通用创建数据方法
- get()  # 通用获取单条数据方法
- get_all()  # 通用获取所有数据方法
- update()  # 通用更新数据方法
- delete()  # 通用删除数据方法

## app/auth/jwt_handler.py
- create_access_token()  # 创建访问令牌
- create_refresh_token()  # 创建刷新令牌
- verify_token()  # 验证令牌有效性
- get_current_user()  # 获取当前认证用户

## app/auth/password_utils.py
- hash_password()  # 密码哈希加密
- verify_password()  # 验证密码正确性
- generate_salt()  # 生成密码盐值

## app/config.py
- Settings  # 应用配置设置类
- get_settings()  # 获取应用配置实例

## tests/test_posts.py
- test_create_post()  # 测试创建文章功能
- test_get_post()  # 测试获取文章功能
- test_update_post()  # 测试更新文章功能
- test_delete_post()  # 测试删除文章功能

## tests/test_users.py
- test_create_user()  # 测试创建用户功能
- test_get_user()  # 测试获取用户功能
- test_update_user()  # 测试更新用户功能
- test_delete_user()  # 测试删除用户功能

## tests/test_auth.py
- test_user_login()  # 测试用户登录功能
- test_user_register()  # 测试用户注册功能
- test_token_refresh()  # 测试令牌刷新功能
- test_password_hashing()  # 测试密码哈希功能