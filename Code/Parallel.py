from concurrent.futures import ThreadPoolExecutor
import docker
import random

import timeit

def fun(message, client):
    container = client.containers.run("eon01/md5summer", environment=["var=%s" % message], detach=True)
    logs = container.logs()
    print("functional call")
    for line in container.logs(stream=True):
        print (line.strip())
        
client1 = docker.DockerClient(base_url='tcp://52.91.228.226:4243',  tls=False)
client2 = docker.DockerClient(base_url='tcp://3.94.208.113:4243',  tls=False)
messages= ["c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d", "c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d", "c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d"]
pool = ThreadPoolExecutor(50)

clients = [client1,client2]
 
start = timeit.timeit()


i = 0 
for my_message in messages:
    
    if  i % 2  == 0  : 
        fun(my_message,client1)
    else:
        future = pool.submit(fun, (my_message),  client2)
    print(pool)
    print(my_message,"Server",i%2)
    i += 1  
end = timeit.timeit()
print(end - start)
