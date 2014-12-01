# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417441812.709017
_template_filename='templates/webapps/galaxy/workflow/editor.mako'
_template_uri='workflow/editor.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['left_panel', 'overlay', 'render_label', 'center_panel', 'right_panel', 'stylesheets', 'init', 'javascripts', 'render_tool']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 403
    ns = runtime.TemplateNamespace('__anon_0x7f5a30573590', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f5a30573590')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n\n')
        # SOURCE LINE 222
        __M_writer(u'\n\n')
        # SOURCE LINE 257
        __M_writer(u'\n\n')
        # SOURCE LINE 264
        __M_writer(u'\n\n')
        # SOURCE LINE 269
        __M_writer(u'\n\n')
        # SOURCE LINE 352
        __M_writer(u'\n\n')
        # SOURCE LINE 384
        __M_writer(u'\n\n')
        # SOURCE LINE 447
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        def render_label(label):
            return render_render_label(context,label)
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        def render_tool(tool,section):
            return render_render_tool(context,tool,section)
        __M_writer = context.writer()
        # SOURCE LINE 271
        __M_writer(u'\n    ')
        # SOURCE LINE 272
        from galaxy.tools import Tool, ToolSection, ToolSectionLabel 
        
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>\n            ')
        # SOURCE LINE 276
        __M_writer(unicode(n_('Tools')))
        __M_writer(u'\n        </div>\n    </div>\n\n    <div class="unified-panel-body" style="overflow: auto;">\n            <div class="toolMenu">\n            <div id="tool-search" style="padding-bottom: 5px; position: relative; display: block; width: 100%">\n                <input type="text" name="query" placeholder="search tools" id="tool-search-query" class="search-query parent-width" />\n                <img src="')
        # SOURCE LINE 284
        __M_writer(unicode(h.url_for('/static/images/loading_small_white_bg.gif')))
        __M_writer(u'" id="search-spinner" class="search-spinner" />\n            </div>\n            <div class="toolSectionList">\n')
        # SOURCE LINE 287
        for key, val in app.toolbox.tool_panel.items():
            # SOURCE LINE 288
            __M_writer(u'                    <div class="toolSectionWrapper">\n')
            # SOURCE LINE 289
            if isinstance( val, Tool ):
                # SOURCE LINE 290
                __M_writer(u'                        ')
                __M_writer(unicode(render_tool( val, False )))
                __M_writer(u'\n')
                # SOURCE LINE 291
            elif isinstance( val, ToolSection ) and val.elems:
                # SOURCE LINE 292
                __M_writer(u'                    ')
                section = val 
                
                __M_writer(u'\n                        <div class="toolSectionTitle" id="title_')
                # SOURCE LINE 293
                __M_writer(unicode(section.id))
                __M_writer(u'">\n                            <span>')
                # SOURCE LINE 294
                __M_writer(unicode(section.name))
                __M_writer(u'</span>\n                        </div>\n                        <div id="')
                # SOURCE LINE 296
                __M_writer(unicode(section.id))
                __M_writer(u'" class="toolSectionBody">\n                            <div class="toolSectionBg">\n')
                # SOURCE LINE 298
                for section_key, section_val in section.elems.items():
                    # SOURCE LINE 299
                    if isinstance( section_val, Tool ):
                        # SOURCE LINE 300
                        __M_writer(u'                                        ')
                        __M_writer(unicode(render_tool( section_val, True )))
                        __M_writer(u'\n')
                        # SOURCE LINE 301
                    elif isinstance( section_val, ToolSectionLabel ):
                        # SOURCE LINE 302
                        __M_writer(u'                                        ')
                        __M_writer(unicode(render_label( section_val )))
                        __M_writer(u'\n')
                        pass
                    pass
                # SOURCE LINE 305
                __M_writer(u'                            </div>\n                        </div>\n')
                # SOURCE LINE 307
            elif isinstance( val, ToolSectionLabel ):
                # SOURCE LINE 308
                __M_writer(u'                        ')
                __M_writer(unicode(render_label( val )))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 310
            __M_writer(u'                    </div>\n')
            pass
        # SOURCE LINE 313
        if trans.user_is_admin() and trans.app.data_managers.data_managers:
            # SOURCE LINE 314
            __M_writer(u'                   <div>&nbsp;</div>\n                   <div class="toolSectionWrapper">\n                       <div class="toolSectionTitle" id="title___DATA_MANAGER_TOOLS__">\n                           <span>Data Manager Tools</span>\n                       </div>\n                       <div id="__DATA_MANAGER_TOOLS__" class="toolSectionBody">\n                           <div class="toolSectionBg">\n')
            # SOURCE LINE 321
            for data_manager_id, data_manager_val in trans.app.data_managers.data_managers.items():
                # SOURCE LINE 322
                __M_writer(u'                                   ')
                __M_writer(unicode( render_tool( data_manager_val.tool, True ) ))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 324
            __M_writer(u'                           </div>\n                       </div>\n                   </div>\n')
            pass
        # SOURCE LINE 329
        __M_writer(u'            </div>\n')
        # SOURCE LINE 331
        __M_writer(u'            <div id="search-no-results" style="display: none; padding-top: 5px">\n                <em><strong>Search did not match any tools.</strong></em>\n            </div>\n            <div>&nbsp;</div>\n            <div class="toolMenuGroupHeader">Workflow control</div>\n            <div class="toolSectionTitle" id="title___workflow__input__">\n                <span>Inputs</span>\n            </div>\n            <div id="__workflow__input__" class="toolSectionBody">\n                <div class="toolSectionBg">\n                    <div class="toolTitle">\n                        <a href="#" onclick="add_node_for_module( \'data_input\', \'Input Dataset\' )">Input dataset</a>\n                    </div>\n                    <div class="toolTitle">\n                        <a href="#" onclick="add_node_for_module( \'data_collection_input\', \'Input Dataset Collection\' )">Input dataset collection</a>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context,visible=False):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 266
        __M_writer(u'\n    ')
        # SOURCE LINE 267
        __M_writer(unicode(parent.overlay( "Loading workflow editor...",
                      "<div class='progress progress-striped progress-info active'><div class='progress-bar' style='width: 100%;'></div></div>", self.overlay_visible )))
        # SOURCE LINE 268
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_label(context,label):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 260
        __M_writer(u'\n    <div class="toolPanelLabel" id="title_')
        # SOURCE LINE 261
        __M_writer(unicode(label.id))
        __M_writer(u'">\n        <span>')
        # SOURCE LINE 262
        __M_writer(unicode(label.text))
        __M_writer(u'</span>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 354
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner" style="float: right">\n            <a id="workflow-options-button" class="panel-header-button" href="#"><span class="fa fa-cog"></span></a>\n        </div>\n        <div class="unified-panel-header-inner">\n            Workflow Canvas | ')
        # SOURCE LINE 361
        __M_writer(filters.html_escape(unicode(h.to_unicode( stored.name ) )))
        __M_writer(u'\n        </div>\n    </div>\n    <div class="unified-panel-body">\n        <div id="canvas-viewport" style="width: 100%; height: 100%; position: absolute; overflow: hidden; background: #EEEEEE; background: white url(')
        # SOURCE LINE 365
        __M_writer(unicode(h.url_for('/static/images/light_gray_grid.gif')))
        __M_writer(u') repeat;">\n            <div id="canvas-container" style="position: absolute; width: 100%; height: 100%;"></div>\n        </div>\n        <div id="overview-border" style="position: absolute; width: 150px; height: 150px; right: 20000px; bottom: 0px; border-top: solid gray 1px; border-left: solid grey 1px; padding: 7px 0 0 7px; background: #EEEEEE no-repeat url(')
        # SOURCE LINE 368
        __M_writer(unicode(h.url_for('/static/images/resizable.png')))
        __M_writer(u'); z-index: 20000; overflow: hidden; max-width: 300px; max-height: 300px; min-width: 50px; min-height: 50px">\n            <div style="position: relative; overflow: hidden; width: 100%; height: 100%; border-top: solid gray 1px; border-left: solid grey 1px;">\n                <div id="overview" style="position: absolute;">\n                    <canvas width="0" height="0" style="background: white; width: 100%; height: 100%;" id="overview-canvas"></canvas>\n                    <div id="overview-viewport" style="position: absolute; width: 0px; height: 0px; border: solid blue 1px; z-index: 10;"></div>\n                </div>\n            </div>\n        </div>\n        <div id=\'workflow-parameters-box\' style="display:none; position: absolute; /*width: 150px; height: 150px;*/ right: 0px; top: 0px; border-bottom: solid gray 1px; border-left: solid grey 1px; padding: 7px; background: #EEEEEE; z-index: 20000; overflow: hidden; max-width: 300px; max-height: 300px; /*min-width: 50px; min-height: 50px*/">\n            <div style="margin-bottom:5px;"><b>Workflow Parameters</b></div>\n            <div id="workflow-parameters-container">\n            </div>\n        </div>\n        <div id="close-viewport" style="border-left: 1px solid #999; border-top: 1px solid #999; background: #ddd url(')
        # SOURCE LINE 381
        __M_writer(unicode(h.url_for('/static/images/overview_arrows.png')))
        __M_writer(u') 12px 0px; position: absolute; right: 0px; bottom: 0px; width: 12px; height: 12px; z-index: 25000;"></div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        annotation = _import_ns.get('annotation', context.get('annotation', UNDEFINED))
        render_individual_tagging_element = _import_ns.get('render_individual_tagging_element', context.get('render_individual_tagging_element', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 386
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            Details\n        </div>\n    </div>\n    <div class="unified-panel-body" style="overflow: auto;">\n')
        # SOURCE LINE 394
        __M_writer(u'        <div id="edit-attributes" class="metadataForm right-content">\n            <div class="metadataFormTitle">Edit Workflow Attributes</div>\n            <div class="metadataFormBody">\n')
        # SOURCE LINE 398
        __M_writer(u'            <div id="workflow-name-area" class="form-row">\n                <label>Name:</label>\n                <span id="workflow-name" class="editable-text" title="Click to rename workflow">')
        # SOURCE LINE 400
        __M_writer(filters.html_escape(unicode(h.to_unicode( stored.name ) )))
        __M_writer(u'</span>\n            </div>\n')
        # SOURCE LINE 403
        __M_writer(u'            ')
        __M_writer(u'\n            <div class="form-row">\n                <label>\n                    Tags:\n                </label>\n                    <div style="float: left; width: 225px; margin-right: 10px; border-style: inset; border-width: 1px; margin-left: 2px">\n                        <style>\n                            .tag-area {\n                                border: none;\n                            }\n                        </style>\n                        ')
        # SOURCE LINE 414
        __M_writer(unicode(render_individual_tagging_element(user=trans.get_user(), tagged_item=stored, elt_context="edit_attributes.mako", use_toggle_link=False, input_size="20")))
        __M_writer(u'\n                    </div>\n                    <div class="toolParamHelp">Apply tags to make it easy to search for and find items with the same tag.</div>\n                </div>\n')
        # SOURCE LINE 420
        __M_writer(u'                <div id="workflow-annotation-area" class="form-row">\n                    <label>Annotation / Notes:</label>\n                    <div id="workflow-annotation" class="editable-text" title="Click to edit annotation">\n')
        # SOURCE LINE 423
        if annotation:
            # SOURCE LINE 424
            __M_writer(u'                        ')
            __M_writer(filters.html_escape(unicode(h.to_unicode( annotation ) )))
            __M_writer(u'\n')
            # SOURCE LINE 425
        else:
            # SOURCE LINE 426
            __M_writer(u'                        <em>Describe or add notes to workflow</em>\n')
            pass
        # SOURCE LINE 428
        __M_writer(u'                    </div>\n                    <div class="toolParamHelp">Add an annotation or notes to a workflow; annotations are available when a workflow is viewed.</div>\n                </div>\n            </div>\n        </div>\n\n')
        # SOURCE LINE 435
        __M_writer(u'        <div id="right-content" class="right-content"></div>\n\n')
        # SOURCE LINE 438
        __M_writer(u'        <div style="display:none;" id="workflow-output-area" class="metadataForm right-content">\n            <div class="metadataFormTitle">Edit Workflow Outputs</div>\n            <div class="metadataFormBody"><div class="form-row">\n                <div class="toolParamHelp">Tag step outputs to indicate the final dataset(s) to be generated by running this workflow.</div>\n                <div id="output-fill-area"></div>\n            </div></div>\n        </div>\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 72
        __M_writer(u'    ')
        __M_writer(unicode(h.css( "base", "autocomplete_tagging", "tool_menu" )))
        __M_writer(u'\n\n')
        # SOURCE LINE 75
        __M_writer(u'    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n\n    <style type="text/css">\n    body { margin: 0; padding: 0; overflow: hidden; }\n\n    #left {\n        background: #C1C9E5 url(')
        # SOURCE LINE 81
        __M_writer(unicode(h.url_for('/static/style/menu_bg.png')))
        __M_writer(u') top repeat-x;\n    }\n\n    div.toolMenu {\n        margin: 5px;\n        margin-left: 10px;\n        margin-right: 10px;\n    }\n    div.toolMenuGroupHeader {\n        font-weight: bold;\n        padding-top: 0.5em;\n        padding-bottom: 0.5em;\n        color: #333;\n        font-style: italic;\n        border-bottom: dotted #333 1px;\n        margin-bottom: 0.5em;\n    }\n    div.toolTitleDisabled {\n        padding-top: 5px;\n        padding-bottom: 5px;\n        margin-left: 16px;\n        margin-right: 10px;\n        display: list-item;\n        list-style: square outside;\n        font-style: italic;\n        color: gray;\n    }\n    div.toolTitleNoSectionDisabled {\n      padding-bottom: 0px;\n      font-style: italic;\n      color: gray;\n    }\n    div.toolFormRow {\n        position: relative;\n    }\n\n    .right-content {\n        margin: 5px;\n    }\n\n    canvas { position: absolute; z-index: 10; }\n    canvas.dragging { position: absolute; z-index: 1000; }\n    .input-terminal { width: 12px; height: 12px; background: url(')
        # SOURCE LINE 123
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_open.png')))
        __M_writer(u'); position: absolute; top: 50%; margin-top: -6px; left: -6px; z-index: 1500; }\n    .output-terminal { width: 12px; height: 12px; background: url(')
        # SOURCE LINE 124
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_open.png')))
        __M_writer(u'); position: absolute; top: 50%; margin-top: -6px; right: -6px; z-index: 1500; }\n    .drag-terminal { width: 12px; height: 12px; background: url(')
        # SOURCE LINE 125
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_drag.png')))
        __M_writer(u'); position: absolute; z-index: 1500; }\n    .input-terminal-active { background: url(')
        # SOURCE LINE 126
        __M_writer(unicode(h.url_for('/static/style/workflow_circle_green.png')))
        __M_writer(u'); }\n')
        # SOURCE LINE 128
        __M_writer(u'    .unselectable { -moz-user-select: none; -khtml-user-select: none; user-select: none; }\n    img { border: 0; }\n\n    div.buttons img {\n    width: 16px; height: 16px;\n    cursor: pointer;\n    }\n\n')
        # SOURCE LINE 138
        __M_writer(u'    div.toolFormInCanvas {\n        z-index: 100;\n        position: absolute;\n')
        # SOURCE LINE 142
        __M_writer(u'        margin: 6px;\n    }\n\n    div.toolForm-active {\n        z-index: 1001;\n        border: solid #8080FF 4px;\n        margin: 3px;\n    }\n\n    div.toolFormTitle {\n        cursor: move;\n        min-height: 16px;\n    }\n\n    div.titleRow {\n        font-weight: bold;\n        border-bottom: dotted gray 1px;\n        margin-bottom: 0.5em;\n        padding-bottom: 0.25em;\n    }\n    div.form-row {\n      position: relative;\n    }\n\n    div.tool-node-error div.toolFormTitle {\n        background: #FFCCCC;\n        border-color: #AA6666;\n    }\n    div.tool-node-error {\n        border-color: #AA6666;\n    }\n\n    #canvas-area {\n        position: absolute;\n        top: 0; left: 305px; bottom: 0; right: 0;\n        border: solid red 1px;\n        overflow: none;\n    }\n\n    .form-row {\n    }\n\n    div.toolFormInCanvas div.toolFormBody {\n        padding: 0;\n    }\n    .form-row-clear {\n        clear: both;\n    }\n\n    div.rule {\n        height: 0;\n        border: none;\n        border-bottom: dotted black 1px;\n        margin: 0 5px;\n    }\n\n    .callout {\n        position: absolute;\n        z-index: 10000;\n    }\n\n    .pjaForm {\n        margin-bottom:10px;\n    }\n\n    .pjaForm .toolFormBody{\n        padding:10px;\n    }\n\n    .pjaForm .toolParamHelp{\n        padding:5px;\n    }\n\n    .panel-header-button-group {\n        margin-right: 5px;\n        padding-right: 5px;\n        border-right: solid gray 1px;\n    }\n\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4

        self.active_view="workflow"
        self.overlay_visible=True
        
        
        # SOURCE LINE 7
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        stored = _import_ns.get('stored', context.get('stored', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n\n    ')
        # SOURCE LINE 12
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n    <!--[if lt IE 9]>\n      <script type=\'text/javascript\' src="')
        # SOURCE LINE 15
        __M_writer(unicode(h.url_for('/static/scripts/libs/IE/excanvas.js')))
        __M_writer(u'"></script>\n    <![endif]-->\n\n    ')
        # SOURCE LINE 18
        __M_writer(unicode(h.js( "libs/jquery/jquery.event.drag",
            "libs/jquery/jquery.event.drop",
            "libs/jquery/jquery.event.hover",
            "libs/jquery/jquery.form",
            "libs/jquery/jstorage",
            "galaxy.workflow_editor.canvas",
            "libs/jquery/jquery.autocomplete",
            "galaxy.autocom_tagging",
            "galaxy.workflows" )))
        # SOURCE LINE 26
        __M_writer(u'\n\n    <!--[if lt IE 7]>\n    <script type=\'text/javascript\'>\n    window.lt_ie_7 = true;\n    </script>\n    <![endif]-->\n\n    <script type=\'text/javascript\'>\n        // Globals\n        workflow = null;\n        canvas_manager = null;\n        active_ajax_call = false;\n\n        var workflow_id = "')
        # SOURCE LINE 40
        __M_writer(unicode(trans.security.encode_id( stored.id ) ))
        __M_writer(u'";\n\n        // URLs used by galaxy.workflows.js\n        var tool_search_url = "')
        # SOURCE LINE 43
        __M_writer(unicode(h.url_for( controller='root', action='tool_search' )))
        __M_writer(u'",\n            get_datatypes_url = "')
        # SOURCE LINE 44
        __M_writer(unicode(h.url_for( controller='workflow', action='get_datatypes' )))
        __M_writer(u'",\n            load_workflow_url = "')
        # SOURCE LINE 45
        __M_writer(unicode(h.url_for( controller='workflow', action='load_workflow' )))
        __M_writer(u'",\n            run_workflow_url = "')
        # SOURCE LINE 46
        __M_writer(unicode(h.url_for( controller='root', action='index', workflow_id=trans.security.encode_id(stored.id))))
        __M_writer(u'",\n            rename_async_url = "')
        # SOURCE LINE 47
        __M_writer(unicode(h.url_for( controller='workflow', action='rename_async', id=trans.security.encode_id(stored.id) )))
        __M_writer(u'",\n            annotate_async_url = "')
        # SOURCE LINE 48
        __M_writer(unicode(h.url_for( controller='workflow', action='annotate_async', id=trans.security.encode_id(stored.id) )))
        __M_writer(u'",\n            get_new_module_info_url = "')
        # SOURCE LINE 49
        __M_writer(unicode(h.url_for(controller='workflow', action='get_new_module_info' )))
        __M_writer(u'",\n            workflow_index_url = "')
        # SOURCE LINE 50
        __M_writer(unicode(h.url_for( controller='workflow', action='index' )))
        __M_writer(u'",\n            save_workflow_url = "')
        # SOURCE LINE 51
        __M_writer(unicode(h.url_for(controller='workflow', action='save_workflow' )))
        __M_writer(u'";\n\n    ')
        # SOURCE LINE 53

        from galaxy.jobs.actions.post import ActionBox
            
        
        # SOURCE LINE 55
        __M_writer(u'\n        // Post-job action vars.\n        var pja_list = "')
        # SOURCE LINE 57
        __M_writer(unicode(ActionBox.get_add_list()))
        __M_writer(u'",\n            get_pja_form = function(pja, node) {\n                var p_str = \'\';\n                // FIXME: this writes JS code; this logic should be codified in galaxy.workflows.js\n                ')
        # SOURCE LINE 61
        __M_writer(unicode(ActionBox.get_forms(trans)))
        __M_writer(u'\n                return p_str;\n            };\n\n        // NOTE: code to initialize and edit workflows is in galaxy.workflows.js\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool(context,tool,section):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30573590')._populate(_import_ns, [u'render_individual_tagging_element'])
        __M_writer = context.writer()
        # SOURCE LINE 225
        __M_writer(u'\n')
        # SOURCE LINE 226
        if not tool.hidden:
            # SOURCE LINE 227
            if tool.is_workflow_compatible:
                # SOURCE LINE 228
                if section:
                    # SOURCE LINE 229
                    __M_writer(u'                <div class="toolTitle">\n')
                    # SOURCE LINE 230
                else:
                    # SOURCE LINE 231
                    __M_writer(u'                <div class="toolTitleNoSection">\n')
                    pass
                # SOURCE LINE 233
                if "[[" in tool.description and "]]" in tool.description:
                    # SOURCE LINE 234
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description.replace( '[[', '<a id="link-${tool.id}" href="javascript:add_node_for_tool( ${tool.id} )">' % tool.id ).replace( "]]", "</a>" )))
                    __M_writer(u'\n')
                    # SOURCE LINE 235
                elif tool.name:
                    # SOURCE LINE 236
                    __M_writer(u'                    <a id="link-')
                    __M_writer(unicode(tool.id))
                    __M_writer(u'" href="#" onclick="add_node_for_tool( \'')
                    __M_writer(unicode(tool.id))
                    __M_writer(u"', '")
                    __M_writer(unicode(tool.name))
                    __M_writer(u'\' )">')
                    __M_writer(unicode(tool.name))
                    __M_writer(u'</a> ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                    # SOURCE LINE 237
                else:
                    # SOURCE LINE 238
                    __M_writer(u'                    <a id="link-')
                    __M_writer(unicode(tool.id))
                    __M_writer(u'" href="#" onclick="add_node_for_tool( \'')
                    __M_writer(unicode(tool.id))
                    __M_writer(u"', '")
                    __M_writer(unicode(tool.name))
                    __M_writer(u'\' )">')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'</a>\n')
                    pass
                # SOURCE LINE 240
                __M_writer(u'            </div>\n')
                # SOURCE LINE 241
            else:
                # SOURCE LINE 242
                if section:
                    # SOURCE LINE 243
                    __M_writer(u'                <div class="toolTitleDisabled">\n')
                    # SOURCE LINE 244
                else:
                    # SOURCE LINE 245
                    __M_writer(u'                <div class="toolTitleNoSectionDisabled">\n')
                    pass
                # SOURCE LINE 247
                if "[[" in tool.description and "]]" in tool.description:
                    # SOURCE LINE 248
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description.replace( '[[', '' % tool.id ).replace( "]]", "" )))
                    __M_writer(u'\n')
                    # SOURCE LINE 249
                elif tool.name:
                    # SOURCE LINE 250
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.name))
                    __M_writer(u' ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                    # SOURCE LINE 251
                else:
                    # SOURCE LINE 252
                    __M_writer(u'                    ')
                    __M_writer(unicode(tool.description))
                    __M_writer(u'\n')
                    pass
                # SOURCE LINE 254
                __M_writer(u'            </div>\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


