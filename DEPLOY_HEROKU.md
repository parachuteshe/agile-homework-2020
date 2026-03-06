# 部署到 Heroku

## 前置条件

- 已安装 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- 已登录：`heroku login`

## 步骤

### 1. 在项目目录创建 Heroku 应用

```bash
cd /Users/parashe/Downloads/github/agile-homework-2020
heroku create
# 或指定应用名：heroku create agile-homework-2020
```

### 2. 添加 Heroku Postgres 数据库

```bash
heroku addons:create heroku-postgresql:essential-0
```

应用会自动获得 `DATABASE_URL`，无需手动配置。

### 3. （可选）设置环境变量

```bash
heroku config:set SECRET_KEY="你的随机密钥"
heroku config:set DJANGO_DEBUG=0
```

生成 SECRET_KEY：`python -c "import secrets; print(secrets.token_urlsafe(50))"`

### 4. 部署

```bash
git add .
git commit -m "Heroku deployment config"
git push heroku main
```

若本地分支是 `master`：`git push heroku master:main`

### 5. 执行迁移（若 release 未自动执行）

```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser   # 如需管理员
```

### 6. 打开应用

```bash
heroku open
```

## 使用自己的 MySQL 而非 Postgres

若要用 JawsDB MySQL 等：

```bash
heroku addons:create jawsdb
# 然后 DATABASE_URL 会指向 MySQL，代码已支持
```

## 常用命令

- 查看日志：`heroku logs --tail`
- 进入 Django shell：`heroku run python manage.py shell`
- 查看配置：`heroku config`
