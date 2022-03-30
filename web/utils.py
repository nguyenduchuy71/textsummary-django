IMG_EXTENDS = ['jpg', 'png', 'jpeg']

def handle_uploaded_file(f):
    with open('web/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    name = f.name
    if name not in IMG_EXTENDS:
        with open('web/static/upload/'+f.name, "r", encoding="utf-8") as file:
            contents = file.readlines()
        file.close()
        rs = ''
        for s in contents:
            rs += s.strip()
        return rs
