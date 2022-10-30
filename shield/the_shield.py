import re
from pathlib import Path
# regex to find if any possible xss vector is there
_PATTERN2 = re.compile(r'[/*:]')

#regex to ensure the xss context
_PATTERN1 = re.compile(r'ja.*pt.*:|d.*a.*:', re.IGNORECASE)


def protect(value):
    try:
        if _PATTERN2.search(value) is not None and _PATTERN1.search(value) is not None:
            return None
    except:
        return value
    return value

def bruter(value):
    # opening event handlers that leads to possible xss attacks
    payloads_dir = (Path(__file__).parent / 'events.txt')
    print(payloads_dir)
    with open(payloads_dir) as f:
        tags = f.readlines()

    for tag in tags:
        # finding the xss context
        got = re.search(r'%s' % tag.replace('\n', ''), value)
        if got is not None:
            return None
    return value