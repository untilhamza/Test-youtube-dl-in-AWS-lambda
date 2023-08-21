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
