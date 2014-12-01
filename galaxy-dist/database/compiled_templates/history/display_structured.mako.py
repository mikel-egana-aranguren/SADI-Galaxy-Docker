# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417441658.005823
_template_filename='templates/webapps/galaxy/history/display_structured.mako'
_template_uri='history/display_structured.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['render_hda_copied_from_library', 'render_item_wf', 'render_item_hda', 'title', 'stylesheets', 'render_item', 'render_item_job', 'javascripts', 'render_hda_copied_from_history']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'show_params', context._clean_inheritance_tokens(), templateuri=u'/show_params.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'show_params')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        items = context.get('items', UNDEFINED)
        def render_item(entity,children):
            return render_render_item(context.locals_(__M_locals),entity,children)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 126
        __M_writer(u'\n\n')
        # SOURCE LINE 174
        __M_writer(u'\n\n')
        # SOURCE LINE 187
        __M_writer(u'\n\n')
        # SOURCE LINE 203
        __M_writer(u'\n\n')
        # SOURCE LINE 226
        __M_writer(u'\n\n')
        # SOURCE LINE 252
        __M_writer(u'\n\n')
        # SOURCE LINE 293
        __M_writer(u'\n\n')
        # SOURCE LINE 309
        __M_writer(u'\n\n')
        # SOURCE LINE 313
        for entity, children in items:
            # SOURCE LINE 314
            __M_writer(u'    ')
            __M_writer(unicode(render_item( entity, children )))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_hda_copied_from_library(context,hda,children):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 228
        __M_writer(u'\n')
        # SOURCE LINE 230
        __M_writer(u'    ')
        id = trans.security.encode_id( hda.id ) 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 231

        folder = hda.copied_from_library_dataset_dataset_association.library_dataset.folder
        folder_id = 'F' + trans.security.encode_id( folder.id )
            
        
        # SOURCE LINE 234
        __M_writer(u'\n    <div class="copied-from copied-from-library">\n        <div class="header">\n            <div class="copied-from-dataset">\n                <span class="light">')
        # SOURCE LINE 238
        __M_writer(unicode( _( 'Copied from library dataset' ) + ':' ))
        __M_writer(u'</span>\n                <span class="bold">')
        # SOURCE LINE 239
        __M_writer(unicode( hda.copied_from_library_dataset_dataset_association.name ))
        __M_writer(u'</span>\n            </div>\n            <div class="copied-from-source">\n                <span class="light">')
        # SOURCE LINE 242
        __M_writer(unicode( _( 'Library' ) + ':' ))
        __M_writer(u'</span>\n                <span class="bold">\n                    <a href="')
        # SOURCE LINE 244
        __M_writer(unicode( h.url_for( controller='library', action='list' ) + '#folders/F' + folder_id ))
        __M_writer(u'">\n                        ')
        # SOURCE LINE 245
        __M_writer(unicode( folder.name ))
        __M_writer(u'\n                    </a>\n                </span>\n            </div>\n        </div>\n        <div id="hda-')
        # SOURCE LINE 250
        __M_writer(unicode(id))
        __M_writer(u'" class="dataset hda state-')
        __M_writer(unicode(hda.state))
        __M_writer(u'"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_wf(context,wf,children):
    context.caller_stack._push_frame()
    try:
        def render_item(entity,children):
            return render_render_item(context,entity,children)
        reversed = context.get('reversed', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 296
        __M_writer(u'\n')
        # SOURCE LINE 298
        __M_writer(u'    <div class="workflow">\n        <div class="header">\n            <span class="bold">')
        # SOURCE LINE 300
        __M_writer(unicode(wf.workflow.name))
        __M_writer(u'</span>\n            <span class="light">- Workflow</span>\n        </div>\n        <div class="body">\n')
        # SOURCE LINE 304
        for e, c in reversed( children ):
            # SOURCE LINE 305
            __M_writer(u'            ')
            __M_writer(unicode(render_item( e, c )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 307
        __M_writer(u'        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_hda(context,hda,children):
    context.caller_stack._push_frame()
    try:
        def render_hda_copied_from_library(hda,children):
            return render_render_hda_copied_from_library(context,hda,children)
        trans = context.get('trans', UNDEFINED)
        def render_hda_copied_from_history(hda,children):
            return render_render_hda_copied_from_history(context,hda,children)
        __M_writer = context.writer()
        # SOURCE LINE 190
        __M_writer(u'\n')
        # SOURCE LINE 192
        __M_writer(u'\n')
        # SOURCE LINE 193
        if hda.copied_from_history_dataset_association:
            # SOURCE LINE 194
            __M_writer(u'    ')
            __M_writer(unicode( render_hda_copied_from_history( hda, children ) ))
            __M_writer(u'\n\n')
            # SOURCE LINE 196
        elif hda.copied_from_library_dataset_dataset_association:
            # SOURCE LINE 197
            __M_writer(u'    ')
            __M_writer(unicode( render_hda_copied_from_library( hda, children ) ))
            __M_writer(u'\n\n')
            # SOURCE LINE 199
        else:
            # SOURCE LINE 200
            __M_writer(u'    ')
            id = trans.security.encode_id( hda.id ) 
            
            __M_writer(u'\n    <div id="hda-')
            # SOURCE LINE 201
            __M_writer(unicode(id))
            __M_writer(u'" class="dataset hda state-')
            __M_writer(unicode(hda.state))
            __M_writer(u'"></div>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        history = context.get('history', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(unicode( history.name ))
        __M_writer(u' | ')
        __M_writer(unicode( _( 'Structure' ) ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 6
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    <style type="text/css">\n        body {\n            padding: 5px;\n        }\n        body > .workflow, body > .toolForm, body > .copied-from {\n            /*width           : 80%;*/\n            margin-bottom   : 8px;\n            /*margin-left     : auto;*/\n            /*margin-right    : auto;*/\n        }\n        .bold {\n            font-weight: bold;\n        }\n        .light {\n            font-weight: lighter;\n            color: grey;\n        }\n        .right-aligned {\n            text-align: right;\n        }\n\n        .clickable {\n            cursor: pointer;\n        }\n\n        .workflow {\n            border: solid gray 1px;\n        }\n        .workflow > .header {\n            background: lightgray;\n            padding: 5px 10px;\n        }\n        .workflow > .light {\n            color: gray;\n        }\n        .workflow > .body {\n            border-top: solid gray 1px;\n        }\n        .workflow > .body > .toolForm {\n            border: 0px;\n        }\n\n        div.toolForm {\n            border-width        : 1px;\n            border-radius       : 0px;\n        }\n        .toolForm > .header {\n            background-color: #EBD9B2;\n            padding: 5px 10px;\n        }\n        .workflow div.toolForm:not(:first-child) .header {\n            border-top: 1px solid #D6B161;\n        }\n        div.toolFormTitle {\n            padding: 0px 0px 4px 0px;\n            margin: 0px 0px 4px 0px;\n            border: 0px;\n            background-color: transparent;\n            border-bottom: 1px solid #D6B161;\n        }\n        /* down from EBD9B2 --> 90743A */\n        .toolFormTitle > .light {\n            color: #90743A;\n        }\n        .toolForm em {\n            color: #90743A;\n        }\n\n        .job-inputs {\n            margin: 0px 6px 0px 6px;\n            text-align: left;\n        }\n        .job-inputs td:nth-child(1) {\n            text-align: right;\n            font-weight: lighter;\n            color: #90743A;\n        }\n        .job-inputs td:nth-child(1):after {\n            content : \':\'\n        }\n        .job-inputs td:nth-child(2) {\n            padding-left: 4px;\n        }\n        .job-inputs em {\n        }\n\n        .job-inputs-show {\n            float: right;\n        }\n\n        .copied-from {\n            border: 1px solid lightgrey;\n            border-width: 1px 1px 0px 1px;\n        }\n        .copied-from .header {\n            border-bottom: 1px solid lightgrey;\n            padding: 5px;\n        }\n        .copied-from .header .bold, .copied-from .header a {\n            color: #888;\n        }\n\n        .dataset.hda {\n            min-height  : 37px;\n            border-width: 0px 0px 1px 0px;\n        }\n        .toolFormBody > .dataset.hda:last-child {\n            border-bottom-width: 0px;\n        }\n        .dataset.hda:first-child {\n            border-top: 1px solid #D6B161;\n        }\n        .dataset.hda .dataset-title-bar {\n            padding-top: 8px;\n            padding-left: 10px;\n        }\n\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,entity,children):
    context.caller_stack._push_frame()
    try:
        def render_item_hda(hda,children):
            return render_render_item_hda(context,hda,children)
        def render_item_wf(wf,children):
            return render_render_item_wf(context,wf,children)
        def render_item_job(job,children):
            return render_render_item_job(context,job,children)
        __M_writer = context.writer()
        # SOURCE LINE 177
        __M_writer(u'\n')
        # SOURCE LINE 178

        entity_name = entity.__class__.__name__
        if entity_name == "HistoryDatasetAssociation":
            render_item_hda( entity, children )
        elif entity_name == "Job":
            render_item_job( entity, children )
        elif entity_name == "WorkflowInvocation":
            render_item_wf( entity, children )
        
        
        # SOURCE LINE 186
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_job(context,job,children):
    context.caller_stack._push_frame()
    try:
        Exception = context.get('Exception', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        reversed = context.get('reversed', UNDEFINED)
        def render_item(entity,children):
            return render_render_item(context,entity,children)
        show_params = _mako_get_namespace(context, 'show_params')
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 255
        __M_writer(u'\n')
        # SOURCE LINE 257
        __M_writer(u'    <div class="tool toolForm">\n        ')
        # SOURCE LINE 258

        tool = trans.app.toolbox.get_tool( job.tool_id )
        if tool:
            tool_name = tool.name
            tool_desc = tool.description
        else:
            tool_name = "Unknown tool with id '%s'" % job.tool_id
            tool_desc = ''
        
        params_object = None
        try:
            params_object = job.get_param_values( trans.app, ignore_errors=True )
        except Exception, exc:
            pass
                
        
        # SOURCE LINE 272
        __M_writer(u'\n        <div class="header">\n            <div class="toolFormTitle">\n                <span class="bold">')
        # SOURCE LINE 275
        __M_writer(unicode(tool_name))
        __M_writer(u'</span>\n                <span class="light">- ')
        # SOURCE LINE 276
        __M_writer(unicode(tool_desc))
        __M_writer(u'</span>\n')
        # SOURCE LINE 278
        __M_writer(u'            </div>\n')
        # SOURCE LINE 279
        if tool and params_object:
            # SOURCE LINE 280
            __M_writer(u'            <table class="job-inputs">\n                ')
            # SOURCE LINE 281
            __M_writer(unicode( show_params.inputs_recursive( tool.inputs, params_object, depth=1 ) ))
            __M_writer(u'\n            </table>\n')
            # SOURCE LINE 283
        else:
            # SOURCE LINE 284
            __M_writer(u'                <em>(')
            __M_writer(unicode( _( 'No parameter data available' ) ))
            __M_writer(u')</em>\n')
            pass
        # SOURCE LINE 286
        __M_writer(u'        </div>\n        <div class="body toolFormBody">\n')
        # SOURCE LINE 288
        for e, c in reversed( children ):
            # SOURCE LINE 289
            __M_writer(u'            ')
            __M_writer(unicode(render_item( e, c )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 291
        __M_writer(u'        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        history = context.get('history', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 129
        __M_writer(u'\n')
        # SOURCE LINE 130

        self.js_app = 'display-structured'
        
        controller = trans.webapp.controllers[ 'history' ]
        hda_dicts = []
        id_hda_dict_map = {}
        for hda in history.active_datasets:
            hda_dict = controller.get_hda_dict( trans, hda )
            id_hda_dict_map[ hda_dict[ 'id' ] ] = hda_dict
            hda_dicts.append( hda_dict )
        
        
        # SOURCE LINE 140
        __M_writer(u'\n    ')
        # SOURCE LINE 141
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n')
        # SOURCE LINE 144
        __M_writer(u'    <script type="text/javascript">\n        define( \'display-structured\', function(){\n            require([ \'mvc/history/hda-li-edit\', \'mvc/history/hda-model\' ], function( hdaEdit, hdaModel ){\n                var hdaJSON = ')
        # SOURCE LINE 147
        __M_writer(unicode( h.dumps( hda_dicts, indent=( 2 if trans.debug else 0 ) ) ))
        __M_writer(u';\n\n                window.hdas = hdaJSON.map( function( hda ){\n                    return new hdaEdit.HDAListItemEdit({\n                        model           : new hdaModel.HistoryDatasetAssociation( hda ),\n                        el              : $( \'#hda-\' + hda.id ),\n                        linkTarget      : \'_self\',\n                        purgeAllowed    : Galaxy.config.allow_user_dataset_purge,\n                        logger          : Galaxy.logger\n                    }).render( false );\n                });\n            });\n        });\n\n        $(function(){\n            $( ".workflow, .tool" ).each( function(){\n                var body = $( this ).children( ".body" );\n                $( this ).children( ".header" ).click( function(){\n                    body.toggle();\n                }).addClass( "clickable" );\n            });\n            //$( ".job-inputs-show" ).click( function( ev ){\n            //    ev.stopPropagation();\n            //    $( this ).parent().siblings( \'.job-inputs\' ).toggle();\n            //});\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_hda_copied_from_history(context,hda,children):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 205
        __M_writer(u'\n')
        # SOURCE LINE 207
        __M_writer(u'    ')
        id = trans.security.encode_id( hda.id ) 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 208
        history_id = trans.security.encode_id( hda.copied_from_history_dataset_association.history_id ) 
        
        __M_writer(u'\n    <div class="copied-from copied-from-history">\n        <div class="header">\n            <div class="copied-from-dataset">\n                <span class="light">')
        # SOURCE LINE 212
        __M_writer(unicode( _( 'Copied from history dataset' ) + ':' ))
        __M_writer(u'</span>\n                <span class="bold">')
        # SOURCE LINE 213
        __M_writer(unicode( hda.copied_from_history_dataset_association.name ))
        __M_writer(u'</span>\n            </div>\n            <div class="copied-from-source">\n                <span class="light">')
        # SOURCE LINE 216
        __M_writer(unicode( _( 'History' ) + ':' ))
        __M_writer(u'</span>\n                <span class="bold">\n                    <a href="')
        # SOURCE LINE 218
        __M_writer(unicode( h.url_for( controller='history', action='view', id=history_id ) ))
        __M_writer(u'">\n                        ')
        # SOURCE LINE 219
        __M_writer(unicode( hda.copied_from_history_dataset_association.history.name ))
        __M_writer(u'\n                    </a>\n                </span>\n            </div>\n        </div>\n        <div id="hda-')
        # SOURCE LINE 224
        __M_writer(unicode(id))
        __M_writer(u'" class="dataset hda state-')
        __M_writer(unicode(hda.state))
        __M_writer(u'"></div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


