# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for AI 学术写作助手
用于将前后端项目打包为单个可执行文件
"""

import os
import sys
from PyInstaller.utils.hooks import (
    collect_submodules,
    collect_data_files,
    collect_all
)

# 获取 spec 文件所在目录
spec_dir = os.path.dirname(os.path.abspath(SPEC))

# -------------------------
# 关键修复：收集 jaraco & pkg_resources
# -------------------------
datas_jaraco, binaries_jaraco, hidden_jaraco = collect_all("jaraco")
datas_pkg, binaries_pkg, hidden_pkg = collect_all("pkg_resources")

# -------------------------
# 原有 hidden imports
# -------------------------
hidden_imports = [
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'uvicorn.lifespan',
    'uvicorn.lifespan.on',
    'uvicorn.lifespan.off',
    'httptools',
    'websockets',
    'sqlalchemy.dialects.sqlite',
    'pydantic',
    'pydantic_settings',
    'passlib.handlers.bcrypt',
    'jose',
    'openai',
    'httpx',
    'aiofiles',
    'sse_starlette',
    'redis',
    'dotenv',
    'mistune',
    'docx',
    'lxml',
    'lxml.etree',
    'lxml._elementpath',
]

# 收集子模块
hidden_imports += collect_submodules('uvicorn')
hidden_imports += collect_submodules('sqlalchemy')
hidden_imports += collect_submodules('pydantic')
hidden_imports += collect_submodules('pydantic_settings')
hidden_imports += collect_submodules('fastapi')
hidden_imports += collect_submodules('starlette')
hidden_imports += collect_submodules('mistune')
hidden_imports += collect_submodules('docx')
hidden_imports += collect_submodules('lxml')

# 加入 jaraco / pkg_resources
hidden_imports += hidden_jaraco + hidden_pkg

# -------------------------
# Analysis
# -------------------------
a = Analysis(
    ['main.py'],
    pathex=[spec_dir, os.path.join(spec_dir, 'backend')],
    binaries=binaries_jaraco + binaries_pkg,
    datas=[
        ('static', 'static'),
        ('backend/app', 'app'),
    ] + datas_jaraco + datas_pkg,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'PIL',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AI学术写作助手',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
