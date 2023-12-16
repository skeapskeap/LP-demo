import time

URLS = ['example.com', 'yandex.ru', 'google.com']


def request_http(url):
    print(f'request {url}')
    time.sleep(1)
    return f'result for {url}'


def url_walker(urls_: list[str]):
    for url in urls_:
        response = request_http(url)
        print(f'yield result for {url}')
        yield response


if __name__ == '__main__':
    time_start = time.time()
    for result in url_walker(URLS):
        print(result)
    print(f'finish in {round(time.time() - time_start, 2)} seconds')
