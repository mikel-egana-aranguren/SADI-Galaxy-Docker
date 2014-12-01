# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417442153.654742
_template_filename='templates/webapps/galaxy/history/view.mako'
_template_uri='history/view.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['body', 'title', 'center_panel', 'stylesheets', 'init', 'javascripts']


# SOURCE LINE 4

def inherit(context):
    if context.get('use_panels'):
        return '/webapps/galaxy/base_panels.mako'
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x7f5a30639390', context._clean_inheritance_tokens(), templateuri=u'/galaxy.masthead.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f5a30639390')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30639390')._populate(_import_ns, [u'get_user_json'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        __M_writer(u'\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n\n')
        # SOURCE LINE 70
        __M_writer(u'\n\n')
        # SOURCE LINE 203
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30639390')._populate(_import_ns, [u'get_user_json'])
        def center_panel():
            return render_center_panel(context)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n    ')
        # SOURCE LINE 23
        __M_writer(unicode(center_panel()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30639390')._populate(_import_ns, [u'get_user_json'])
        history = _import_ns.get('history', context.get('history', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n    ')
        # SOURCE LINE 28
        __M_writer(unicode(history[ 'name' ]))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30639390')._populate(_import_ns, [u'get_user_json'])
        hdas = _import_ns.get('hdas', context.get('hdas', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        user_is_owner = _import_ns.get('user_is_owner', context.get('user_is_owner', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        history = _import_ns.get('history', context.get('history', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\n')
        # SOURCE LINE 74

        imp_with_deleted_url = h.url_for( controller='history', action='imp', id=history[ 'id' ], all_datasets=True )
        imp_without_deleted_url = h.url_for( controller='history', action='imp', id=history[ 'id' ] )
        
        structure_url = h.url_for( controller='history', action='display_structured', id=history[ 'id' ] )
        
        switch_to_url = h.url_for( controller='history', action='switch_to_history', hist_id=history[ 'id' ] )
        
        show_deleted = context.get( 'show_deleted', None )
        show_hidden  = context.get( 'show_hidden',  None )
        
        user_is_owner_json = 'true' if user_is_owner else 'false'
        show_deleted_json  = h.dumps( show_deleted )
        show_hidden_json   = h.dumps( show_hidden )
        
        
        # SOURCE LINE 88
        __M_writer(u'\n\n<div id="header" class="clear">\n    <div id="history-view-controls">\n        <div class="pull-left">\n')
        # SOURCE LINE 93
        if not history[ 'purged' ]:
            # SOURCE LINE 94
            if user_is_owner:
                # SOURCE LINE 95
                __M_writer(u'                    <button id="switch" class="btn btn-default">')
                __M_writer(unicode( _( 'Switch to this history' ) ))
                __M_writer(u'</button>\n')
                # SOURCE LINE 96
            else:
                # SOURCE LINE 97
                __M_writer(u'                    <button id="import" class="btn btn-default"></button>\n')
                pass
            # SOURCE LINE 99
            __M_writer(u'                <a id="structure" href="')
            __M_writer(unicode( structure_url ))
            __M_writer(u'" class="btn btn-default">')
            __M_writer(unicode( _( 'Show structure' ) ))
            __M_writer(u'</a>\n')
            pass
        # SOURCE LINE 101
        __M_writer(u'        </div>\n        <div class="pull-right">\n            <button id="toggle-deleted" class="btn btn-default"></button>\n            <button id="toggle-hidden" class="btn btn-default"></button>\n        </div>\n    </div>\n</div>\n\n<div id="history-')
        # SOURCE LINE 109
        __M_writer(unicode( history[ 'id' ] ))
        __M_writer(u'" class="history-panel unified-panel-body" style="overflow: auto;"></div>\n\n<script type="text/javascript">\n\n    function setUpBehaviors(){\n\n        $( \'#toggle-deleted\' ).modeButton({\n            initialMode : "')
        # SOURCE LINE 116
        __M_writer(unicode( 'showing_deleted' if show_deleted else 'not_showing_deleted' ))
        __M_writer(u'",\n            modes: [\n                { mode: \'showing_deleted\',      html: _l( \'Exclude deleted\' ) },\n                { mode: \'not_showing_deleted\',  html: _l( \'Include deleted\' ) }\n            ]\n        }).click( function(){\n            // allow the \'include/exclude deleted\' button to control whether the \'import\' button includes deleted\n            //  datasets when importing or not; when deleted datasets are shown, they\'ll be imported\n            $( \'#import\' ).modeButton( \'setMode\',\n                $( this ).modeButton( \'current\' ) === \'showing_deleted\'? \'with_deleted\': \'without_deleted\' );\n        });\n\n        $( \'#toggle-hidden\' ).modeButton({\n            initialMode : "')
        # SOURCE LINE 129
        __M_writer(unicode( 'showing_hidden' if show_hidden else 'not_showing_hidden' ))
        __M_writer(u'",\n            modes: [\n                { mode: \'showing_hidden\',     html: _l( \'Exclude hidden\' ) },\n                { mode: \'not_showing_hidden\', html: _l( \'Include hidden\' ) }\n            ]\n        });\n\n        $( \'#switch\' ).click( function( ev ){\n')
        # SOURCE LINE 139
        __M_writer(u'            var hpanel = Galaxy.currHistoryPanel\n                      || ( top.Galaxy && top.Galaxy.currHistoryPanel )? top.Galaxy.currHistoryPanel : null;\n            if( hpanel ){\n                hpanel.switchToHistory( "')
        # SOURCE LINE 142
        __M_writer(unicode( history[ 'id' ] ))
        __M_writer(u'" );\n            } else {\n                window.location = "')
        # SOURCE LINE 144
        __M_writer(unicode( switch_to_url ))
        __M_writer(u'";\n            }\n        });\n        \n        $( \'#import\' ).modeButton({\n            switchModesOnClick : false,\n            initialMode : "')
        # SOURCE LINE 150
        __M_writer(unicode( 'with_deleted' if show_deleted else 'without_deleted' ))
        __M_writer(u'",\n            modes: [\n                { mode: \'with_deleted\', html: _l( \'Import with deleted datasets and start using history\' ),\n                    onclick: function importWithDeleted(){\n                        window.location = \'')
        # SOURCE LINE 154
        __M_writer(unicode(imp_with_deleted_url))
        __M_writer(u"';\n                    }\n                },\n                { mode: 'without_deleted', html: _l( 'Import and start using history' ),\n                    onclick: function importWithoutDeleted(){\n                        window.location = '")
        # SOURCE LINE 159
        __M_writer(unicode(imp_without_deleted_url))
        __M_writer(u"';\n                    }\n                }\n            ]\n        });\n    }\n\n    var userIsOwner  = ")
        # SOURCE LINE 166
        __M_writer(unicode('true' if user_is_owner else 'false'))
        __M_writer(u',\n        historyJSON  = ')
        # SOURCE LINE 167
        __M_writer(unicode(h.dumps( history )))
        __M_writer(u',\n        hdaJSON      = ')
        # SOURCE LINE 168
        __M_writer(unicode(h.dumps( hdas )))
        __M_writer(u';\n        panelToUse   = ( userIsOwner )?\n//TODO: change class names\n            ({ location: \'mvc/history/history-panel-edit\',  className: \'HistoryPanelEdit\' }):\n            ({ location: \'mvc/history/history-panel\',       className: \'HistoryPanel\' });\n\n    require.config({\n        baseUrl : "')
        # SOURCE LINE 175
        __M_writer(unicode(h.url_for( '/static/scripts' )))
        __M_writer(u'"\n    })([ \'mvc/user/user-model\', panelToUse.location, \'utils/localization\' ], function( user, panelMod, _l ){\n        $(function(){\n            setUpBehaviors();\n     \n            var panelClass = panelMod[ panelToUse.className ],\n                // history module is already in the dpn chain from the panel. We can re-scope it here.\n                historyModel = require( \'mvc/history/history-model\' ),\n                history = new historyModel.History( historyJSON, hdaJSON );\n\n            window.historyPanel = new panelClass({\n                show_deleted    : ')
        # SOURCE LINE 186
        __M_writer(unicode(show_deleted_json))
        __M_writer(u',\n                show_hidden     : ')
        # SOURCE LINE 187
        __M_writer(unicode(show_hidden_json))
        __M_writer(u',\n                purgeAllowed    : Galaxy.config.allow_user_dataset_purge,\n                el              : $( "#history-" + historyJSON.id ),\n                model           : history\n            }).render();\n\n            $( \'#toggle-deleted\' ).on( \'click\', function(){\n                historyPanel.toggleShowDeleted();\n            });\n            $( \'#toggle-hidden\' ).on( \'click\', function(){\n                historyPanel.toggleShowHidden();\n            });\n        });\n    });\n</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30639390')._populate(_import_ns, [u'get_user_json'])
        use_panels = _import_ns.get('use_panels', context.get('use_panels', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n')
        # SOURCE LINE 33
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n<style>\n')
        # SOURCE LINE 35
        if not use_panels:
            # SOURCE LINE 36
            __M_writer(u'    body, html {\n        margin: 0px;\n        padding: 0px;\n    }\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'#header {\n    background-color: white;\n    border-bottom: 1px solid #DDD;\n    width: 100%;\n    height: 48px;\n}\n#history-view-controls {\n    margin: 10px 10px 10px 10px;\n}\n.history-panel {\n    /* this and the height of #header above are way too tweaky */\n    margin-top: 18px;\n}\n.history-title {\n    font-size: 120%;\n}\n.history-title input {\n    font-size: 100%;\n}\na.btn {\n    text-decoration: none;\n}\n</style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30639390')._populate(_import_ns, [u'get_user_json'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\n')
        # SOURCE LINE 14

        self.has_left_panel=False
        self.has_right_panel=False
        self.message_box_visible=False
        
        
        # SOURCE LINE 18
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f5a30639390')._populate(_import_ns, [u'get_user_json'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 67
        __M_writer(u'\n')
        # SOURCE LINE 68
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


