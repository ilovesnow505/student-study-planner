$ErrorActionPreference = "Stop"
$project = (Get-Location).Path

while ($true) {
    $changes = git status --porcelain
    if ($changes) {
        git add -A
        if (git diff --cached --quiet) {
            git reset
        } else {
            $message = "Auto-save $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
            git commit -m $message
        }
    }
    Start-Sleep -Seconds 5
}