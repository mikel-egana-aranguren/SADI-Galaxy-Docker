# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417441774.005014
_template_filename='templates/webapps/galaxy/workflow/build_from_current_history.mako'
_template_uri='workflow/build_from_current_history.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['stylesheets', 'javascripts', 'history_item', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x7f5a1834b850', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f5a1834b850')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a1834b850')._populate(_import_ns, [u'render_msg'])
        jobs = _import_ns.get('jobs', context.get('jobs', UNDEFINED))
        warnings = _import_ns.get('warnings', context.get('warnings', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        getattr = _import_ns.get('getattr', context.get('getattr', UNDEFINED))
        def history_item(data,creator_disabled=False):
            return render_history_item(context.locals_(__M_locals),data,creator_disabled)
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        history = _import_ns.get('history', context.get('history', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n')
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n<p>The following list contains each tool that was run to create the\ndatasets in your current history. Please select those that you wish\nto include in the workflow.</p>\n\n<p>Tools which cannot be run interactively and thus cannot be incorporated\ninto a workflow will be shown in gray.</p>\n\n')
        # SOURCE LINE 75
        for warning in warnings:
            # SOURCE LINE 76
            __M_writer(u'    <div class="warningmark">')
            __M_writer(unicode(warning))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 78
        __M_writer(u'\n<form method="post" action="')
        # SOURCE LINE 79
        __M_writer(unicode(h.url_for(controller='workflow', action='build_from_current_history')))
        __M_writer(u'">\n<div class=\'form-row\'>\n    <label>')
        # SOURCE LINE 81
        __M_writer(unicode(_('Workflow name')))
        __M_writer(u'</label>\n    <input name="workflow_name" type="text" value="Workflow constructed from history \'')
        # SOURCE LINE 82
        __M_writer(unicode( util.unicodify( history.name )))
        __M_writer(u'\'" size="60"/>\n</div>\n<p>\n    <input type="submit" value="')
        # SOURCE LINE 85
        __M_writer(unicode(_('Create Workflow')))
        __M_writer(u'" />\n    <button id="checkall" style="display: none;">Check all</button>\n    <button id="uncheckall" style="display: none;">Uncheck all</button>\n</p>\n\n<table border="0" cellspacing="0">\n    \n    <tr>\n        <th style="width: 47.5%">')
        # SOURCE LINE 93
        __M_writer(unicode(_('Tool')))
        __M_writer(u'</th>\n        <th style="width: 5%"></th>\n        <th style="width: 47.5%">')
        # SOURCE LINE 95
        __M_writer(unicode(_('History items created')))
        __M_writer(u'</th>\n    </tr>\n\n')
        # SOURCE LINE 98
        for job, datasets in jobs.iteritems():
            # SOURCE LINE 99
            __M_writer(u'\n    ')
            # SOURCE LINE 100

            cls = "toolForm"
            tool_name = "Unknown"
            if hasattr( job, 'is_fake' ) and job.is_fake:
                cls += " toolFormDisabled"
                disabled = True
                tool_name = getattr( job, 'name', tool_name )
            else:    
                tool = app.toolbox.get_tool( job.tool_id )
                if tool:
                    tool_name = tool.name
                if tool is None or not( tool.is_workflow_compatible ):
                    cls += " toolFormDisabled"
                    disabled = True
                else:
                    disabled = False
                if tool and tool.version != job.tool_version:
                    tool_version_warning = 'Dataset was created with tool version "%s", but workflow extraction will use version "%s".' % ( job.tool_version, tool.version )
                else:
                    tool_version_warning = ''
            if disabled:
                disabled_why = getattr( job, 'disabled_why', "This tool cannot be used in workflows" )
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool_version_warning','tool','disabled_why','disabled','tool_name','cls'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 122
            __M_writer(u'\n    \n    <tr>\n        <td>\n            <div class="')
            # SOURCE LINE 126
            __M_writer(unicode(cls))
            __M_writer(u'">\n\n                <div class="toolFormTitle">')
            # SOURCE LINE 128
            __M_writer(unicode(tool_name))
            __M_writer(u'</div>\n                <div class="toolFormBody">\n')
            # SOURCE LINE 130
            if disabled:
                # SOURCE LINE 131
                __M_writer(u'                        <div style="font-style: italic; color: gray">')
                __M_writer(unicode(disabled_why))
                __M_writer(u'</div>\n')
                # SOURCE LINE 132
            else:
                # SOURCE LINE 133
                __M_writer(u'                        <div><input type="checkbox" name="job_ids" value="')
                __M_writer(unicode(job.id))
                __M_writer(u'" checked="true" />Include "')
                __M_writer(unicode(tool_name))
                __M_writer(u'" in workflow</div>\n')
                # SOURCE LINE 134
                if tool_version_warning:
                    # SOURCE LINE 135
                    __M_writer(u'                            ')
                    __M_writer(unicode( render_msg( tool_version_warning, status="warning" ) ))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 138
            __M_writer(u'                </div>\n            </div>\n        </td>\n        <td style="text-align: center;">\n            &#x25B6;\n        </td>\n        <td>\n')
            # SOURCE LINE 145
            for _, data in datasets:
                # SOURCE LINE 146
                __M_writer(u'                <div>')
                __M_writer(unicode(history_item( data, disabled )))
                __M_writer(u'</div>     \n')
                pass
            # SOURCE LINE 148
            __M_writer(u'        </td>\n    </tr>\n\n')
            pass
        # SOURCE LINE 152
        __M_writer(u'\n</table>\n\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a1834b850')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\n    ')
        # SOURCE LINE 9
        __M_writer(unicode(h.css( 'history', 'base' )))
        __M_writer(u'\n    <style type="text/css">\n    div.toolForm{\n        margin-top: 10px;\n        margin-bottom: 10px;\n    }\n    div.historyItem {\n        margin-right: 0;\n    }\n    th {\n        border-bottom: solid black 1px;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a1834b850')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n    ')
        # SOURCE LINE 25
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    <script type="text/javascript">\n    $(function() {\n        $("#checkall").click( function() {\n            $("input[type=checkbox]").attr( \'checked\', true );\n            return false;\n        }).show();\n        $("#uncheckall").click( function() {\n            $("input[type=checkbox]").attr( \'checked\', false );\n            return false;\n        }).show();\n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_history_item(context,data,creator_disabled=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a1834b850')._populate(_import_ns, [u'render_msg'])
        disabled = _import_ns.get('disabled', context.get('disabled', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if data.state in [ "no state", "", None ]:
            # SOURCE LINE 42
            __M_writer(u'        ')
            data_state = "queued" 
            
            __M_writer(u'\n')
            # SOURCE LINE 43
        else:
            # SOURCE LINE 44
            __M_writer(u'        ')
            data_state = data.state 
            
            __M_writer(u'\n')
            pass
        # SOURCE LINE 46
        __M_writer(u'    <div class="historyItemWrapper historyItem historyItem-')
        __M_writer(unicode(data_state))
        __M_writer(u'" id="historyItem-$data.id">\n        <table cellpadding="0" cellspacing="0" border="0" width="100%">\n            <tr>\n')
        # SOURCE LINE 49
        if data_state != 'ok':
            # SOURCE LINE 50
            __M_writer(u'                    <td style="width: 20px;">\n                        <div style=\'padding-right: 5px;\'><img src="')
            # SOURCE LINE 51
            __M_writer(unicode(h.url_for( str( '/static/style/data_%s.png' % data_state ) )))
            __M_writer(u'" border="0" align="middle"></div>\n                    </td>\n')
            pass
        # SOURCE LINE 54
        __M_writer(u'                <td>\n                    <div style="overflow: hidden;">\n                        <span class="historyItemTitle"><b>')
        # SOURCE LINE 56
        __M_writer(unicode(data.hid))
        __M_writer(u': ')
        __M_writer(unicode(data.display_name()))
        __M_writer(u'</b></span>\n                    </div>\n                </td>\n            </tr>\n        </table>\n')
        # SOURCE LINE 61
        if disabled:
            # SOURCE LINE 62
            __M_writer(u'            <hr>\n            <div><input type="checkbox" name="')
            # SOURCE LINE 63
            __M_writer(unicode(data.history_content_type))
            __M_writer(u'_ids" value="')
            __M_writer(unicode(data.hid))
            __M_writer(u'" checked="true" />')
            __M_writer(unicode(_('Treat as input dataset')))
            __M_writer(u'</div>\n')
            pass
        # SOURCE LINE 65
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a1834b850')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'Extract workflow from history')
        return ''
    finally:
        context.caller_stack._pop_frame()


