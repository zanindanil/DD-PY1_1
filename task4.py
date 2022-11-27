import json
INPUT_FILE = "input.csv"
def collect_dict(name,new_line="\n",delimiter=","):
    all_dict = []
    data = []
    dict = {}
    with open(name) as f:
        k=0
        for i in f:
            headers=i.strip(new_line).split(delimiter)
            if k>=0:
                break
        for j in f:
            if k>=0:
              data.append(j.strip(new_line).split(delimiter))
            k+=1
        k=0
        for symbol in data:
            k=0
            for head in headers:
                dict[head]=symbol[k]
                k+=1
            all_dict.append(dict)
            dict={}
    return all_dict
print(json.dumps(collect_dict(INPUT_FILE),indent=4))