import os

def hello_world():
    try:
        cwd = os.path.curdir
        print('Current working directory: {0}'.format(cwd))
        print('Hello World!')
    except Exception as err:
        print('Exception: {0}'.format(err))
    else:
        print('printAfter printing hello world I am in else clause')
    finally:
        print('Finally, I am here!')

if __name__ == '__main__':
    hello_world()

