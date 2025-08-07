import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x force')
    os.system('./force')
elif bit == '32bit':
    os.system('chmod +x force32')
    os.system('./force32')
else:
    print('device not supported')
