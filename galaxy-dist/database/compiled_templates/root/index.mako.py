# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417014200.187688
_template_filename='templates/webapps/galaxy/root/index.mako'
_template_uri='root/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['left_panel', 'center_panel', 'late_javascripts', 'right_panel', 'stylesheets', 'init', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 3
    ns = runtime.TemplateNamespace('__anon_0x23147550', context._clean_inheritance_tokens(), templateuri=u'/root/tool_menu.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x23147550')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/webapps/galaxy/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23147550')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(u'\n\n')
        # SOURCE LINE 20
        __M_writer(u'\n\n')
        # SOURCE LINE 137
        __M_writer(u'\n\n')
        # SOURCE LINE 153
        __M_writer(u'\n\n')
        # SOURCE LINE 164
        __M_writer(u'\n\n')
        # SOURCE LINE 187
        __M_writer(u'\n\n')
        # SOURCE LINE 239
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23147550')._populate(_import_ns, [u'*'])
        render_tool_menu = _import_ns.get('render_tool_menu', context.get('render_tool_menu', UNDEFINED))
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 155
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>\n            ')
        # SOURCE LINE 158
        __M_writer(unicode(n_('Tools')))
        __M_writer(u'\n        </div>\n    </div>\n    <div class="unified-panel-body" style="overflow: auto">\n        ')
        # SOURCE LINE 162
        __M_writer(unicode(render_tool_menu()))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23147550')._populate(_import_ns, [u'*'])
        tool_id = _import_ns.get('tool_id', context.get('tool_id', UNDEFINED))
        m_c = _import_ns.get('m_c', context.get('m_c', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        m_a = _import_ns.get('m_a', context.get('m_a', UNDEFINED))
        workflow_id = _import_ns.get('workflow_id', context.get('workflow_id', UNDEFINED))
        params = _import_ns.get('params', context.get('params', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 166
        __M_writer(u'\n\n')
        # SOURCE LINE 169
        __M_writer(u'    ')

        if trans.app.config.require_login and not trans.user:
            center_url = h.url_for( controller='user', action='login' )
        elif tool_id is not None:
            center_url = h.url_for( 'tool_runner', tool_id=tool_id, from_noframe=True, **params )
        elif workflow_id is not None:
            center_url = h.url_for( controller='workflow', action='run', id=workflow_id )
        elif m_c is not None:
            center_url = h.url_for( controller=m_c, action=m_a )
        else:
            center_url = h.url_for( controller="root", action="welcome" )
        
        
        # SOURCE LINE 180
        __M_writer(u'\n    \n    <div style="position: absolute; width: 100%; height: 100%">\n        <iframe name="galaxy_main" id="galaxy_main" frameborder="0"\n                style="position: absolute; width: 100%; height: 100%;" src="')
        # SOURCE LINE 184
        __M_writer(unicode(center_url))
        __M_writer(u'"></iframe>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23147550')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n    ')
        # SOURCE LINE 23
        __M_writer(unicode(parent.late_javascripts()))
        __M_writer(u'\n\n    <script type="text/javascript">\n    // Set up GalaxyAsync object.\n    var galaxy_async = new GalaxyAsync();\n    galaxy_async.set_func_url( galaxy_async.set_user_pref,\n        "')
        # SOURCE LINE 29
        __M_writer(unicode(h.url_for( controller='user', action='set_user_pref_async' )))
        __M_writer(u'");\n    \n    // set up history options menu\n    $(function(){\n        // Init history options.\n        //$("#history-options-button").css( "position", "relative" );\n        var popupmenu = PopupMenu.make_popupmenu( $("#history-options-button"), {\n            "')
        # SOURCE LINE 36
        __M_writer(unicode(_("History Lists")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 37
        __M_writer(unicode(_("Saved Histories")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 38
        __M_writer(unicode(h.url_for( controller='history', action='list')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 40
        __M_writer(unicode(_("Histories Shared with Me")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 41
        __M_writer(unicode(h.url_for( controller='history', action='list_shared')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 43
        __M_writer(unicode(_("Current History")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 44
        __M_writer(unicode(_("Create New")))
        __M_writer(u'": function() {\n                if( Galaxy && Galaxy.currHistoryPanel ){\n                    Galaxy.currHistoryPanel.createNewHistory();\n                }\n            },\n            "')
        # SOURCE LINE 49
        __M_writer(unicode(_("Copy History")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 50
        __M_writer(unicode(h.url_for( controller='history', action='copy')))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 52
        __M_writer(unicode(_("Copy Datasets")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 53
        __M_writer(unicode(h.url_for( controller='dataset', action='copy_datasets' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 55
        __M_writer(unicode(_("Share or Publish")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 56
        __M_writer(unicode(h.url_for( controller='history', action='sharing' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 58
        __M_writer(unicode(_("Extract Workflow")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 59
        __M_writer(unicode(h.url_for( controller='workflow', action='build_from_current_history' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 61
        __M_writer(unicode(_("Dataset Security")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 62
        __M_writer(unicode(h.url_for( controller='root', action='history_set_default_permissions' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 64
        __M_writer(unicode(_("Resume Paused Jobs")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 65
        __M_writer(unicode(h.url_for( controller='history', action='resume_paused_jobs', current=True)))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 67
        __M_writer(unicode(_("Collapse Expanded Datasets")))
        __M_writer(u'": function() {\n                if( Galaxy && Galaxy.currHistoryPanel ){\n                    Galaxy.currHistoryPanel.collapseAll();\n                }\n            },\n            "')
        # SOURCE LINE 72
        __M_writer(unicode(_("Include Deleted Datasets")))
        __M_writer(u'": function( clickEvent, thisMenuOption ) {\n                if( Galaxy && Galaxy.currHistoryPanel ){\n                    thisMenuOption.checked = Galaxy.currHistoryPanel.toggleShowDeleted();\n                }\n            },\n            "')
        # SOURCE LINE 77
        __M_writer(unicode(_("Include Hidden Datasets")))
        __M_writer(u'": function( clickEvent, thisMenuOption ) {\n                if( Galaxy && Galaxy.currHistoryPanel ){\n                    thisMenuOption.checked = Galaxy.currHistoryPanel.toggleShowHidden();\n                }\n            },\n            "')
        # SOURCE LINE 82
        __M_writer(unicode(_("Unhide Hidden Datasets")))
        __M_writer(u'": function() {\n                if ( confirm( "Really unhide all hidden datasets?" ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 84
        __M_writer(unicode(h.url_for( controller='history', action='unhide_datasets', current=True )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 87
        __M_writer(unicode(_("Delete Hidden Datasets")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete all hidden datasets?" ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 89
        __M_writer(unicode(h.url_for( controller='history', action='delete_hidden_datasets')))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 92
        __M_writer(unicode(_("Purge Deleted Datasets")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete all deleted datasets permanently? This cannot be undone." ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 94
        __M_writer(unicode(h.url_for( controller='history', action='purge_deleted_datasets' )))
        __M_writer(u'";\n                    // update the user disk size when the purge page loads\n                    $( \'#galaxy_main\' ).load( function(){\n                        Galaxy.user.fetch();\n                    })\n                }\n            },\n            "')
        # SOURCE LINE 101
        __M_writer(unicode(_("Show Structure")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 102
        __M_writer(unicode(h.url_for( controller='history', action='display_structured' )))
        __M_writer(u'";\n            },            \n            "')
        # SOURCE LINE 104
        __M_writer(unicode(_("Export Citations")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 105
        __M_writer(unicode(h.url_for( controller='history', action='citations' )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 107
        __M_writer(unicode(_("Export to File")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 108
        __M_writer(unicode(h.url_for( controller='history', action='export_archive', preview=True )))
        __M_writer(u'";\n            },\n            "')
        # SOURCE LINE 110
        __M_writer(unicode(_("Delete")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete the current history?" ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 112
        __M_writer(unicode(h.url_for( controller='history', action='delete_current' )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 115
        __M_writer(unicode(_("Delete Permanently")))
        __M_writer(u'": function() {\n                if ( confirm( "Really delete the current history permanently? This cannot be undone." ) ) {\n                    galaxy_main.location = "')
        # SOURCE LINE 117
        __M_writer(unicode(h.url_for( controller='history', action='delete_current', purge=True )))
        __M_writer(u'";\n                }\n            },\n            "')
        # SOURCE LINE 120
        __M_writer(unicode(_("Other Actions")))
        __M_writer(u'": null,\n            "')
        # SOURCE LINE 121
        __M_writer(unicode(_("Import from File")))
        __M_writer(u'": function() {\n                galaxy_main.location = "')
        # SOURCE LINE 122
        __M_writer(unicode(h.url_for( controller='history', action='import_archive' )))
        __M_writer(u'";\n            }\n        });\n        Galaxy.historyOptionsMenu = popupmenu;\n\n        // Fix iFrame scrolling on iOS\n        if( navigator.userAgent.match( /(iPhone|iPod|iPad)/i ) ) {\n            $("iframe").parent().css( {\n                "overflow": "scroll",\n                "-webkit-overflow-scrolling": "touch"\n            })\n        }\n\n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23147550')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        _ = _import_ns.get('_', context.get('_', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 189
        __M_writer(u'\n    <!-- current history panel -->\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            <div style="float: right">\n                <a id="history-refresh-button" class=\'panel-header-button\' href="javascript:void(0)"\n                   title="')
        # SOURCE LINE 195
        __M_writer(unicode( _( 'Refresh history' ) ))
        __M_writer(u'">\n                    <span class="fa fa-refresh"></span>\n                </a>\n                <a id="history-options-button" class=\'panel-header-button\'\n                   href="')
        # SOURCE LINE 199
        __M_writer(unicode(h.url_for( controller='root', action='history_options' )))
        __M_writer(u'" target="galaxy_main"\n                   title="')
        # SOURCE LINE 200
        __M_writer(unicode( _( 'History options' ) ))
        __M_writer(u'">\n                    <span class="fa fa-cog"></span>\n                </a>\n            </div>\n            <div class="panel-header-text">')
        # SOURCE LINE 204
        __M_writer(unicode(_('History')))
        __M_writer(u'</div>\n        </div>\n    </div>\n    <div class="unified-panel-body">\n        <div id="current-history-panel" class="history-panel"></div>\n')
        # SOURCE LINE 210
        __M_writer(u'        <script type="text/javascript">\n        require([ "mvc/history/history-panel-edit-current" ], function( historyPanel ){\n            $(function(){\n                var currPanel = new historyPanel.CurrentHistoryPanel({\n                    el              : $( "#current-history-panel" ),\n                    purgeAllowed    : Galaxy.config.allow_user_dataset_purge,\n                    linkTarget      : \'galaxy_main\',\n                    $scrollContainer: function(){ return this.$el.parent(); }\n                });\n                currPanel\n                    .connectToQuotaMeter( Galaxy.quotaMeter )\n                    .connectToOptionsMenu( Galaxy.historyOptionsMenu );\n                currPanel.loadCurrentHistory();\n                Galaxy.currHistoryPanel = currPanel;\n            });\n        });\n        </script>\n        <script type="text/javascript">\n            $(function(){\n                $( \'#history-refresh-button\' )\n                    .on( \'click\', function(){\n                        if( top.Galaxy && top.Galaxy.currHistoryPanel ){\n                            top.Galaxy.currHistoryPanel.loadCurrentHistory();\n                            inside_galaxy_frameset = true;\n                        }\n                    });\n            });\n        </script>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23147550')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    ')
        # SOURCE LINE 6
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        # SOURCE LINE 7
        __M_writer(unicode(h.css("tool_menu")))
        __M_writer(u'\n    <style>\n        #right .unified-panel-body {\n            background: none repeat scroll 0 0 #DFE5F9;\n            overflow: auto;\n            padding: 0;\n        }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23147550')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 139
        __M_writer(u'\n')
        # SOURCE LINE 140

        self.has_left_panel = True
        self.has_right_panel = True
        self.active_view = "analysis"
        self.require_javascript = True
        
        
        # SOURCE LINE 145
        __M_writer(u'\n')
        # SOURCE LINE 146
        if trans.app.config.require_login and not trans.user:
            # SOURCE LINE 147
            __M_writer(u'    <script type="text/javascript">\n        if ( window != top ) {\n            top.location.href = location.href;\n        }\n    </script>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x23147550')._populate(_import_ns, [u'*'])
        tool_menu_javascripts = _import_ns.get('tool_menu_javascripts', context.get('tool_menu_javascripts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        # SOURCE LINE 19
        __M_writer(unicode(tool_menu_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


