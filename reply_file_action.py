import yaml
def reply_read():
    with open('reply.yaml', encoding='utf-8') as f:
        return yaml.safe_load(f)