"""
项目的源代码包

在项目启动时，初始化日志
"""
from resource_rc import qInitResources
from src.log_initialize import LogInitialize

# 初始化日志
log = LogInitialize()
log.initialize()

# 初始化资源
qInitResources()
