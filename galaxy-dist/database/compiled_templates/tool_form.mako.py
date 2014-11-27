# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417014254.606529
_template_filename='templates/webapps/galaxy/tool_form.mako'
_template_uri='tool_form.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['help_for_param', 'errors_for_param', 'input_for_param', 'label_for_param', 'row_for_param', 'do_inputs', 'stylesheets', 'row_for_rerun', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x2302d290', context._clean_inheritance_tokens(), templateuri=u'/base_panels.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2302d290')] = ns

    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x2302d150', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x2302d150')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        add_frame = _import_ns.get('add_frame', context.get('add_frame', UNDEFINED))
        errors = _import_ns.get('errors', context.get('errors', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        unicode = _import_ns.get('unicode', context.get('unicode', UNDEFINED))
        overlay = _import_ns.get('overlay', context.get('overlay', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        def do_inputs(inputs,tool_state,errors,prefix,other_values=None):
            return render_do_inputs(context.locals_(__M_locals),inputs,tool_state,errors,prefix,other_values)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        tool_id_version_message = _import_ns.get('tool_id_version_message', context.get('tool_id_version_message', UNDEFINED))
        def row_for_rerun():
            return render_row_for_rerun(context.locals_(__M_locals))
        type = _import_ns.get('type', context.get('type', UNDEFINED))
        tool_state = _import_ns.get('tool_state', context.get('tool_state', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        AttributeError = _import_ns.get('AttributeError', context.get('AttributeError', UNDEFINED))
        tool = _import_ns.get('tool', context.get('tool', UNDEFINED))
        tool_version_select_field = _import_ns.get('tool_version_select_field', context.get('tool_version_select_field', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        import galaxy.util 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['galaxy'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        __M_writer(u'\n\n')
        # SOURCE LINE 110
        __M_writer(u'\n\n')
        # SOURCE LINE 203
        __M_writer(u'\n\n')
        # SOURCE LINE 231
        __M_writer(u'\n\n')
        # SOURCE LINE 235
        __M_writer(u'\n\n')
        # SOURCE LINE 242
        __M_writer(u'\n\n')
        # SOURCE LINE 250
        __M_writer(u'\n\n')
        # SOURCE LINE 258
        __M_writer(u'\n\n')
        # SOURCE LINE 270
        __M_writer(u'\n\n')
        # SOURCE LINE 272
        overlay(visible=False) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        # SOURCE LINE 274
        if add_frame.from_noframe:
            # SOURCE LINE 275
            __M_writer(u'    <div class="warningmessage">\n        <strong>Welcome to Galaxy</strong>\n        <hr/>\n        It appears that you found this tool from a link outside of Galaxy.\n        If you\'re not familiar with Galaxy, please consider visiting the\n        <a href="')
            # SOURCE LINE 280
            __M_writer(unicode(h.url_for( controller='root' )))
            __M_writer(u'" target="_top">welcome page</a>.\n        To learn more about what Galaxy is and what it can do for you, please visit\n        the <a href="')
            # SOURCE LINE 282
            __M_writer(unicode(add_frame.wiki_url))
            __M_writer(u'" target="_top">Galaxy wiki</a>.\n    </div>\n    <br/>\n')
            pass
        # SOURCE LINE 286
        __M_writer(u'\n')
        # SOURCE LINE 287

    # Render an error message if a dynamically generated select list is missing a required
    # index file or entry in the tool_data_table_conf.xml file.
        message = ""
        params_with_missing_data_table_entry = tool.params_with_missing_data_table_entry
        params_with_missing_index_file = tool.params_with_missing_index_file
        if params_with_missing_data_table_entry:
            param = params_with_missing_data_table_entry[0]
            message += "Data table named '%s' is required by tool but not configured.  " % param.options.missing_tool_data_table_name
        if tool.params_with_missing_index_file:
            param = params_with_missing_index_file[0]
            message += "Index file named '%s' is required by tool but not available.  " % param.options.missing_index_file
        
        # Handle calculating the redirect url for the special case where we have nginx proxy
        # upload and need to do url_for on the redirect portion of the tool action.
        try:
            tool_url = h.url_for(tool.action)
        except AttributeError:
            assert len(tool.action) == 2
            tool_url = tool.action[0] + h.url_for(tool.action[1])
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool_url','message','params_with_missing_data_table_entry','params_with_missing_index_file','param'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 307
        __M_writer(u'\n\n')
        # SOURCE LINE 309

    # Name of the tool in lower case
        low_tool_name = tool.name.lower()
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['low_tool_name'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 312
        __M_writer(u'\n\n')
        # SOURCE LINE 314
        if tool_id_version_message:
            # SOURCE LINE 315
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( tool_id_version_message, 'warning' )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 317
        __M_writer(u'\n<div class="toolForm" id="')
        # SOURCE LINE 318
        __M_writer(unicode(tool.id))
        __M_writer(u'">\n    <form id="tool_form" name="tool_form" action="')
        # SOURCE LINE 319
        __M_writer(unicode(tool_url))
        __M_writer(u'" enctype="')
        __M_writer(unicode(tool.enctype))
        __M_writer(u'" target="')
        __M_writer(unicode(tool.target))
        __M_writer(u'" method="')
        __M_writer(unicode(tool.method))
        __M_writer(u'">\n')
        # SOURCE LINE 320
        if tool.has_multiple_pages:
            # SOURCE LINE 321
            __M_writer(u'            <div class="toolFormTitle">')
            __M_writer(unicode(tool.name))
            __M_writer(u' (step ')
            __M_writer(unicode(tool_state.page+1))
            __M_writer(u' of ')
            __M_writer(unicode(tool.npages))
            __M_writer(u')\n')
            # SOURCE LINE 322
        elif not tool_version_select_field:
            # SOURCE LINE 323
            __M_writer(u'            <div class="toolFormTitle">')
            __M_writer(unicode(tool.name))
            __M_writer(u' (version ')
            __M_writer(unicode(tool.version))
            __M_writer(u')\n')
            # SOURCE LINE 324
        else:
            # SOURCE LINE 325
            __M_writer(u'            <div class="toolFormTitle">')
            __M_writer(unicode(tool.name))
            __M_writer(u' ')
            __M_writer(unicode(tool_version_select_field.get_html()))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 327
        __M_writer(u'\n        <span class="pull-right">\n')
        # SOURCE LINE 329
        if trans.app.config.biostar_url:
            # SOURCE LINE 331
            __M_writer(u'                Help from Biostar\n                <div class="icon-btn-group">\n                    <a href="')
            # SOURCE LINE 333
            __M_writer(unicode(h.url_for( controller='biostar', action='biostar_tool_tag_redirect', tool_id=tool.id )))
            __M_writer(u'"\n                        target="_blank" class="icon-btn" title="Search for this tool" data-toggle="tooltip" data-placement="bottom"><span class="fa fa-search"></span></a>\n                    <a href="')
            # SOURCE LINE 335
            __M_writer(unicode(h.url_for( controller='biostar', action='biostar_tool_question_redirect', tool_id=tool.id )))
            __M_writer(u'"\n                        target="_blank" class="icon-btn" title="Ask a question about this tool" data-toggle="tooltip" data-placement="bottom"><span class="fa fa-question-circle"></a>\n                </div>\n')
            pass
        # SOURCE LINE 339
        __M_writer(u'            <div class="icon-btn-group">\n                <a href="#" data-link="')
        # SOURCE LINE 340
        __M_writer(unicode(h.url_for( controller='root', action='index', tool_id=tool.id )))
        __M_writer(u'"\n                    class="icon-btn tool-share-link" title="Share this tool" data-toggle="tooltip" data-placement="bottom"><span class="fa fa-share"></span></a>\n            </div>\n        </span>\n        </div>\n        <div class="toolFormBody">\n            <input type="hidden" name="refresh" value="refresh">\n            <input type="hidden" name="tool_id" value="')
        # SOURCE LINE 347
        __M_writer(unicode(tool.id))
        __M_writer(u'">\n            <input type="hidden" name="tool_state" value="')
        # SOURCE LINE 348
        __M_writer(unicode(util.object_to_string( tool_state.encode( tool, app ) )))
        __M_writer(u'">\n')
        # SOURCE LINE 349
        if tool.display_by_page[tool_state.page]:
            # SOURCE LINE 350
            __M_writer(u'                ')
            __M_writer(unicode(trans.fill_template_string( tool.display_by_page[tool_state.page], context=tool.get_param_html_map( trans, tool_state.page, tool_state.inputs ) )))
            __M_writer(u'\n                ')
            # SOURCE LINE 351
            __M_writer(unicode(row_for_rerun()))
            __M_writer(u'\n                <input type="submit" class="btn btn-primary" name="runtool_btn" value="Execute">\n')
            # SOURCE LINE 353
        else:
            # SOURCE LINE 354
            __M_writer(u'                ')
            __M_writer(unicode(do_inputs( tool.inputs_by_page[ tool_state.page ], tool_state.inputs, errors, "" )))
            __M_writer(u'\n')
            # SOURCE LINE 355
            if tool_state.page == tool.last_page:
                # SOURCE LINE 356
                __M_writer(u'                    ')
                __M_writer(unicode(row_for_rerun()))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 358
            __M_writer(u'                <div class="form-row form-actions">\n')
            # SOURCE LINE 359
            if tool_state.page == tool.last_page:
                # SOURCE LINE 360
                __M_writer(u'                        <input type="submit" class="btn btn-primary" name="runtool_btn" value="Execute">\n')
                # SOURCE LINE 361
            else:
                # SOURCE LINE 362
                __M_writer(u'                        <input type="submit" class="btn btn-primary" name="runtool_btn" value="Next step">\n')
                pass
            # SOURCE LINE 364
            __M_writer(u'                </div>\n')
            pass
        # SOURCE LINE 366
        __M_writer(u'        </div>\n    </form>\n</div>\n')
        # SOURCE LINE 369
        if tool.help:
            # SOURCE LINE 370
            __M_writer(u'    <div class="toolHelp">\n        <div class="toolHelpBody">\n            ')
            # SOURCE LINE 372

            if tool.has_multiple_pages:
                tool_help = tool.help_by_page[tool_state.page]
            else:
                tool_help = tool.help
            
            # Help is Mako template, so render using current static path.
            tool_help = tool_help.render( static_path=h.url_for( '/static' ), host_url=h.url_for('/', qualified=True) )
            
            # Convert to unicode to display non-ascii characters.
            if type( tool_help ) is not unicode:
                tool_help = unicode( tool_help, 'utf-8')
                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool_help'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 384
            __M_writer(u'\n            ')
            # SOURCE LINE 385
            __M_writer(unicode(tool_help))
            __M_writer(u'\n        </div>\n    </div>\n')
            pass
        # SOURCE LINE 389
        if tool.tool_shed_repository:
            # SOURCE LINE 390
            __M_writer(u'    ')
            tool_url = tool.tool_shed_repository.get_sharable_url( tool.app ) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tool_url'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            # SOURCE LINE 391
            if tool_url:
                # SOURCE LINE 392
                __M_writer(u'        <br/>\n        ')
                # SOURCE LINE 393
                __M_writer(unicode( render_msg( 'This tool was installed from a ToolShed, you may be able to find additional information by following this link: <a href="%s" target="_blank">%s</a>' % ( tool_url, tool_url ), 'info' ) ))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 396
        if tool.citations:
            # SOURCE LINE 397
            __M_writer(u'    <script>\n    require(["mvc/citation/citation-model", "mvc/citation/citation-view"\n    ], function( citationModel, citationView ){\n        $(function() {\n            var citations = new citationModel.ToolCitationCollection();\n            citations.tool_id = "')
            # SOURCE LINE 402
            __M_writer(unicode(tool.id))
            __M_writer(u'";\n            var citation_list_view = new citationView.CitationListView({ collection: citations } );\n            citation_list_view.render();\n            citations.fetch();\n        } );\n    } );\n    </script>\n    <div id="citations">\n    </div>\n')
            pass
        # SOURCE LINE 412
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_help_for_param(context,param):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 252
        __M_writer(u'\n')
        # SOURCE LINE 253
        if param.help:
            # SOURCE LINE 254
            __M_writer(u'        <div class="toolParamHelp" style="clear: both;">\n            ')
            # SOURCE LINE 255
            __M_writer(unicode(param.help))
            __M_writer(u'\n        </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_errors_for_param(context,param,parent_errors):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 244
        __M_writer(u'\n')
        # SOURCE LINE 245
        if parent_errors.has_key( param.name ):
            # SOURCE LINE 246
            __M_writer(u'        <div class="form-row-error-message">\n            <div><img style="vertical-align: middle;" src="')
            # SOURCE LINE 247
            __M_writer(unicode(h.url_for('/static/style/error_small.png')))
            __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
            __M_writer(unicode(parent_errors[param.name]))
            __M_writer(u'</span></div>\n        </div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_input_for_param(context,param,field_html):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 233
        __M_writer(u'\n    <div class="form-row-input">')
        # SOURCE LINE 234
        __M_writer(unicode(field_html))
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_label_for_param(context,param):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        # SOURCE LINE 237
        __M_writer(u'\n    ')
        # SOURCE LINE 238
        label = param.get_label()
        
        __M_writer(u'\n')
        # SOURCE LINE 239
        if label:
            # SOURCE LINE 240
            __M_writer(u'        <label for="')
            __M_writer(unicode(param.name))
            __M_writer(u'">')
            __M_writer(unicode(label))
            __M_writer(u':</label>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_row_for_param(context,prefix,param,parent_state,parent_errors,other_values):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        def help_for_param(param):
            return render_help_for_param(context,param)
        def errors_for_param(param,parent_errors):
            return render_errors_for_param(context,param,parent_errors)
        def input_for_param(param,field_html):
            return render_input_for_param(context,param,field_html)
        def label_for_param(param):
            return render_label_for_param(context,param)
        unicode = _import_ns.get('unicode', context.get('unicode', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        type = _import_ns.get('type', context.get('type', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 205
        __M_writer(u'\n    ')
        # SOURCE LINE 206

        if parent_errors.has_key( param.name ):
            cls = "form-row form-row-error"
        else:
            cls = "form-row"
        
        field = param.get_html_field( trans, parent_state[ param.name ], other_values )
        field.refresh_on_change = param.refresh_on_change
        
        # Field may contain characters submitted by user and these characters may
        # be unicode; handle non-ascii characters gracefully.
        field_html = field.get_html( prefix )
        if type( field_html ) is not unicode:
            field_html = unicode( field_html, 'utf-8', 'replace' )
        
        if param.type == "hidden":
            return field_html
        
        
        # SOURCE LINE 223
        __M_writer(u'\n    <div class="')
        # SOURCE LINE 224
        __M_writer(unicode(cls))
        __M_writer(u'">\n        ')
        # SOURCE LINE 225
        __M_writer(unicode(label_for_param( param )))
        __M_writer(u'\n        ')
        # SOURCE LINE 226
        __M_writer(unicode(input_for_param( param, field_html )))
        __M_writer(u'\n        ')
        # SOURCE LINE 227
        __M_writer(unicode(errors_for_param( param, parent_errors )))
        __M_writer(u'\n        ')
        # SOURCE LINE 228
        __M_writer(unicode(help_for_param( param )))
        __M_writer(u'\n        <div style="clear: both;"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_do_inputs(context,inputs,tool_state,errors,prefix,other_values=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        def row_for_param(prefix,param,parent_state,parent_errors,other_values):
            return render_row_for_param(context,prefix,param,parent_state,parent_errors,other_values)
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        def do_inputs(inputs,tool_state,errors,prefix,other_values=None):
            return render_do_inputs(context,inputs,tool_state,errors,prefix,other_values)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        range = _import_ns.get('range', context.get('range', UNDEFINED))
        dict = _import_ns.get('dict', context.get('dict', UNDEFINED))
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 112
        __M_writer(u'\n    ')
        # SOURCE LINE 113

        from galaxy.util.expressions import ExpressionContext
        other_values = ExpressionContext( tool_state, other_values )
        
        
        # SOURCE LINE 116
        __M_writer(u'\n')
        # SOURCE LINE 117
        for input_index, input in enumerate( inputs.itervalues() ):
            # SOURCE LINE 118
            if not input.visible:
                # SOURCE LINE 119
                __M_writer(u'            ')
                pass 
                
                __M_writer(u'\n')
                # SOURCE LINE 120
            elif input.type == "repeat":
                # SOURCE LINE 121
                __M_writer(u'          <div class="repeat-group">\n              <div class="form-title-row"><strong>')
                # SOURCE LINE 122
                __M_writer(unicode(input.title_plural))
                __M_writer(u'</strong>\n')
                # SOURCE LINE 123
                if input.help:
                    # SOURCE LINE 124
                    __M_writer(u'                  <div class="toolParamHelp" style="clear: both;">\n                      ')
                    # SOURCE LINE 125
                    __M_writer(unicode(input.help))
                    __M_writer(u'\n                  </div>\n')
                    pass
                # SOURCE LINE 128
                __M_writer(u'              </div>\n              ')
                # SOURCE LINE 129

                repeat_state = tool_state[input.name]
                num_repeats = len( repeat_state )
                
                
                # SOURCE LINE 132
                __M_writer(u'\n')
                # SOURCE LINE 133
                for i in range( num_repeats ):
                    # SOURCE LINE 134
                    __M_writer(u'                <div class="repeat-group-item">\n                    ')
                    # SOURCE LINE 135

                    if input.name in errors:
                        rep_errors = errors[input.name][i]
                    else:
                        rep_errors = dict()
                    index = repeat_state[i]['__index__']
                    
                    
                    # SOURCE LINE 141
                    __M_writer(u'\n                    <div class="form-title-row"><strong>')
                    # SOURCE LINE 142
                    __M_writer(unicode(input.title))
                    __M_writer(u' ')
                    __M_writer(unicode(i + 1))
                    __M_writer(u'</strong></div>\n                    ')
                    # SOURCE LINE 143
                    __M_writer(unicode(do_inputs( input.inputs, repeat_state[i], rep_errors, prefix + input.name + "_" + str(index) + "|", other_values )))
                    __M_writer(u'\n')
                    # SOURCE LINE 144
                    if input.min < num_repeats:
                        # SOURCE LINE 145
                        __M_writer(u'                        <div class="form-row"><input type="submit" class="btn" name="')
                        __M_writer(unicode(prefix))
                        __M_writer(unicode(input.name))
                        __M_writer(u'_')
                        __M_writer(unicode(index))
                        __M_writer(u'_remove" value="Remove ')
                        __M_writer(unicode(input.title))
                        __M_writer(u' ')
                        __M_writer(unicode(i+1))
                        __M_writer(u'"></div>\n')
                        pass
                    # SOURCE LINE 147
                    __M_writer(u'                </div>\n')
                    # SOURCE LINE 148
                    if rep_errors.has_key( '__index__' ):
                        # SOURCE LINE 149
                        __M_writer(u'                    <div><img style="vertical-align: middle;" src="')
                        __M_writer(unicode(h.url_for('/static/style/error_small.png')))
                        __M_writer(u'">&nbsp;<span style="vertical-align: middle;">')
                        __M_writer(unicode(rep_errors['__index__']))
                        __M_writer(u'</span></div>\n')
                        pass
                    pass
                # SOURCE LINE 152
                if input.max > num_repeats:
                    # SOURCE LINE 153
                    __M_writer(u'                  <div class="form-row"><input type="submit" class="btn" name="')
                    __M_writer(unicode(prefix))
                    __M_writer(unicode(input.name))
                    __M_writer(u'_add" value="Add new ')
                    __M_writer(unicode(input.title))
                    __M_writer(u'"></div>\n')
                    pass
                # SOURCE LINE 155
                __M_writer(u'          </div>\n')
                # SOURCE LINE 156
            elif input.type == "conditional":
                # SOURCE LINE 157
                __M_writer(u'            ')

                group_state = tool_state[input.name]
                group_errors = errors.get( input.name, {} )
                current_case = group_state['__current_case__']
                group_prefix = prefix + input.name + "|"
                
                
                # SOURCE LINE 162
                __M_writer(u'\n')
                # SOURCE LINE 163
                if input.value_ref_in_group:
                    # SOURCE LINE 164
                    __M_writer(u'                ')
                    __M_writer(unicode(row_for_param( group_prefix, input.test_param, group_state, group_errors, other_values )))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 166
                __M_writer(u'            ')
                __M_writer(unicode(do_inputs( input.cases[current_case].inputs, group_state, group_errors, group_prefix, other_values )))
                __M_writer(u'\n')
                # SOURCE LINE 167
            elif input.type == "upload_dataset":
                # SOURCE LINE 168
                if input.get_datatype( trans, other_values ).composite_type is None: #have non-composite upload appear as before
                    # SOURCE LINE 169
                    __M_writer(u'                ')

                    if input.name in errors:
                        rep_errors = errors[input.name][0]
                    else:
                        rep_errors = dict()
                    
                    
                    # SOURCE LINE 174
                    __M_writer(u'\n              ')
                    # SOURCE LINE 175
                    __M_writer(unicode(do_inputs( input.inputs, tool_state[input.name][0], rep_errors, prefix + input.name + "_" + str( 0 ) + "|", other_values )))
                    __M_writer(u'\n')
                    # SOURCE LINE 176
                else:
                    # SOURCE LINE 177
                    __M_writer(u'                <div class="repeat-group">\n                    <div class="form-title-row"><strong>')
                    # SOURCE LINE 178
                    __M_writer(unicode(input.group_title( other_values )))
                    __M_writer(u'</strong></div>\n                    ')
                    # SOURCE LINE 179

                    repeat_state = tool_state[input.name]
                    
                    
                    # SOURCE LINE 181
                    __M_writer(u'\n')
                    # SOURCE LINE 182
                    for i in range( len( repeat_state ) ):
                        # SOURCE LINE 183
                        __M_writer(u'                      <div class="repeat-group-item">\n                      ')
                        # SOURCE LINE 184

                        if input.name in errors:
                            rep_errors = errors[input.name][i]
                        else:
                            rep_errors = dict()
                        index = repeat_state[i]['__index__']
                        
                        
                        # SOURCE LINE 190
                        __M_writer(u'\n                      <div class="form-title-row"><strong>File Contents for ')
                        # SOURCE LINE 191
                        __M_writer(unicode(input.title_by_index( trans, i, other_values )))
                        __M_writer(u'</strong></div>\n                      ')
                        # SOURCE LINE 192
                        __M_writer(unicode(do_inputs( input.inputs, repeat_state[i], rep_errors, prefix + input.name + "_" + str(index) + "|", other_values )))
                        __M_writer(u'\n')
                        # SOURCE LINE 194
                        __M_writer(u'                      </div>\n')
                        pass
                    # SOURCE LINE 197
                    __M_writer(u'                </div>\n')
                    pass
                # SOURCE LINE 199
            else:
                # SOURCE LINE 200
                __M_writer(u'            ')
                __M_writer(unicode(row_for_param( prefix, input, tool_state, errors, other_values )))
                __M_writer(u'\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(h.css( "autocomplete_tagging", "base", "library" )))
        __M_writer(u'\n    <style type="text/css">\n        html, body {\n            background-color: #fff;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_row_for_rerun(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        tool_state = _import_ns.get('tool_state', context.get('tool_state', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 260
        __M_writer(u'\n')
        # SOURCE LINE 261
        if trans.app.config.track_jobs_in_database and tool_state.rerun_remap_job_id is not None:
            # SOURCE LINE 262
            __M_writer(u'        <div id="remap-row" class="form-row">\n            <input type="checkbox" name="rerun_remap_job_id" value="')
            # SOURCE LINE 263
            __M_writer(unicode(tool_state.rerun_remap_job_id))
            __M_writer(u'"> Resume dependencies from this job\n            <div class="toolParamHelp" style="clear: both;">\n                The previous run of this tool failed and other tools were waiting for it to finish successfully, use this option to resume those tools using the outputs of this tool run.\n            </div>\n        </div>\n        <div style="clear: both;"></div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x2302d290')._populate(_import_ns, [u'overlay'])
        _mako_get_namespace(context, '__anon_0x2302d150')._populate(_import_ns, [u'render_msg'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        add_frame = _import_ns.get('add_frame', context.get('add_frame', UNDEFINED))
        tool = _import_ns.get('tool', context.get('tool', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n    ')
        # SOURCE LINE 17
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(unicode(h.js( "galaxy.panels", "libs/jquery/jstorage" )))
        __M_writer(u'\n    ')
        # SOURCE LINE 19
        __M_writer(unicode(h.js( "libs/bibtex" )))
        __M_writer(u'\n    <script type="text/javascript">\n        require( [ "galaxy.tools" ] );\n        window.enhanced_galaxy_tools = true;\n    </script>\n    <script type="text/javascript">\n    $(function() {\n        $(window).bind("refresh_on_change", function() {\n            $(\':file\').each( function() {\n                var file = $(this);\n                var file_value = file.val();\n                if (file_value) {\n                    // disable file input, since we don\'t want to upload the file on refresh\n                    var file_name = $(this).attr("name");\n                    file.attr( { name: \'replaced_file_input_\' + file_name, disabled: true } );\n                    // create a new hidden field which stores the filename and has the original name of the file input\n                    var new_file_input = $(document.createElement(\'input\'));\n                    new_file_input.attr( { "type": "hidden", "value": file_value, "name": file_name } );\n                    file.after(new_file_input);\n                }\n            });\n        });\n\n        // For drilldown parameters: add expand/collapse buttons and collapse initially-collapsed elements\n        $( \'div.drilldown-container\' ).each( function() {\n            $(this).find(\'span.form-toggle\' ).each( function() {\n                var show_hide_click_elt = $(this);\n                var group_id = show_hide_click_elt.attr(\'id\').substring( 0, show_hide_click_elt.attr(\'id\').lastIndexOf( \'-click\' ) );\n                $(\'#\' + group_id + \'-container\').each( function() {\n                    var show_hide_elt = $(this);\n                    if (  show_hide_click_elt.hasClass( \'toggle-expand\' ) ) {\n                        show_hide_elt.hide();\n                    }\n                    show_hide_click_elt.click( function() {\n                        if ( show_hide_click_elt.hasClass("toggle") ){\n                            show_hide_click_elt.addClass("toggle-expand");\n                            show_hide_click_elt.removeClass("toggle");\n                            show_hide_elt.slideUp( \'fast\' );\n                        }\n                        else {\n                            show_hide_click_elt.addClass("toggle");\n                            show_hide_click_elt.removeClass("toggle-expand");\n                            show_hide_elt.slideDown( \'fast\' );\n                        }\n                    });\n                });\n            });\n        });\n\n        $(".add-librarydataset").click(function() {\n            var link = $(this);\n            $.ajax({\n                url: "/visualization/list_libraries",\n                error: function(xhr, ajaxOptions, thrownError) { alert( "Grid failed" ); console.log(xhr, ajaxOptions, thrownError); },\n                success: function(table_html) {\n                    show_modal(\n                        "Select Library Dataset",\n                        table_html, {\n                            "Cancel": function() {\n                                hide_modal();\n                            },\n                            "Select": function() {\n                                var names = [];\n                                var ids = [];\n                                counter = 1;\n                                $(\'input[name=ldda_ids]:checked\').each(function() {\n                                    var name = $.trim( $(this).siblings("label").text() );\n                                    var id = $(this).val();\n                                    names.push( counter + ". " + name );\n                                    counter += 1;\n                                    ids.push(id);\n                                });\n                                link.html( names.join("<br/>") );\n                                link.siblings("input[type=hidden]").val( ids.join("||") );\n                                hide_modal();\n                            }\n                        }\n                    );\n                }\n            });\n        });\n    });\n\n')
        # SOURCE LINE 102
        if not add_frame.debug:
            # SOURCE LINE 103
            __M_writer(u'        if( window.name != "galaxy_main" ) {\n            location.replace( \'')
            # SOURCE LINE 104
            __M_writer(unicode(h.url_for( controller='root', action='index', tool_id=tool.id )))
            __M_writer(u"' );\n        }\n")
            pass
        # SOURCE LINE 107
        __M_writer(u'\n    </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


