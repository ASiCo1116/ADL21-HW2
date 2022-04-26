import json

with open('/data/ADL/hw2/train.json', 'r') as f:
    train_file = json.loads(f.read())
# with open('/data/ADL/hw2/valid.json', 'r') as f:
#     validation_file = json.loads(f.read())
# with open('/data/ADL/hw2/test.json', 'r') as f:
#     prediction_file = json.loads(f.read())
    print(train_file)