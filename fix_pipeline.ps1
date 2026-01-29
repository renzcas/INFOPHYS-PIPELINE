# --------------------------------------------
# OPTION A: Move organism files into INFOPHYS/PIPELINE
# --------------------------------------------

Write-Host "Fixing INFOPHYS PIPELINE structure..." -ForegroundColor Cyan

# Paths
$root = "D:\INFOPHYS-PIPELINE"
$engine = "$root\engine"
$pipeline = "$root\INFOPHYS\PIPELINE"
$organs = "$pipeline\organs"

# Ensure target folders exist
if (!(Test-Path $pipeline)) { New-Item -ItemType Directory -Path $pipeline | Out-Null }
if (!(Test-Path $organs)) { New-Item -ItemType Directory -Path $organs | Out-Null }

# Ensure __init__.py files exist
@(
    "$root\INFOPHYS\__init__.py",
    "$pipeline\__init__.py",
    "$organs\__init__.py"
) | ForEach-Object {
    if (!(Test-Path $_)) { New-Item -ItemType File -Path $_ | Out-Null }
}

# Move registry.py and pipeline.py
$filesToMove = @("registry.py", "pipeline.py")

foreach ($file in $filesToMove) {
    $src = "$engine\$file"
    $dst = "$pipeline\$file"
    if (Test-Path $src) {
        Move-Item -Force $src $dst
        Write-Host "Moved $file → PIPELINE/" -ForegroundColor Green
    }
}

# Move ALL organ files from engine to PIPELINE/organs
$organFiles = Get-ChildItem -Path $engine -Filter *.py | Where-Object {
    $_.Name -notin @("registry.py", "pipeline.py")
}

foreach ($file in $organFiles) {
    $src = $file.FullName
    $dst = "$organs\$($file.Name)"
    Move-Item -Force $src $dst
    Write-Host "Moved organ $($file.Name) → PIPELINE/organs/" -ForegroundColor Green
}

Write-Host "PIPELINE fix complete." -ForegroundColor Cyan
Write-Host "You can now run: uvicorn INFOPHYS.backend.app.server:app --reload" -ForegroundColor Yellow