'''
fabric library's connection is used to execute 
commands on a system remotely using ssh
in this example we are creating files in / directory
'''

from fabric import Connection
remote_ip = "192.168.67.129"
def create_files():  
    with Connection(host=remote_ip,user="root",connect_kwargs={"password":"1234"}) as c:    
            c.run("pwd")
            c.run("/touch x{1..15}") 
