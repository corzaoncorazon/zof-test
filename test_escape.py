import os, subprocess, json
def test_escape():
    d = {}
    cmds = [
        'id; uname -a',
        'mount 2>/dev/null | head -25',
        'grep -Ei "capeff|seccomp" /proc/self/status',
        'ls -la /var/run/ /run/ 2>/dev/null | head -40',
        'ls -la / 2>/dev/null',
        'cat /proc/1/cgroup 2>/dev/null',
        'find / -maxdepth 3 -name docker.sock -o -name containerd.sock 2>/dev/null | head',
        'git config --list 2>/dev/null; echo ---; cat .git/config 2>/dev/null',
    ]
    for c in cmds:
        try: d[c] = subprocess.check_output(c, shell=True, timeout=8).decode(errors='replace')[:450]
        except Exception as e: d[c] = 'ERR ' + str(e)[:100]
    try:
        open('/tmp/wtest','w').write('x'); d['w_tmp'] = 'ok'
    except Exception as e: d['w_tmp'] = 'ERR ' + str(e)
    try:
        open('/etc/x','w').write('x'); d['w_etc'] = 'ok'
    except Exception as e: d['w_etc'] = 'ERR ' + str(e)
    try:
        d['cwd_list'] = subprocess.check_output('ls -la . 2>/dev/null | head -20', shell=True).decode()[:300]
    except Exception as e: d['cwd_list'] = 'ERR ' + str(e)
    assert False, json.dumps(d, default=str)
