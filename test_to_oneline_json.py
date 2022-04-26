import sys
import json

with open(sys.argv[1], 'r') as f:
    test_file = json.loads(f.read())

with open('oneline_test.json', 'w') as f:
    for line in test_file:
        json.dump(line, f, ensure_ascii=False)
        f.write('\n')
