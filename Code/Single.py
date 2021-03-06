from concurrent.futures import ThreadPoolExecutor
import docker

import timeit 



def fun(message, client):
    container = client.containers.run("eon01/md5summer", environment=["var=%s" % message], detach=True)
    logs = container.logs()
    
    for line in container.logs(stream=True):
        print (line.strip())
client1 = docker.DockerClient(base_url='tcp://52.91.228.226:4243',  tls=False)
messages= [
"c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d", "c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d", "c4ca4238a0b923820dcc509a6f75849b", "c4ca4238a0b923820dcc509a6f758491", "c4ca4238a0b923820dcc509a6f75849c", "c4ca4238a0b923820dcc509a6f75849d"
]
pool = ThreadPoolExecutor(50)
 
start = timeit.timeit()

print("Testing")
for my_message in messages:
    future = pool.submit(fun, (my_message), client1 )
    print(my_message)
print("Done")

end = timeit.timeit()
print(end - start)
