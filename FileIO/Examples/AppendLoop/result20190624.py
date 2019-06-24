import os
import time

def resultWriter():
    switch = 0
    result = 0
    totalOK = 0
    totalNG = 0
    for i in range(1000):
        if i%100 < 10:
            switch = 0
        else:
            switch = 1
            if i % 2 == 0:
                result = 1
                totalOK+=1
            else:
                result = 0
                totalNG+=1
        fd = open("/home/song/Desktop/result.txt", "a")
        fd.write("%d %d %d %d %d\n" % (i, switch, result, totalOK, totalNG))
        fd.close()
        time.sleep(1)

if __name__ == '__main__':
    resultWriter()



