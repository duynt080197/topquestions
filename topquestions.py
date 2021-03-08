"""Viết script lấy top N câu hỏi được vote cao nhất của 'tag' trên stackoverflow.com.
    In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất
    Link API: https://api.stackexchange.com/docs
    Dạng của câu lệnh:

    python3 topquestions.py N tag
    """

import requests
import json
import sys
import html


def get_questions(N, tag):
    """Trả về list chứa tittle, link của N câu hỏi được vote cao nhất
    :param N: Số top câu hỏi
    :param tag: tên tag
    :rtype list:
    """
    r = requests.get(
        "https://api.stackexchange.com/2.2/questions?order=desc&sort=votes&tagged={}&site=stackoverflow".format(
            tag
        )
    )
    data = json.loads(r.text)
    result = []
    for number, item in enumerate(data["items"], 1):
        link = item["link"]
        title = item["title"]
        title = html.unescape(title)
        result.append("Tittle: {}\nLink: {}".format(title, link))
        if number == int(N):
            break
    return result


def main():
    N = sys.argv[1]
    tag = sys.argv[2]
    print("Top {} câu hỏi được vote cao nhất tag {} :".format(N, tag))
    for question in get_questions(N, tag):
        print(question)


if __name__ == "__main__":
    main()
