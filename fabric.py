from fabric import Connection
remote_ip = "192.168.67.129"
def create_files(dir_name):  
    with Connection(host=remote_ip,user="islam",connect_kwargs={"password":"1234"}) as c:  
        with c.cd("/home/client/Desktop/{}".format(dir_name)):  
            c.run("touch files{1..15}") 


create_files('/share')