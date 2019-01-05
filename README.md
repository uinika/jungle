# Jungle

![](./static/logo.png)

## 安装步骤

### 建立虚拟环境

```cmd
C:\Workspace\django
λ python -m venv venv
```

### 激活虚拟环境

```cmd
C:\Workspace\django
λ .\venv\Scripts\activate.bat
(venv) λ
```

### 安装项目依赖包

```cmd
pip install -r requirements.txt
```

### 启动 Django 服务

```cmd
(venv) λ python manage.py runserver 8080
Performing system checks...

System check identified no issues (0 silenced).
January 03, 2019 - 21:31:48
Django version 2.1.4, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CTRL-BREAK.
```
