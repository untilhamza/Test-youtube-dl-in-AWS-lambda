# Get the base image from AWS ECR so that we can run our code in a Lambda-like environment
FROM public.ecr.aws/lambda/python:3.10-x86_64

# Copy FFmpeg and FFprobe binaries
COPY ffmpeg /usr/local/bin/
COPY ffprobe /usr/local/bin/

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Pythons script to the container
COPY lambda_function.py ./

# Set the entry point for the container
CMD ["lambda_function.lambda_handler"]