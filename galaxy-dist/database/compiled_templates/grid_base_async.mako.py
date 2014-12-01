# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417442147.008255
_template_filename='templates/grid_base_async.mako'
_template_uri='grid_base_async.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace(u'grid_base', context._clean_inheritance_tokens(), templateuri=u'./grid_base.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'grid_base')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'grid_base')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        init = _import_ns.get('init', context.get('init', UNDEFINED))
        grid_base = _mako_get_namespace(context, 'grid_base')
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(unicode(init()))
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(unicode(h.dumps( grid_base.get_grid_config() )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


