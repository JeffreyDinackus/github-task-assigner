from flask import Flask,jsonify, request
import json
from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')




app = Flask(__name__)


#import data here and refresh (?) when a get /post is received? what is best practice?

@app.route('/', methods=['GET'])
def query_records():
    #this is for query parameters such as ipaddr/name=xcksdee
    #this part of the code looks at the records and returns json if the record is availible. 
    name = request.args.get('name')
    print(name)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

@app.route('/', methods=['PUT'])
#this part of the code if it is a put request, will create new records. 

#WE NEED TO IMPORT OUR DATA ON SERVER RUN

def create_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)


if __name__ == "__main__":
    app.run(debug=True)