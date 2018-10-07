from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.traceroute


def insert_task(task_id, target):
    data = {
        'task_id': task_id,
        'target': target
    }
    res = db.tasks.insert_one(data)
    # print('One post: {}'.format(res.inserted_id))
    print('task inserted for {}'.format(task_id))


def insert_new_result(task_id):
    data = {
        'task_id': task_id,
        'status': 'in process',
        'nodes': []
    }
    res = db.results.insert_one(data)
    # print('One post: {}'.format(res.inserted_id))
    print('new result inserted for {}'.format(task_id))


def append_result(task_id, new_node):
    db.results.update_one({
        'task_id': task_id
    }, {
        '$push': {
            'nodes': new_node
        }
    }, upsert=False)
    print('new node appended for {}'.format(task_id))


def update_result_status(task_id, status):
    db.results.update_one({
        'task_id': task_id
    }, {
        '$set': {
            'status': status
        }
    }, upsert=False)
    print('status changed to {} for {}'.format(status, task_id))


def get_result(task_id):
    result = db.results.find_one({"task_id": task_id})
    result.pop('_id')
    return result
