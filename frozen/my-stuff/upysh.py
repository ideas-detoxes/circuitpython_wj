import sys
import os


class LS:
    def __repr__(self):
        self.__call__()
        return ""

    def __call__(self, path="."):
        l = list(os.listdir(path))
        l.sort()
        for f in l:
            s = os.stat(f)
            if s[0] == 16384:  # stat.S_IFDIR
                print("    <dir> %s" % f)
        for f in l:
            s = os.stat(f)
            if s[0] != 16384:
                if len(s) > 3:
                    print("% 9d %s" % (s[6], f))
                else:
                    print("          %s" % f)
        try:
            st = os.statvfs(path)
            print("\n{:,d}k free".format(st[1] * st[3] // 1024))
        except:
            pass


class PWD:
    def __repr__(self):
        return os.getcwd()

    def __call__(self):
        return self.__repr__()


class CLEAR:
    def __repr__(self):
        return "\x1b[2J\x1b[H"

    def __call__(self):
        return self.__repr__()


def head(f, n=10):
    with open(f) as f:
        for i in range(n):
            l = f.readline()
            if not l:
                break
            sys.stdout.write(l)

def run(f):
    with open(f) as r:
        exec(r.read())

def ed(f):
    if 'pye' not in dir():
        from pye import pye
    pye(f)

def ro():
    if 'storage' not in dir():
        import storage
    storage.remount('/', readonly=True)
    pass

def rw():
    if 'storage' not in dir():
        import storage
    storage.remount('/', readonly=False)
    pass

def reset(bootloader=None):
    import microcontroller
    if not bootloader == None:
        print('Going into BootLoader mode....')
        microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)
    microcontroller.reset()

def bootloader():
    reset(1)
    
def mkFiles():
    import os
    if 'settings.toml' not in os.listdir():
        with open('settings.toml', 'w') as f:
            f.write("""
CIRCUITPY_WIFI_SSID="Szentbigyo"
CIRCUITPY_WIFI_PASSWORD=""
CIRCUITPY_WEB_API_PASSWORD=""
CIRCUITPY_WEB_API_PORT=80
""")

    if 'repl.py' not in os.listdir():
        with open('repl.py', 'w') as f:
            f.write("""
from upysh import *
""")    

def cat(f):
    head(f, 1 << 30)


def cp(s, t):
    try:
        if os.stat(t)[0] & 0x4000:  # is directory
            t = t.rstrip("/") + "/" + s
    except OSError:
        pass
    buf = bytearray(512)
    buf_mv = memoryview(buf)
    with open(s, "rb") as s, open(t, "wb") as t:
        while True:
            n = s.readinto(buf)
            if n <= 0:
                break
            t.write(buf_mv[:n])


def newfile(path):
    print("Type file contents line by line, finish with EOF (Ctrl+D).")
    with open(path, "w") as f:
        while 1:
            try:
                l = input()
            except EOFError:
                break
            f.write(l)
            f.write("\n")


def rm(d, recursive=False):  # Remove file or tree
    try:
        if (os.stat(d)[0] & 0x4000) and recursive:  # Dir
            for f in os.ilistdir(d):
                if f[0] != "." and f[0] != "..":
                    rm("/".join((d, f[0])))  # File or Dir
            os.rmdir(d)
        else:  # File
            os.remove(d)
    except:
        print("rm of '%s' failed" % d)


class Man:
    def __repr__(self):
        return """
upysh commands:
clear, ls, ls(...), head(...), cat(...), newfile(...),
cp('src', 'dest'), mv('old', 'new'), rm(...),
pwd, cd(...), mkdir(...), rmdir(...),
ed(...), run(...), ro(), rw(), mkFiles(), reset(), bootloader()
"""


man = Man()
pwd = PWD()
ls = LS()
clear = CLEAR()

cd = os.chdir
mkdir = os.mkdir
mv = os.rename
rmdir = os.rmdir

print(man)



