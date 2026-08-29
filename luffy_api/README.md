## pip换源
- 在文件管理器的地址栏中输入`%APPDATA%`，快速进入C:\Users\User\AppData\Roaming文件夹中
- 新建pip.ini文件
- 在pip.ini文件中输入以下内容：
```text
[global]
    index-url = https://mirrors.aliyun.com/pypi/simple
    [install]
    use-mirrors =true
    mirrors =https://mirrors.aliyun.com/pypi/simple
    trusted-host =mirrors.aliyun.com
```
## 虚拟环境管理
- `pip install virtualenv`
- `pip install virtualenvwrapper-win`
- 在python解释器下的Scripts文件夹下，双击virtualenvwrapper.bat文件
- 用virtualenv创建虚拟环境：`mkvirtualenv 虚拟环境名称`
- 查看当前已有的虚拟环境：`workon`
- 使用某个虚拟环境：`workon 虚拟环境名`
- 进入|退出 该虚拟环境的Python环境：`python | exit()`
- 退出当前虚拟环境：`deactivate`
- 删除虚拟环境(删除当前虚拟环境要先退出)：`rmvirtualenv 虚拟环境名称`