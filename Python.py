import sys
import os
import platform

python_version = sys.version
os_name = os.name
platform_name = platform.platform()

html_content = f"<h2>Python is working!</h2><p>Python Version: {python_version}</p><p>OS Name: {os_name}</p><p>Platform Name: {platform_name}</p>"