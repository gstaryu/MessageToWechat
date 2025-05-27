# -*- coding: UTF-8 -*-
from sendToWeChatMessage import send_message, send_error, send_stop


def main():
    "Training......"

    return best_res


if __name__ == "__main__":
    try:
        best_res = main()
        send_stop("实验名称", best_res)
    except Exception as e:
        print(e)
        send_error("实验名称")
