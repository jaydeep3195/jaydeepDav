echo "Cleaning up previous builds..."
rm -rf build/

echo "Creating build directory..."
mkdir build

echo "Running tests..."
pytest --junitxml=build/test-results.xml

if [ $? -eq 0 ]; then
    echo "Tests passed. Creating deployable package..."
    cp -r . build/
    tar -czf build/deployable-package.tar.gz -C build/ .
    echo "Build and package creation complete."
else
    echo "Tests failed. Build aborted."
    exit 1
fi