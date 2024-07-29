@echo off

echo Cleaning up previous builds...
rmdir /S /Q build

echo Creating build directory...
mkdir build

echo Running tests...
pytest --junitxml=build/test-results.xml
if %ERRORLEVEL% equ 0 (
    echo Tests passed. Creating deployable package...
    xcopy /E /I .\ build\
    tar -czf build\deployable-package.tar.gz -C build .
    echo Build and package creation complete.
) else (
    echo Tests failed. Build aborted.
    exit /B 1
)
