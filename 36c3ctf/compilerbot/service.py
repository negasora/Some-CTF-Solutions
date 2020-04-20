#!/usr/bin/env python3

import base64
import subprocess

code = base64.b64decode(input('> ')).decode()
code = 'int main(void) {' + code.translate(str.maketrans('', '', '{#}')) + '}'

result = subprocess.run(['/usr/bin/clang', '-x', 'c', '-std=c11', '-Wall',
                         '-Wextra', '-Werror', '-Wmain', '-Wfatal-errors',
                         '-o', '/dev/null', '-'], input=code.encode(),
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                        timeout=15.0)

if result.returncode == 0 and result.stdout.strip() == b'':
    print('OK')
else:
    print('Not OK')
