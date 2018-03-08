import requests


r1 = requests.get("vcm-3584.vm.duke.edu/name:5000")

r2 = requests.get("vcm-3584.vm.duke.edu/hello/Petek:5000")

r3 = requests.post("vcm-3584.vm.duke.edu:5000/distance", json={"a":[4,8], "b": [3,6]})
distance = r2.json()

print(r1,r2,distance)
