#!/bin/bash

# Navigate to site-packages directory
cd .venv/lib/python3.10/site-packages/

# Create zip file with all packages
zip -r ../../../../function.zip .

# Navigate back to root directory
cd ../../../../

# Add the lambda function python file to the zip file
zip function.zip lambda_function.py

# Optional: print completion message
echo "Package has been successfully created and ready for upload."
