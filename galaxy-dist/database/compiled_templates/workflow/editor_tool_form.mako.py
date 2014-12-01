# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417441813.18923
_template_filename='templates/webapps/galaxy/workflow/editor_tool_form.mako'
_template_uri='workflow/editor_tool_form.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['do_inputs', 'row_for_param']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        errors = context.get('errors', UNDEFINED)
        h = context.get('h', UNDEFINED)
        tool = context.get('tool', UNDEFINED)
        def do_inputs(inputs,values,errors,prefix,ctx=None):
            return render_do_inputs(context.locals_(__M_locals),inputs,values,errors,prefix,ctx)
        values = context.get('values', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1

        from galaxy.tools.parameters import DataToolParameter, RuntimeValue
        from galaxy.tools.parameters import DataCollectionToolParameter
        from galaxy.util.expressions import ExpressionContext
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['DataCollectionToolParameter','RuntimeValue','ExpressionContext','DataToolParameter'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 49
        __M_writer(u'\n\n')
        # SOURCE LINE 106
        __M_writer(u'\n\n<form method="post" action="')
        # SOURCE LINE 108
        __M_writer(unicode(h.url_for(controller='workflow', action='editor_form_post' )))
        __M_writer(u'">\n\n    <div class="toolForm">\n        <div class="toolFormTitle">Tool: ')
        # SOURCE LINE 111
        __M_writer(unicode(tool.name))
        __M_writer(u'</div>\n')
        # SOURCE LINE 112
        if tool.version:
            # SOURCE LINE 113
            __M_writer(u'            <div class="form-row"><div class=\'titleRow\'>Version: ')
            __M_writer(unicode(tool.version))
            __M_writer(u'</div></div>\n')
            pass
        # SOURCE LINE 115
        __M_writer(u'        <div class="toolFormBody">\n            <input type="hidden" name="tool_id" value="')
        # SOURCE LINE 116
        __M_writer(unicode(tool.id))
        __M_writer(u'" />\n')
        # SOURCE LINE 117
        for i, inputs in enumerate( tool.inputs_by_page ):
            # SOURCE LINE 118
            if tool.has_multiple_pages:
                # SOURCE LINE 119
                __M_writer(u"                    <div class='titleRow'>Page ")
                __M_writer(unicode(i+1))
                __M_writer(u'</div>\n')
                pass
            # SOURCE LINE 121
            __M_writer(u'                ')
            __M_writer(unicode(do_inputs( inputs, values, errors, "" )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 123
        __M_writer(u'        </div>\n    </div>\n    \n\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_do_inputs(context,inputs,values,errors,prefix,ctx=None):
    context.caller_stack._push_frame()
    try:
        def row_for_param(param,value,error_dict,prefix,ctx,allow_runtime=True):
            return render_row_for_param(context,param,value,error_dict,prefix,ctx,allow_runtime)
        def do_inputs(inputs,values,errors,prefix,ctx=None):
            return render_do_inputs(context,inputs,values,errors,prefix,ctx)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        ExpressionContext = context.get('ExpressionContext', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n  ')
        # SOURCE LINE 8
        ctx = ExpressionContext( values, ctx ) 
        
        __M_writer(u'\n')
        # SOURCE LINE 9
        for input_index, input in enumerate( inputs.itervalues() ):
            # SOURCE LINE 10
            if input.type == "repeat":
                # SOURCE LINE 11
                __M_writer(u'      <div class="repeat-group form-row">\n          <label>')
                # SOURCE LINE 12
                __M_writer(unicode(input.title_plural))
                __M_writer(u':</label>\n          ')
                # SOURCE LINE 13
                repeat_values = values[input.name] 
                
                __M_writer(u'\n')
                # SOURCE LINE 14
                for i in range( len( repeat_values ) ):
                    # SOURCE LINE 15
                    __M_writer(u'            ')

                    if input.name in errors:
                        rep_errors = errors[input.name][i]
                    else:
                        rep_errors = dict()
                    index = repeat_values[i]['__index__']
                    
                    
                    # SOURCE LINE 21
                    __M_writer(u'\n            <div class="repeat-group-item">\n            <div class="form-title-row"><label>')
                    # SOURCE LINE 23
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i + 1))
                    __M_writer(u'</label></div>\n            ')
                    # SOURCE LINE 24
                    __M_writer(unicode(do_inputs( input.inputs, repeat_values[ i ], rep_errors,  prefix + input.name + "_" + str(index) + "|", ctx )))
                    __M_writer(u'\n            <div class="form-row"><input type="submit" name="')
                    # SOURCE LINE 25
                    __M_writer(unicode(prefix))
                    __M_writer(unicode(input.name))
                    __M_writer(u'_')
                    __M_writer(unicode(index))
                    __M_writer(u'_remove" value="Remove ')
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i+1))
                    __M_writer(u'"></div>\n            </div>\n')
                    pass
                # SOURCE LINE 28
                __M_writer(u'          <div class="form-row"><input type="submit" name="')
                __M_writer(unicode(prefix))
                __M_writer(unicode(input.name))
                __M_writer(u'_add" value="Add new ')
                __M_writer(unicode(input.title))
                __M_writer(u'"></div>\n      </div>\n')
                # SOURCE LINE 30
            elif input.type == "conditional":
                # SOURCE LINE 31
                if input.is_job_resource_conditional:
                    # SOURCE LINE 32
                    __M_writer(u'        ')
                    continue 
                    
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 34
                __M_writer(u'      ')
                group_values = values[input.name] 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 35
                current_case = group_values['__current_case__'] 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 36
                group_prefix = prefix + input.name + "|" 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 37
                group_errors = errors.get( input.name, {} ) 
                
                __M_writer(u'\n      ')
                # SOURCE LINE 38
                __M_writer(unicode(row_for_param( input.test_param, group_values[ input.test_param.name ], group_errors, group_prefix, ctx, allow_runtime=False )))
                __M_writer(u'\n      ')
                # SOURCE LINE 39
                __M_writer(unicode(do_inputs( input.cases[ current_case ].inputs, group_values, group_errors, group_prefix, ctx )))
                __M_writer(u'\n')
                # SOURCE LINE 40
            else:
                # SOURCE LINE 41
                if input.name in values:
                    # SOURCE LINE 42
                    __M_writer(u'        ')
                    __M_writer(unicode(row_for_param( input, values[ input.name ], errors, prefix, ctx )))
                    __M_writer(u'\n')
                    # SOURCE LINE 43
                else:
                    # SOURCE LINE 44
                    __M_writer(u'        ')
                    errors[ input.name ] = 'Value not stored, displaying default' 
                    
                    __M_writer(u'\n        ')
                    # SOURCE LINE 45
                    __M_writer(unicode(row_for_param( input, input.get_initial_value( trans, values ), errors, prefix, ctx )))
                    __M_writer(u'\n')
                    pass
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_row_for_param(context,param,value,error_dict,prefix,ctx,allow_runtime=True):
    context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        DataToolParameter = context.get('DataToolParameter', UNDEFINED)
        h = context.get('h', UNDEFINED)
        RuntimeValue = context.get('RuntimeValue', UNDEFINED)
        DataCollectionToolParameter = context.get('DataCollectionToolParameter', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        type = context.get('type', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 51
        __M_writer(u'\n')
        # SOURCE LINE 52
        if error_dict.has_key( param.name ):
            # SOURCE LINE 53
            __M_writer(u'        ')
            cls = "form-row form-row-error" 
            
            __M_writer(u'\n')
            # SOURCE LINE 54
        else:
            # SOURCE LINE 55
            __M_writer(u'        ')
            cls = "form-row" 
            
            __M_writer(u'\n')
            pass
        # SOURCE LINE 57
        __M_writer(u'    <div class="')
        __M_writer(unicode(cls))
        __M_writer(u'" id="row-')
        __M_writer(unicode(prefix))
        __M_writer(unicode(param.name))
        __M_writer(u'">\n')
        # SOURCE LINE 60
        if type( param ) is DataToolParameter:
            # SOURCE LINE 61
            __M_writer(u'            <label>\n                ')
            # SOURCE LINE 62
            __M_writer(unicode(param.get_label()))
            __M_writer(u"\n            </label>\n            <div>\n                Data input '")
            # SOURCE LINE 65
            __M_writer(unicode(param.name))
            __M_writer(u"' (")
            __M_writer(unicode(" or ".join( param.extensions )))
            __M_writer(u')\n            </div>\n')
            # SOURCE LINE 67
        elif type( param ) is DataCollectionToolParameter:
            # SOURCE LINE 68
            __M_writer(u'            <label>\n                ')
            # SOURCE LINE 69
            __M_writer(unicode(param.get_label()))
            __M_writer(u"\n            </label>\n            <div>\n                Data collection input '")
            # SOURCE LINE 72
            __M_writer(unicode(param.name))
            __M_writer(u"'\n            </div>\n")
            # SOURCE LINE 74
        else:
            # SOURCE LINE 75
            if isinstance( value, RuntimeValue ):    
                # SOURCE LINE 76
                __M_writer(u'                <label>\n                    ')
                # SOURCE LINE 77
                __M_writer(unicode(param.get_label()))
                __M_writer(u':\n                    <span class="popupmenu">\n                        <button type="submit" name="make_buildtime" value="')
                # SOURCE LINE 79
                __M_writer(unicode(prefix))
                __M_writer(unicode(param.name))
                __M_writer(u'">Set in advance</button>\n                    </span>\n                </label>\n                <div>\n                    <i>To be set at runtime</i>\n                </div>\n')
                # SOURCE LINE 85
            else:
                # SOURCE LINE 86
                __M_writer(u'                <label>\n                    ')
                # SOURCE LINE 87
                __M_writer(unicode(param.get_label()))
                __M_writer(u':\n')
                # SOURCE LINE 88
                if allow_runtime:
                    # SOURCE LINE 89
                    __M_writer(u'                        <span class="popupmenu">\n                            <button type="submit" name="make_runtime" value="')
                    # SOURCE LINE 90
                    __M_writer(unicode(prefix))
                    __M_writer(unicode(param.name))
                    __M_writer(u'">Set at runtime</button>\n                        </span>\n')
                    pass
                # SOURCE LINE 93
                __M_writer(u'                </label>\n                <div>\n                    ')
                # SOURCE LINE 95
                __M_writer(unicode(param.get_html_field( trans, value, ctx ).get_html( prefix )))
                __M_writer(u'          \n                </div>\n')
                pass
            # SOURCE LINE 98
            if error_dict.has_key( param.name ):
                # SOURCE LINE 99
                __M_writer(u'            <div style="color: red; font-weight: bold; padding-top: 1px; padding-bottom: 3px;">\n                <div style="width: 300px;"><img style="vertical-align: middle;" src="')
                # SOURCE LINE 100
                __M_writer(unicode(h.url_for('/static/style/error_small.png')))
                __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
                __M_writer(unicode(error_dict[param.name]))
                __M_writer(u'</span></div>\n            </div>\n')
                pass
            pass
        # SOURCE LINE 104
        __M_writer(u'        <div style="clear: both"></div>       \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


