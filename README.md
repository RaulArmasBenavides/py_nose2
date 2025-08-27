# py_nose2
Unit teting with Nose2 and python


Ejecutar en esta terminal : 
$env:Path = "$HOME\.pyenv\pyenv-win\shims;$HOME\.pyenv\pyenv-win\bin;$env:Path"


Opción A — PATH de usuario (recomendado)

En PowerShell (normal, sin admin), ejecuta:

$pyenvDirs = @("$HOME\.pyenv\pyenv-win\shims", "$HOME\.pyenv\pyenv-win\bin")
$uPath = [Environment]::GetEnvironmentVariable("Path","User")
$parts = @()
if ($uPath) { $parts = $uPath -split ';' }
foreach ($d in [System.Linq.Enumerable]::Reverse([string[]]$pyenvDirs)) {
  if (-not ($parts -contains $d)) { $parts = ,$d + $parts }
}
[Environment]::SetEnvironmentVariable("Path", ($parts -join ';'), "User")




Opción B — PATH global (todos los usuarios)

Abre PowerShell como Administrador y ejecuta:

$pyenvDirs = @("$HOME\.pyenv\pyenv-win\shims", "$HOME\.pyenv\pyenv-win\bin")
$mPath = [Environment]::GetEnvironmentVariable("Path","Machine")
$parts = @()
if ($mPath) { $parts = $mPath -split ';' }
foreach ($d in [System.Linq.Enumerable]::Reverse([string[]]$pyenvDirs)) {
  if (-not ($parts -contains $d)) { $parts = ,$d + $parts }
}
[Environment]::SetEnvironmentVariable("Path", ($parts -join ';'), "Machine")



Para cambiar ─ pyenv local 3.9.13