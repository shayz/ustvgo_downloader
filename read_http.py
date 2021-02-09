import shutil
import tempfile
import urllib.request


response = urllib.request.urlopen("http://192.168.5.9:8080/playlist.m3u8?output=ts")
lines = response.readlines()
for line in lines:
  print(line)
