# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417014200.231505
_template_filename=u'templates/base/base_panels.mako'
_template_uri=u'/base/base_panels.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['overlay', 'late_javascripts', 'stylesheets', 'init', 'javascript_app', 'masthead', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'galaxy_client', context._clean_inheritance_tokens(), templateuri=u'/galaxy_client_app.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'galaxy_client')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        app = context.get('app', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML>\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4

        self.has_left_panel = hasattr( self, 'left_panel' )
        self.has_right_panel = hasattr( self, 'right_panel' )
        self.message_box_visible = app.config.message_box_visible
        self.show_inactivity_warning = False
        if trans.webapp.name == 'galaxy' and trans.user:
            self.show_inactivity_warning = ( ( trans.user.active is False ) and ( app.config.user_activation_on ) and ( app.config.inactivity_box_content is not None ) )
        self.overlay_visible=False
        self.active_view=None
        self.body_class=""
        self.require_javascript=False
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 15
        __M_writer(u'\n    \n')
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 37
        __M_writer(u'\n\n')
        # SOURCE LINE 97
        __M_writer(u'\n\n')
        # SOURCE LINE 102
        __M_writer(u'\n\n')
        # SOURCE LINE 252
        __M_writer(u'\n\n')
        # SOURCE LINE 257
        __M_writer(u'\n\n')
        # SOURCE LINE 289
        __M_writer(u'\n\n')
        # SOURCE LINE 292
        __M_writer(u'<html>\n    <!--base_panels.mako-->\n    ')
        # SOURCE LINE 294
        __M_writer(unicode(self.init()))
        __M_writer(u'    \n    <head>\n')
        # SOURCE LINE 296
        if app.config.brand:
            # SOURCE LINE 297
            __M_writer(u'            <title>')
            __M_writer(unicode(self.title()))
            __M_writer(u' / ')
            __M_writer(unicode(app.config.brand))
            __M_writer(u'</title>\n')
            # SOURCE LINE 298
        else:
            # SOURCE LINE 299
            __M_writer(u'            <title>')
            __M_writer(unicode(self.title()))
            __M_writer(u'</title>\n')
            pass
        # SOURCE LINE 301
        __M_writer(u'        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        # SOURCE LINE 303
        __M_writer(u'        <meta name = "viewport" content = "maximum-scale=1.0">\n')
        # SOURCE LINE 305
        __M_writer(u'        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n        ')
        # SOURCE LINE 306
        __M_writer(unicode(self.stylesheets()))
        __M_writer(u'\n        ')
        # SOURCE LINE 307
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n        ')
        # SOURCE LINE 308
        __M_writer(unicode(self.javascript_app()))
        __M_writer(u'\n    </head>\n    \n    ')
        # SOURCE LINE 311

        body_class = self.body_class
        if self.message_box_visible:
            body_class += " has-message-box"
        if self.show_inactivity_warning:
            body_class += " has-inactivity-box"
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['body_class'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 317
        __M_writer(u'\n\n    <body scroll="no" class="full-content ')
        # SOURCE LINE 319
        __M_writer(unicode(body_class))
        __M_writer(u'">\n')
        # SOURCE LINE 320
        if self.require_javascript:
            # SOURCE LINE 321
            __M_writer(u'            <noscript>\n                <div class="overlay overlay-background">\n                    <div class="modal dialog-box" border="0">\n                        <div class="modal-header"><h3 class="title">Javascript Required</h3></div>\n                        <div class="modal-body">The Galaxy analysis interface requires a browser with Javascript enabled. <br> Please enable Javascript and refresh this page</div>\n                    </div>\n                </div>\n            </noscript>\n')
            pass
        # SOURCE LINE 330
        __M_writer(u'        <div id="everything" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">\n')
        # SOURCE LINE 332
        __M_writer(u'            <div id="background"></div>\n')
        # SOURCE LINE 334
        __M_writer(u'            <div id="masthead" class="navbar navbar-fixed-top navbar-inverse">\n                ')
        # SOURCE LINE 335
        __M_writer(unicode(self.masthead()))
        __M_writer(u'\n            </div>\n            <div id="messagebox" class="panel-')
        # SOURCE LINE 337
        __M_writer(unicode(app.config.message_box_class))
        __M_writer(u'-message">\n                ')
        # SOURCE LINE 338
        __M_writer(unicode(app.config.message_box_content))
        __M_writer(u'\n            </div>\n')
        # SOURCE LINE 340
        if self.show_inactivity_warning:
            # SOURCE LINE 341
            __M_writer(u'                <div id="inactivebox" class="panel-warning-message">\n                    ')
            # SOURCE LINE 342
            __M_writer(unicode(app.config.inactivity_box_content))
            __M_writer(u' <a href="')
            __M_writer(unicode(h.url_for( controller='user', action='resend_verification' )))
            __M_writer(u'">Resend verification.</a>\n                </div>\n')
            pass
        # SOURCE LINE 345
        __M_writer(u'            ')
        __M_writer(unicode(self.overlay(visible=self.overlay_visible)))
        __M_writer(u'\n')
        # SOURCE LINE 346
        if self.has_left_panel:
            # SOURCE LINE 347
            __M_writer(u'                <div id="left">\n                    ')
            # SOURCE LINE 348
            __M_writer(unicode(self.left_panel()))
            __M_writer(u'\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse"></div>\n                        <div class="drag"></div>\n                    </div>\n                </div><!--end left-->\n')
            pass
        # SOURCE LINE 355
        __M_writer(u'            <div id="center" class="inbound">\n                ')
        # SOURCE LINE 356
        __M_writer(unicode(self.center_panel()))
        __M_writer(u'\n            </div><!--end center-->\n')
        # SOURCE LINE 358
        if self.has_right_panel:
            # SOURCE LINE 359
            __M_writer(u'                <div id="right">\n                    ')
            # SOURCE LINE 360
            __M_writer(unicode(self.right_panel()))
            __M_writer(u'\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse right"></div>\n                        <div class="drag"></div>\n                    </div>\n                </div><!--end right-->\n')
            pass
        # SOURCE LINE 367
        __M_writer(u'        </div><!--end everything-->\n')
        # SOURCE LINE 369
        __M_writer(u'    </body>\n')
        # SOURCE LINE 372
        __M_writer(u'    ')
        __M_writer(unicode(self.late_javascripts()))
        __M_writer(u'\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context,title='',content='',visible=False):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 259
        __M_writer(u'\n    ')
        # SOURCE LINE 260
        __M_writer(u'\n    ')
        # SOURCE LINE 261
        __M_writer(u'\n\n    ')
        # SOURCE LINE 263

        if visible:
            display = "style='display: block;'"
            overlay_class = "in"
        else:
            display = "style='display: none;'"
            overlay_class = ""
        
        
        # SOURCE LINE 270
        __M_writer(u'\n\n    <div id="top-modal" class="modal fade ')
        # SOURCE LINE 272
        __M_writer(unicode(overlay_class))
        __M_writer(u'" ')
        __M_writer(unicode(display))
        __M_writer(u'>\n        <div id="top-modal-backdrop" class="modal-backdrop fade ')
        # SOURCE LINE 273
        __M_writer(unicode(overlay_class))
        __M_writer(u'" style="z-index: -1"></div>\n        <div id="top-modal-dialog" class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <button type=\'button\' class=\'close\' style="display: none;">&times;</button>\n                    <h4 class=\'title\'>')
        # SOURCE LINE 278
        __M_writer(unicode(title))
        __M_writer(u'</h4>\n                </div>\n                <div class="modal-body">')
        # SOURCE LINE 280
        __M_writer(unicode(content))
        __M_writer(u'</div>\n                <div class="modal-footer">\n                    <div class="buttons" style="float: right;"></div>\n                    <div class="extra_buttons" style=""></div>\n                    <div style="clear: both;"></div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 105
        __M_writer(u'\n')
        # SOURCE LINE 108
        __M_writer(u'    ')
        __M_writer(unicode(h.js(
        'libs/jquery/jquery.event.hover',
        'libs/jquery/jquery.form',
        'libs/jquery/jquery.rating',
        'galaxy.panels'
    )))
        # SOURCE LINE 113
        __M_writer(u'\n    <script type="text/javascript">\n        \n    ensure_dd_helper();\n        \n')
        # SOURCE LINE 118
        if self.has_left_panel:
            # SOURCE LINE 119
            __M_writer(u'            var lp = new Panel( { panel: $("#left"), center: $("#center"), drag: $("#left > .unified-panel-footer > .drag" ), toggle: $("#left > .unified-panel-footer > .panel-collapse" ) } );\n            force_left_panel = function( x ) { lp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 122
        __M_writer(u'        \n')
        # SOURCE LINE 123
        if self.has_right_panel:
            # SOURCE LINE 124
            __M_writer(u'            var rp = new Panel( { panel: $("#right"), center: $("#center"), drag: $("#right > .unified-panel-footer > .drag" ), toggle: $("#right > .unified-panel-footer > .panel-collapse" ), right: true } );\n            window.handle_minwidth_hint = function( x ) { rp.handle_minwidth_hint( x ) };\n            force_right_panel = function( x ) { rp.force_panel( x ) };\n')
            pass
        # SOURCE LINE 128
        __M_writer(u'    \n    </script>\n')
        # SOURCE LINE 131
        __M_writer(u'    <script type="text/javascript">\n        var upload_form_error = function( msg ) {\n            var $galaxy_mainBody = $("iframe#galaxy_main").contents().find("body"),\n                $errMsg = $galaxy_mainBody.find( \'div.errormessage\' );\n            if ( !$errMsg.size() ){\n                $errMsg = $( \'<div/>\' ).addClass( \'errormessage\' ).prependTo( $galaxy_mainBody );\n            }\n            $errMsg.text( msg );\n        }\n\n        var uploads_in_progress = 0;\n        function decrementUploadsInProgress(){\n            uploads_in_progress -= 1;\n            if( uploads_in_progress === 0 ){\n                window.onbeforeunload = null;\n            }\n        }\n        jQuery( function() {\n            $("iframe#galaxy_main").load( function() {\n                $(this).contents().find("form").each( function() {\n                    if ( $(this).find("input[galaxy-ajax-upload]").length > 0 ){\n                        var $form = $( this );\n\n                        $(this).submit( function( event ) {\n                            // Only bother using a hidden iframe if there\'s a file (e.g. big data) upload\n                            var file_upload = false;\n                            $(this).find("input[galaxy-ajax-upload]").each( function() {\n                                if ( $(this).val() != \'\' ) {\n                                    file_upload = true;\n                                }\n                            });\n                            if ( ! file_upload ) {\n                                return true;\n                            }\n                            // Make a synchronous request to create the datasets first\n                            var async_datasets;\n                            var upload_error = false;\n\n                            //NOTE: in order for upload.py to match the datasets created below, we\'ll move the js File\n                            //  object\'s name into the file_data field (not in the form only for what we send to\n                            //  upload_async_create)\n                            var formData = $( this ).serializeArray();\n                            var name = function(){\n                                var $fileInput = $form.find( \'input[name="files_0|file_data"]\' );\n                                if( /msie/.test( navigator.userAgent.toLowerCase() ) ){\n                                    return $fileInput.val().replace( \'C:\\\\fakepath\\\\\', \'\' );\n                                } else {\n                                    return $fileInput.get( 0 ).files[0].name;\n                                }\n                            }\n                            formData.push({ name: "files_0|file_data", value: name });\n\n                            $.ajax( {\n                                async:      false,\n                                type:       "POST",\n                                url:        "')
        # SOURCE LINE 186
        __M_writer(unicode(h.url_for(controller='/tool_runner', action='upload_async_create')))
        __M_writer(u'",\n                                data:       formData,\n                                dataType:   "json",\n                                success:    function(array_obj, status) {\n                                                if (array_obj.length > 0) {\n                                                    if (array_obj[0] == \'error\') {\n                                                        upload_error = true;\n                                                        upload_form_error(array_obj[1]);\n                                                    } else {\n                                                        async_datasets = array_obj.join();\n                                                    }\n                                                } else {\n                                                    // ( gvk 1/22/10 ) FIXME: this block is never entered, so there may be a bug somewhere\n                                                    // I\'ve done some debugging like checking to see if array_obj is undefined, but have not\n                                                    // tracked down the behavior that will result in this block being entered.  I believe the\n                                                    // intent was to have this block entered if the upload button is clicked on the upload\n                                                    // form but no file was selected.\n                                                    upload_error = true;\n                                                    upload_form_error( \'No data was entered in the upload form.  You may choose to upload a file, paste some data directly in the data box, or enter URL(s) to fetch data.\' );\n                                                }\n                                            }\n                            } );\n\n                            // show the dataset we created above in the history panel\n                            Galaxy && Galaxy.currHistoryPanel && Galaxy.currHistoryPanel.refreshContents();\n\n                            if (upload_error == true) {\n                                return false;\n                            } else {\n                                $(this).find("input[name=async_datasets]").val( async_datasets );\n                                $(this).append("<input type=\'hidden\' name=\'ajax_upload\' value=\'true\'>");\n                            }\n                            // iframe submit is required for nginx (otherwise the encoding is wrong)\n                            $(this).ajaxSubmit({\n                                //iframe: true,\n                                error: function( xhr, msg, status ){\n                                    decrementUploadsInProgress();\n                                },\n                                success: function ( response, x, y, z ) {\n                                    decrementUploadsInProgress();\n                                }\n                            });\n                            uploads_in_progress++;\n                            window.onbeforeunload = function() {\n                                return "Navigating away from the Galaxy analysis interface will interrupt the "\n                                        + "file upload(s) currently in progress.  Do you really want to do this?";\n                            }\n                            if ( $(this).find("input[name=\'folder_id\']").val() != undefined ) {\n                                var library_id = $(this).find("input[name=\'library_id\']").val();\n                                var show_deleted = $(this).find("input[name=\'show_deleted\']").val();\n                                if ( location.pathname.indexOf( \'admin\' ) != -1 ) {\n                                    $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 237
        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library' )))
        __M_writer(u'?cntrller=library_admin&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);\n                                } else {\n                                    $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 239
        __M_writer(unicode(h.url_for( controller='library_common', action='browse_library' )))
        __M_writer(u'?cntrller=library&id=" + library_id + "&created_ldda_ids=" + async_datasets + "&show_deleted=" + show_deleted);\n                                }\n                            } else {\n                                $("iframe#galaxy_main").attr("src","')
        # SOURCE LINE 242
        __M_writer(unicode(h.url_for(controller='tool_runner', action='upload_async_message')))
        __M_writer(u'");\n                            }\n                            event.preventDefault();\n                            return false;\n                        });\n                    }\n                });\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n    ')
        # SOURCE LINE 23
        __M_writer(unicode(h.css(
        'base',
        'jquery.rating'
    )))
        # SOURCE LINE 26
        __M_writer(u'\n    <style type="text/css">\n    #center {\n')
        # SOURCE LINE 29
        if not self.has_left_panel:
            # SOURCE LINE 30
            __M_writer(u'            left: 0 !important;\n')
            pass
        # SOURCE LINE 32
        if not self.has_right_panel:
            # SOURCE LINE 33
            __M_writer(u'            right: 0 !important;\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    context.caller_stack._push_frame()
    try:
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        __M_writer = context.writer()
        # SOURCE LINE 99
        __M_writer(u'\n')
        # SOURCE LINE 101
        __M_writer(u'    ')
        __M_writer(unicode( galaxy_client.load() ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 255
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        if app.config.sentry_dsn:
            # SOURCE LINE 44
            __M_writer(u'        ')
            __M_writer(unicode(h.js( "libs/tracekit", "libs/raven" )))
            __M_writer(u"\n        <script>\n            Raven.config('")
            # SOURCE LINE 46
            __M_writer(unicode(app.config.sentry_dsn_public))
            __M_writer(u"').install();\n")
            # SOURCE LINE 47
            if trans.user:
                # SOURCE LINE 48
                __M_writer(u'                Raven.setUser( { email: "')
                __M_writer(unicode(trans.user.email))
                __M_writer(u'" } );\n')
                pass
            # SOURCE LINE 50
            __M_writer(u'        </script>\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'\n    ')
        # SOURCE LINE 53
        __M_writer(unicode(h.js(
        'libs/jquery/jquery',
        'libs/jquery/jquery.migrate',
        'libs/jquery/select2',
        'libs/bootstrap',
        'libs/underscore',
        'libs/backbone/backbone',
        'libs/handlebars.runtime',
        'galaxy.base',
        'libs/require',
        "mvc/ui"
    )))
        # SOURCE LINE 64
        __M_writer(u'\n    \n    <script type="text/javascript">\n')
        # SOURCE LINE 68
        __M_writer(u"        var galaxy_config =\n        {\n            root: '")
        # SOURCE LINE 70
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u'\'\n        };\n\n        //## load additional style sheet\n        //if (window != window.top)\n        //    $(\'<link href="\' + galaxy_config.root + \'static/style/galaxy.frame.masthead.css" rel="stylesheet">\').appendTo(\'head\');\n\n        // console protection\n        window.console = window.console || {\n            log     : function(){},\n            debug   : function(){},\n            info    : function(){},\n            warn    : function(){},\n            error   : function(){},\n            assert  : function(){}\n        };\n\n')
        # SOURCE LINE 88
        __M_writer(u'        require.config({\n            baseUrl: "')
        # SOURCE LINE 89
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n            shim: {\n                "libs/underscore": { exports: "_" },\n                "libs/backbone/backbone": { exports: "Backbone" }\n            }\n        });\n    </script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


