from uuid import uuid4


def get_filename(old_name):
    img_format = old_name.rsplit('.', 1)[-1]
    return f'{uuid4()}.{img_format}'


