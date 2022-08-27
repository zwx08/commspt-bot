


from reply_file_action import reply_read


def Image(path):
    return path

def Plain(a):
    return a

reply_yaml=reply_read()
for key,content in reply_yaml["SimpleReply"].items():
    con=[]
    if content != None:
        if "Image" in content:
            if "path" in content["Image"]:
                con.append(Image(path=content["Image"]["path"]))
        if "Plain" in content:
            con.append(Plain(content["Plain"]))
    print(con)