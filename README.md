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

### 升级 Pip 包管理器

```cmd
C:\Workspace\nfc-cloud (master -> origin)
(venv) λ python -m pip install --upgrade pip
Collecting pip
  Using cached https://files.pythonhosted.org/packages/c2/d7/90f34cb0d83a6c5631cf71dfe64cc1054598c843a92b400e55675cc2ac37/pip-18.1-py2.py3-none-any.whl
Installing collected packages: pip
  Found existing installation: pip 10.0.1
    Uninstalling pip-10.0.1:
      Successfully uninstalled pip-10.0.1
Successfully installed pip-18.1
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
