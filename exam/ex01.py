# ex.인터럽트

import time
import signal

def handler(signum, frame):
    print('키보드 인터럽트 감지')
    print('신호 번호:', signum)
    print('스택 프레임:', frame)
    exit()

signal.signal(signal.SIGINT, handler)

while True:
    print('2초 간격으로 출력 중...')
    time.sleep(2)