import subprocess

procname = "C:\\ffmpeg\\bin\\ffprobe.exe"
video1 = "E:\\Movies\\[ www.UsaBit.com ] - A Walk to Remember (2002) BluRay 720p 700MB Ganool.mkv"
video2 = 'C:\\ps tutorial\\1 - Photoshop CS6 One-on-One - Fundamentals' \
         '\\1 - Opening an Image\\1-1 Welcome to One-on-One.f4v'

directory = "E:\\Movies\\Anik"
directory2 = "C:\\ps tutorial"
directory3 = "E:\\Video tutorials\\Django + AngularJS for a Powerful Web Application"
directory4 = "E:\Video tutorials\SEO"


def findduration(processname, file):
    sp = subprocess.Popen([processname, file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    bindata = sp.stdout.readlines()
    # textdata = [x.decode('utf-8') for x in bindata]
    textdata = []
    for x in bindata:
        try:
            data = x.decode('utf-8')
            textdata.append(data)
        except UnicodeDecodeError:
            pass
    # timelist = [i.split(',')[0].split(':')[1:] for i in textdata if "Duration" in i]
    timelist = []
    for i in textdata:
        if "Duration" in i:
            timelist = i.split(',')[0].split(':')[1:]
    duration = int(float(timelist[2])) + int(timelist[1]) * 60 + int(timelist[0]) * 3600
    return duration


def secondtohms(seconds):
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds"
