
@echo off
echo === Εγκατάσταση εργαλείων για Data Engineering ===

:: Βήμα 1: Έλεγχος για Chocolatey
where choco >nul 2>nul
if %errorlevel% neq 0 (
    echo Εγκατάσταση Chocolatey...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
)

:: Βήμα 2: Εγκατάσταση Python
choco install python --version=3.11.7 -y

:: Βήμα 3: Εγκατάσταση Git
choco install git -y

:: Βήμα 4: Εγκατάσταση VS Code
choco install vscode -y

:: Βήμα 5: Εγκατάσταση Anaconda (προαιρετικά)
choco install anaconda -y

:: Βήμα 6: Εγκατάσταση Python πακέτων
pip install --upgrade pip
pip install pandas numpy matplotlib notebook jupyterlab virtualenv

:: Βήμα 7: VS Code Extensions
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension eamodio.gitlens

echo === Εγκατάσταση Ολοκληρώθηκε ===
pause
