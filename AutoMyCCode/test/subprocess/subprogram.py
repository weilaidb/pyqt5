import sys
import time

# #org text
# for i in range(5):
#     sys.stdout.write('Processing {}\n'.format(i))
#     time.sleep(1)
#
# for i in range(5):
#     sys.stderr.write('Error {}\n'.format(i))
#     time.sleep(1)

#changed text
for i in range(5):
    sys.stdout.write('Processing {}\n'.format(i))
    sys.stdout.flush()
    time.sleep(1)

for i in range(5):
    sys.stderr.write('Error {}\n'.format(i))
    sys.stdout.flush()
    time.sleep(1)

