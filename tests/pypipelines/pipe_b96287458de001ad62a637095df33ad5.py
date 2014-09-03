# Pipe pipe_b96287458de001ad62a637095df33ad5 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipeitembuilder import pipe_itembuilder
from pipe2py.modules.pipestrconcat import pipe_strconcat
from pipe2py.modules.pipeitembuilder import pipe_itembuilder
from pipe2py.modules.pipeunion import pipe_union
from pipe2py.modules.pipeoutput import pipe_output

def pipe_b96287458de001ad62a637095df33ad5(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context.describe_input:
        return []

    forever = pipe_forever()


    sw_632 = pipe_itembuilder(
        context, forever, conf=dict(attrs=[dict(value=dict(type='text', value='VAL1'), key=dict(type='text', value='ATTR1')), dict(value=dict(type='text', value='VAL2'), key=dict(type='text', value='attrpath.attr2'))]))

    sw_605 = pipe_strconcat(
        context, forever, conf=dict(part=dict(type='text', value='extVal')))

    sw_551 = pipe_itembuilder(
        context, forever, attrs_3_value=sw_605, conf=dict(attrs=[dict(value=dict(type='text', value='val1'), key=dict(type='text', value='attr1')), dict(value=dict(type='text', value='val2'), key=dict(type='text', value='attrpath.attr2')), dict(value=dict(terminal='attrs_3_value', type='text'), key=dict(type='text', value='attrpath.attr3')), dict(value=dict(type='text', value='val3'), key=dict(type='text', value='longpath.attrpath.attr3'))]))

    sw_613 = pipe_union(
        context, sw_551, _OTHER1=sw_632, conf=dict())

    _OUTPUT = pipe_output(
        context, sw_613, conf=dict())

    return _OUTPUT


if __name__ == "__main__":
    context = Context()
    pipeline = pipe_b96287458de001ad62a637095df33ad5(context, None)

    for i in pipeline:
        print i