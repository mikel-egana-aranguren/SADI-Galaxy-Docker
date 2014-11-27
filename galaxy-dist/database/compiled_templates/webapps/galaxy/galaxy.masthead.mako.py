# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417014200.215938
_template_filename=u'templates/webapps/galaxy/galaxy.masthead.mako'
_template_uri=u'/webapps/galaxy/galaxy.masthead.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['load', 'get_user_json']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 125
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_load(context,active_view=None):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        bool = context.get('bool', UNDEFINED)
        def get_user_json():
            return render_get_user_json(context)
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n    ')
        # SOURCE LINE 33

        ## get configuration
        masthead_config = {
            ## inject configuration
            'brand'                     : app.config.get("brand", ""),
            'nginx_upload_path'         : app.config.get("nginx_upload_path", h.url_for(controller='api', action='tools')),
            'use_remote_user'           : app.config.use_remote_user,
            'remote_user_logout_href'   : app.config.remote_user_logout_href,
            'enable_cloud_launch'       : app.config.get_bool('enable_cloud_launch', False),
            'lims_doc_url'              : app.config.get("lims_doc_url", "http://main.g2.bx.psu.edu/u/rkchak/p/sts"),
            'biostar_url'               : app.config.biostar_url,
            'biostar_url_redirect'      : h.url_for( controller='biostar', action='biostar_redirect', qualified=True ),
            'support_url'               : app.config.get("support_url", "http://wiki.galaxyproject.org/Support"),
            'search_url'                : app.config.get("search_url", "http://galaxyproject.org/search/usegalaxy/"),
            'mailing_lists'             : app.config.get("mailing_lists", "http://wiki.galaxyproject.org/MailingLists"),
            'screencasts_url'           : app.config.get("screencasts_url", "http://vimeo.com/galaxyproject"),
            'wiki_url'                  : app.config.get("wiki_url", "http://galaxyproject.org/"),
            'citation_url'              : app.config.get("citation_url", "http://wiki.galaxyproject.org/CitingGalaxy"),
            'terms_url'                 : app.config.get("terms_url", ""),
            'allow_user_creation'       : app.config.allow_user_creation,
            'logo_url'                  : h.url_for(app.config.get( 'logo_url', '/')),
            'is_admin_user'             : trans.user_is_admin(),
            'active_view'               : active_view,
            'ftp_upload_dir'            : app.config.get("ftp_upload_dir",  None),
            'ftp_upload_site'           : app.config.get("ftp_upload_site",  None),
            'datatypes_disable_auto'    : app.config.get_bool("datatypes_disable_auto",  False),
        
            ## user details
            'user'          : {
                'requests'  : bool(trans.user and (trans.user.requests or trans.app.security_agent.get_accessible_request_types(trans, trans.user))),
                'email'     : trans.user.email if (trans.user) else "",
                'valid'     : bool(trans.user != None),
                'json'      : get_user_json()
            }
        }
            
        
        # SOURCE LINE 68
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        __M_writer(u'    <script type="text/javascript">\n        if( !window.Galaxy ){\n            Galaxy = {};\n        }\n\n')
        # SOURCE LINE 77
        __M_writer(u'        if (window != window.top){\n            $(\'<link href="\' + galaxy_config.root + \'static/style/galaxy.frame.masthead.css" rel="stylesheet">\')\n                .appendTo(\'head\');\n        }\n\n')
        # SOURCE LINE 83
        __M_writer(u"        require([\n            'galaxy.masthead', 'galaxy.menu', 'mvc/ui/ui-modal', 'galaxy.frame', 'mvc/upload/upload-view',\n            'mvc/user/user-model',\n            'mvc/user/user-quotameter'\n        ], function( mod_masthead, mod_menu, mod_modal, mod_frame, GalaxyUpload, user, quotameter ){\n            if( !Galaxy.currUser ){\n                // this doesn't need to wait for the page being readied\n                Galaxy.currUser = new user.User(")
        # SOURCE LINE 90
        __M_writer(unicode( h.dumps( get_user_json(), indent=2 ) ))
        __M_writer(u');\n            }\n\n            $(function() {\n                // check if masthead is available\n                if (Galaxy.masthead){\n                    return;\n                }\n\n                // get configuration\n                var masthead_config = ')
        # SOURCE LINE 100
        __M_writer(unicode( h.dumps( masthead_config ) ))
        __M_writer(u";\n\n                // load global galaxy objects\n                Galaxy.masthead = new mod_masthead.GalaxyMasthead(masthead_config);\n                Galaxy.modal = new mod_modal.View();\n                Galaxy.frame = new mod_frame.GalaxyFrame();\n\n                // construct default menu options\n                Galaxy.menu = new mod_menu.GalaxyMenu({\n                    masthead: Galaxy.masthead,\n                    config: masthead_config\n                });\n                \n                // add upload plugin\n                Galaxy.upload = new GalaxyUpload(masthead_config);\n\n                // set up the quota meter (And fetch the current user data from trans)\n                // add quota meter to masthead\n                Galaxy.quotaMeter = new quotameter.UserQuotaMeter({\n                    model   : Galaxy.currUser,\n                    el      : Galaxy.masthead.$('.quota-meter-container')\n                }).render();\n            });\n        });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_user_json(context):
    context.caller_stack._push_frame()
    try:
        AssertionError = context.get('AssertionError', UNDEFINED)
        int = context.get('int', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        float = context.get('float', UNDEFINED)
        util = context.get('util', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3

        """Bootstrapping user API JSON"""
        #TODO: move into common location (poss. BaseController)
        if trans.user:
            user_dict = trans.user.to_dict( view='element', value_mapper={ 'id': trans.security.encode_id,
                                                                                 'total_disk_usage': float } )
            user_dict[ 'quota_percent' ] = trans.app.quota_agent.get_percent( trans=trans )
            users_api_controller = trans.webapp.api_controllers[ 'users' ]
            user_dict[ 'tags_used' ] = users_api_controller.get_user_tags_used( trans, user=trans.user )
            user_dict[ 'is_admin' ] = trans.user_is_admin()
        else:
            usage = 0
            percent = None
            try:
                usage = trans.app.quota_agent.get_usage( trans, history=trans.history )
                percent = trans.app.quota_agent.get_percent( trans=trans, usage=usage )
            except AssertionError, assertion:
                # no history for quota_agent.get_usage assertion
                pass
            user_dict = {
                'total_disk_usage'      : int( usage ),
                'nice_total_disk_usage' : util.nice_size( usage ),
                'quota_percent'         : percent
            }
        return user_dict
        
        
        # SOURCE LINE 28
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


