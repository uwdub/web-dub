@echo off
rem Opens a command prompt in the project folder with the portable legacy toolchain
rem (Python 3.6.6, Node 8.12.0, Ruby 2.5.1) available. Nothing is installed system-wide.
rem The tools live in the git-ignored .legacy-tools folder; see .legacy-tools\README.txt.
if not exist "%~dp0.legacy-tools\env.cmd" (echo The .legacy-tools folder is missing. See the project notes to rebuild it. & pause & exit /b 1)
cd /d "%~dp0"
cmd /k "call .legacy-tools\env.cmd & prompt (legacy) $P$G & echo Legacy toolchain active: & ruby --version & python --version & node --version & echo. & echo Try: invoke -l ^| invoke serve_test ^| nosetests tests.fast ^| nosetests"