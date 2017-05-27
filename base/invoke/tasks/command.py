import subprocess
import sys


def run(command, error_on_failure=True):
    # for line in process.stdout:
    #     flag_print = line.startswith('Step ')
    #
    #     if flag_print:
    #         print(line, end='', flush=True)

    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    output = ''
    for line in process.stdout:
        output += line
        print(
            line.encode(sys.getdefaultencoding(), errors='backslashreplace').decode(sys.getdefaultencoding()),
            end='',
            flush=True
        )

    process.wait()
    process.stdout = output
    process.stderr = process.stderr.read()
    process.failed = process.returncode != 0

    if process.failed:
        if error_on_failure:
            print(
                (
                    '========================================\n'
                    'Command failed with error code: {}\n'
                    '========================================\n'
                    'COMMAND:\n'
                    '========================================\n'
                    '{}'
                    '\n'
                    '========================================\n'
                    'STDOUT:\n'
                    '========================================\n'
                    '{}'
                    '\n'
                    '========================================\n'
                    'STDERR:\n'
                    '========================================\n'
                    '{}'
                    '\n'
                    '========================================\n'
                ).format(
                    process.returncode,
                    command,
                    process.stdout,
                    process.stderr
                ),
                file=sys.stderr, flush=True
            )

            raise subprocess.CalledProcessError(
                process.returncode,
                command
            )

    return process
