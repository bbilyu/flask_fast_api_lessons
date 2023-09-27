import sys
import time
import threading
import multiprocessing
import asyncio
import aiohttp
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

async def download_async(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    image_data = await response.read()
                    image_name = url.split('/')[-1]
                    with open(f"static/image/{image_name}", 'wb') as image_file:
                        image_file.write(image_data)
                    return f"Скачано: {image_name}"
                else:
                    return f"Ошибка при скачивании изображения: {url}"
        except Exception as e:
            return f"Ошибка: {str(e)}"

def download(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_data = response.content
            image_name = url.split('/')[-1]
            with open(f"static/image/{image_name}", 'wb') as image_file:
                image_file.write(image_data)
            return f"Скачано: {image_name}"
        else:
            return f"Ошибка при скачивании изображения: {url}"
    except Exception as e:
        print(f'Error: {e}')

async def download_images_async(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_async(url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return results, total_time

def download_images_multiprocess(urls):
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(download, urls)
    end_time = time.time()
    total_time = end_time - start_time
    return results, total_time

def download_images_multithread(urls):
    start_time = time.time()
    results = []
    threads = []
    for url in urls:
        thread = threading.Thread(target=lambda url=url: results.append(download(url)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    return results, total_time

@app.route('/download', methods=['GET', 'POST'])
def download_images():
    if request.method == 'GET':
        return render_template("download.html")
    if request.method == 'POST':
        if not urls:
            return "Пустой список URL-адресов", 400

        async_results, async_total_time = asyncio.run(download_images_async(urls))
        multiprocess_results, multiprocess_total_time = download_images_multiprocess(urls)
        multithread_results, multithread_total_time = download_images_multithread(urls)

        response = {
            "async_result": {res.split(":")[1]:res.split(":")[0] for res in async_results}, "async_time": async_total_time,
            "multiprocess_result": {res.split(":")[1]:res.split(":")[0] for res in multiprocess_results}, "multiprocess_time": multiprocess_total_time,
            "multithread_result": {res.split(":")[1]:res.split(":")[0] for res in multithread_results}, "multithread_time": multithread_total_time,
        }
        print(response)
        return render_template('result.html', **response)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Использование: python app.py <URL1> <URL2> ...")
        sys.exit(1)
    urls = sys.argv[1:]
    app.run(debug=True)