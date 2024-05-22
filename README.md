# Tut-_
## install packages
## Create a Dockerfile:

Start "Docker Desktop" on Windows 11
<Download: https://www.docker.com/products/docker-desktop/>

docker build -t image_tag .
docker run 47f2578704f3

Issue 1:
(The process started from chrome location /usr/bin/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.)

Solution:
    from selenium.webdriver.chrome.options import Options
and 
    option = Options()
    option.add_argument("--no-sandbox")
    option.add_argument('--Headless')
    option.add_argument('--disable-dev-shm-usage')  # /tmp, not share memory!