from flask import abort, request, g
from .. import serverbb
from ..models import docs
from ..models import convenience
from ..app import app
def check_read_authentication_and_create_client(func):
    def wrapper(docid, *args, **kwargs):
        doc = docs.Doc.load(app.servermodel_storage, docid)
        if convenience.can_read_from_request(doc, request, app):
            return func(docid, *args, **kwargs)            
        else:
            abort(401)
    wrapper.__name__ = func.__name__
    return wrapper

def check_write_authentication_and_create_client(func):
    def wrapper(docid, *args, **kwargs):
        doc = docs.Doc.load(app.servermodel_storage, docid)
        if convenience.can_write_from_request(doc, request, app):
            return func(docid, *args, **kwargs)            
        else:
            abort(401)
    wrapper.__name__ = func.__name__
    return wrapper
