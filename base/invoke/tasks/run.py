def check_result(result, description):
    if result.failed:
        print('========================================')
        print('Failed to {}'.format(description))
        print('')
        print('========================================')
        print('STDOUT:')
        print('========================================')
        print(result.stdout)
        print('========================================')
        print('STDERR:')
        print('========================================')
        print(result.stderr)
        print('========================================')

        raise Exception('Failed to {}'.format(description))

# def _check_result(command, result):
#     if result.returncode != 0:
#         print(
#             (
#                 '========================================\n'
#                 'Command failed with error code: {}\n'
#                 '{}'
#                 '\n'
#                 '========================================\n'
#                 'STDOUT:\n'
#                 '========================================\n'
#                 '{}'
#                 '\n'
#                 '========================================\n'
#                 'STDERR:\n'
#                 '========================================\n'
#                 '{}'
#                 '\n'
#                 '========================================\n'
#             ).format(
#                 result.returncode,
#                 command,
#                 result.stdout,
#                 result.stderr
#             ),
#             file=sys.stderr, flush=True
#         )
#
#         raise subprocess.CalledProcessError(
#             result.returncode,
#             command
#         )
