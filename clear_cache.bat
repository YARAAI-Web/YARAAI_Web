@echo off
REM ========================================
REM 프로젝트 루트(여기에 clear_cache.bat 저장)
REM ========================================

echo == Clearing backend uploads ==
rmdir /s /q "%~dp0backend\uploads"
mkdir "%~dp0backend\uploads%"

echo == Clearing backend meta_json ==
rmdir /s /q "%~dp0backend\meta_json"
mkdir "%~dp0backend\meta_json%"

echo == Clearing backend callgraphs ==
rmdir /s /q "%~dp0backend\static\callgraphs"
mkdir "%~dp0backend\static\callgraphs%"

echo == Clearing root gpt_cache ==
rmdir /s /q "%~dp0gpt_cache"
mkdir "%~dp0gpt_cache%"

echo Done.
pause
