import os
import json
import requests
from collections import Counter

dowlaod = False
url = "http://131.114.88.8:3000/api/images"
path_file_json = os.getcwd()+"/images-graph.json"

page = 1                  # first page to be downloaed
limit = 1000             # number of images per page
payload = {'page': page, 'limit': limit}
images_graph = {}
images = []
if dowlaod:
    res = requests.get(url, params=payload).json()
    # "count":87570,"page":1,"limit":200,"pages":438,"images":
    count = res['count']
    pages = res['pages']

    images_graph["num_nodes"] = count

    print("{} number of images to download".format(count))
    print("{} number of total pages".format(pages))

    print("downloading...")
    while page <= pages:
        payload = {'page': page, 'limit': limit}
        res = requests.get(url, params=payload).json()
        for image in res["images"]:
            images.append((image["name"], image["from_repo"]))

        page += 1

    images_graph["edges"] = images

    print("downloaed completed")
    with open(path_file_json, 'w') as f:
        json.dump(images_graph, f, ensure_ascii=False)
        print("Saved into {} ".format(path_file_json))


cnt = Counter()
with open(path_file_json) as json_data:
    images_graph = json.load(json_data)
    edges = images_graph["edges"]
    for edge in edges:
        cnt[edge[1]] += 1

common_parent_images = cnt.most_common(20)
print(common_parent_images)
for image, count in common_parent_images:
    print(image + ", ")
