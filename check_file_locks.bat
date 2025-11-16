@echo off
REM Batch script to check which process is using log files
REM Usage: check_file_locks.bat

echo 检查日志文件占用情况...
echo.

REM Check if handle.exe (Sysinternals) is available
where handle.exe >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo 使用 Sysinternals Handle 工具检查...
    echo.
    handle.exe logs\log.txt 2>nul
    handle.exe logs\experience_analysis.log 2>nul
    echo.
    echo 提示: 如果看到 "No matching handles found"，表示文件未被占用
) else (
    echo 未找到 handle.exe 工具
    echo.
    echo 请使用以下方法之一:
    echo 1. 下载 Sysinternals Handle: https://docs.microsoft.com/en-us/sysinternals/downloads/handle
    echo 2. 运行 PowerShell 脚本: check_file_locks.ps1
    echo 3. 手动检查:
    echo    - 关闭所有文本编辑器（Notepad++, VS Code, Notepad等）
    echo    - 检查任务管理器中的 Python 进程
    echo    - 确保没有其他脚本实例在运行
)

echo.
pause

