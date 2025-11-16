# PowerShell script to check which process is using log files
# Usage: .\check_file_locks.ps1

$logFiles = @(
    "logs\log.txt",
    "logs\experience_analysis.log"
)

Write-Host "检查日志文件占用情况..." -ForegroundColor Cyan
Write-Host ""

foreach ($file in $logFiles) {
    $fullPath = Join-Path $PSScriptRoot $file
    
    if (Test-Path $fullPath) {
        Write-Host "检查文件: $file" -ForegroundColor Yellow
        
        # Method 1: Using Get-Process and file handles (requires admin)
        try {
            $processes = Get-Process | Where-Object {
                $_.Path -and (Test-Path $_.Path)
            }
            
            $found = $false
            foreach ($proc in $processes) {
                try {
                    $handles = $proc.OpenFiles() 2>$null
                    if ($handles) {
                        foreach ($handle in $handles) {
                            if ($handle.FileName -like "*$file*" -or $handle.FileName -eq $fullPath) {
                                Write-Host "  [找到] 进程: $($proc.ProcessName) (PID: $($proc.Id))" -ForegroundColor Green
                                Write-Host "    路径: $($proc.Path)" -ForegroundColor Gray
                                $found = $true
                            }
                        }
                    }
                } catch {
                    # Some processes may not allow access
                }
            }
            
            if (-not $found) {
                Write-Host "  [未找到] 没有进程占用此文件" -ForegroundColor Green
            }
        } catch {
            Write-Host "  [错误] 无法检查进程（可能需要管理员权限）" -ForegroundColor Red
        }
        
        Write-Host ""
    } else {
        Write-Host "文件不存在: $file" -ForegroundColor Red
        Write-Host ""
    }
}

Write-Host "提示: 如果文件被占用，常见原因包括:" -ForegroundColor Cyan
Write-Host "  1. 文本编辑器（如 Notepad++, VS Code, Notepad）打开了日志文件" -ForegroundColor White
Write-Host "  2. 另一个 Python 脚本实例正在运行" -ForegroundColor White
Write-Host "  3. 文件资源管理器正在预览文件" -ForegroundColor White
Write-Host ""
Write-Host "解决方法:" -ForegroundColor Cyan
Write-Host "  1. 关闭所有可能打开日志文件的程序" -ForegroundColor White
Write-Host "  2. 检查任务管理器中的 Python 进程" -ForegroundColor White
Write-Host "  3. 重启脚本" -ForegroundColor White

