import os
import time


def rizhi(*args):
    # 日志存放目录
    shijian = time.strftime("%Y-%m-%d")
    shijian1 = time.strftime("%Y-%m-%d-%H-%M-%S")
    path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) + "/rzcf/" + shijian + ".log"

    with open(path, "a", encoding="utf-8") as f:
        f.write(shijian1 + "\n")
        for i in args:
            f.write(i + " ")

        f.write("\n")


if __name__ == "__main__":
    rizhi("测试1", "滴滴2", "1234", "aaaaa")
