from autoscraper import AutoScraper
from flask import Flask, request

amz_scrap = AutoScraper()
amz_scrap.load('amz_search')

app = Flask(__name__)


def get_result(query):
    url = f"https://www.amazon.in/s?k=%s" % query
    result = amz_scrap.get_result_similar(url, group_by_alias=True)
    return agregate(result)


def agregate(result):
    final = []
    print(list(result.values())[0])
    for i in range(len(list(result.values())[0])):
        try:
            final.append({alias: result[alias][i] for alias in result})
        except:
            pass
    return final


@app.route('/', methods=['GET'])

def search_api():
    query = request.args.get('q')
    print(query)
    
    return dict(result=get_result(query))

if __name__ == '__main__':
    app.run(debug = True)
