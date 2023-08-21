## Deploy youtube-dl in lambda function

- This project show how to deploy youtube-dl package in lambda function. It uses [yt-dlp](https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz)
- The binaries for ffmeg and ffprobe are downloaded from [here](https://johnvansickle.com/ffmpeg/) and provided in the project directory. The binaries are compiled for linux x64 architecture.
- The binaries and code are dockerized and deployed in lambda function using AWS ECR.
- The docker file is provided in the code.
- The instructions for deploying to ECR will appear in the AWS console when you create an ECR repository.
- All you have to do is create a repository in ECR and push the docker image to the repository.
- Then create a lambda function and select the "deploy from container image" option. Select the ECR repository and the image you pushed to the repository.
- Ensure to set up the appropriate IAM role for the lambda function.
- The downloaded audio is stored in the /tmp directory of you computer because that is the only directory that can store files in lambda function.

## Fix for issue -> ERROR: Unable to extract uploader id; please report this issue on https://yt-dl.org/bug

- Install from master branch

```bash
python -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
```

This installs tha master version. Run it through the command-line

```bash
yt-dlp URL
```

where URL is the URL of the video you want. See yt-dlp --help for all options. It should just work without errors.

If you're using it as a module,

```python
import yt_dlp as youtube_dl
```
