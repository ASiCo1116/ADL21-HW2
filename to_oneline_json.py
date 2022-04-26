import json

# with open('/data/ADL/hw2/train.json', 'r') as f:
#     train_file = json.loads(f.read())
# with open('/data/ADL/hw2/valid.json', 'r') as f:
#     validation_file = json.loads(f.read())
# predict = [json.loads(line) for line in open('/data/ADL/hw2/my_test.json', 'r')]
# print(len(predict))

# with open('/data/ADL/hw2/my_train.json', 'w') as f:
#     for t in train_file:
#         json.dump(t, f, ensure_ascii=False)
#         f.write('\n')
# with open('/data/ADL/hw2/my_valid.json', 'w') as f:
#     for t in validation_file:
#         json.dump(t, f, ensure_ascii=False)
#         f.write('\n')
# with open('/data/ADL/hw2/my_test.json', 'w') as f:
#     for t in prediction_file:
#         json.dump(t, f, ensure_ascii=False)
#         f.write('\n')
