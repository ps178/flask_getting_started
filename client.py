import requests


r1 = requests.get("http://vcm-3584.vm.duke.edu:5000/name")
name = r1.json()

r2 = requests.get("http://vcm-3584.vm.duke.edu:5000/hello/Petek")
hello = r2.json()

#r3 = requests.post("http://vcm-3584.vm.duke.edu:5000/distance", json={"a":[4,8], "b": [3,6]})
#distance = r3.json()

print(name, hello)
