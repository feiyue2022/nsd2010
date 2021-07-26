#!/usr/bin/env python
'''
简化除法判断
1. 提示用户输入一个数字作为除法
2. 如果用户按下 Ctrl + C 或 Ctrl + D 则退出程序
3. 如果用户输入非数字字符，提示用户应该输入数字
4. 如果用户输入 0，提示用户 0 不能作为除法
'''
while True:
    try:
        num = input('请输入数字：')
        inum = int(num)
        res = 100 / inum
    except ValueError as e:
        print(e,'必须输入数字')
        continue
    except (KeyboardInterrupt,IOError):
        print('\nBye')
        break
    except ZeroDivisionError:
        print('0不能作为被除数')
        continue
    except Exception:
        print('未知异常')
        continue
    else:
        print(res)
    finally:
        print('Done')