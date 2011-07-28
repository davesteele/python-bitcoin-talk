try:
    json = __import__('simplejson')
except ImportError:
    json = __import__('json')
loads = json.loads
dumps = json.dumps
JSONEncodeException = TypeError
JSONDecodeException = ValueError
