# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417014200.244444
_template_filename=u'templates/galaxy_client_app.mako'
_template_uri=u'/galaxy_client_app.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['load', 'get_user_dict', 'bootstrap', 'get_user_json', 'get_config_json', 'get_config_dict']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(u'\n\n')
        # SOURCE LINE 43
        __M_writer(u'\n\n\n')
        # SOURCE LINE 60
        __M_writer(u'\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n\n')
        # SOURCE LINE 105
        __M_writer(u'\n\n')
        # SOURCE LINE 110
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_load(context,app=None,**kwargs):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'    ')
        __M_writer(unicode( self.bootstrap( **kwargs ) ))
        __M_writer(u'\n    <script type="text/javascript">\n        require([ \'require\', \'galaxy-app-base\' ], function( require, galaxy ){\n            //TODO: global...\n            window.Galaxy = new galaxy.GalaxyApp({\n                root            : \'')
        # SOURCE LINE 33
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u"',\n                //TODO: get these options from the server\n                loggerOptions   : {}\n            });\n\n")
        # SOURCE LINE 38
        if app:
            # SOURCE LINE 39
            __M_writer(u"                require([ '")
            __M_writer(unicode(app))
            __M_writer(u"' ]);\n")
            pass
        # SOURCE LINE 41
        __M_writer(u'        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_user_dict(context):
    context.caller_stack._push_frame()
    try:
        AssertionError = context.get('AssertionError', UNDEFINED)
        Exception = context.get('Exception', UNDEFINED)
        int = context.get('int', UNDEFINED)
        float = context.get('float', UNDEFINED)
        util = context.get('util', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 69
        __M_writer(u'\n')
        # SOURCE LINE 72
        __M_writer(u'    ')

        user_dict = {}
        try:
            if trans.user:
                user_dict = trans.user.to_dict( view='element',
                    value_mapper={ 'id': trans.security.encode_id, 'total_disk_usage': float } )
                user_dict[ 'quota_percent' ] = trans.app.quota_agent.get_percent( trans=trans )
        
                # tags used
                users_api_controller = trans.webapp.api_controllers[ 'users' ]
                user_dict[ 'tags_used' ] = users_api_controller.get_user_tags_used( trans, user=trans.user )
                user_dict[ 'is_admin' ] = trans.user_is_admin()
                return user_dict
        
            usage = 0
            percent = None
            try:
                usage = trans.app.quota_agent.get_usage( trans, history=trans.history )
                percent = trans.app.quota_agent.get_percent( trans=trans, usage=usage )
            except AssertionError, assertion:
                # no history for quota_agent.get_usage assertion
                pass
            return {
                'total_disk_usage'      : int( usage ),
                'nice_total_disk_usage' : util.nice_size( usage ),
                'quota_percent'         : percent
            }
        
        except Exception, exc:
            pass
        
        return user_dict
            
        
        # SOURCE LINE 104
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bootstrap(context,**kwargs):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        def get_user_dict():
            return render_get_user_dict(context)
        def get_config_dict():
            return render_get_config_dict(context)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'    ')

        kwargs.update({
            'config'    : get_config_dict(),
            'user'      : get_user_dict(),
        })
            
        
        # SOURCE LINE 13
        __M_writer(u'\n    <script type="text/javascript">\n        //TODO: global...\n')
        # SOURCE LINE 16
        for key in kwargs:
            # SOURCE LINE 17
            __M_writer(u"            ( window.bootstrapped = window.bootstrapped || {} )[ '")
            __M_writer(unicode(key))
            __M_writer(u"' ] = (\n                ")
            # SOURCE LINE 18
            __M_writer(unicode( h.dumps( kwargs[ key ], indent=( 2 if trans.debug else 0 ) )))
            __M_writer(u' );\n')
            pass
        # SOURCE LINE 20
        __M_writer(u"        define( 'bootstrapped-data', function(){\n            return window.bootstrapped;\n        });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_user_json(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def get_user_dict():
            return render_get_user_dict(context)
        __M_writer = context.writer()
        # SOURCE LINE 107
        __M_writer(u'\n')
        # SOURCE LINE 109
        __M_writer(unicode( h.dumps( get_user_dict() )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_config_json(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def get_config_dict():
            return render_get_config_dict(context)
        __M_writer = context.writer()
        # SOURCE LINE 62
        __M_writer(u'\n')
        # SOURCE LINE 64
        __M_writer(unicode( h.dumps( get_config_dict() )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_config_dict(context):
    context.caller_stack._push_frame()
    try:
        Exception = context.get('Exception', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 47
        __M_writer(u'\n')
        # SOURCE LINE 49
        __M_writer(u'    ')

        config_dict = {}
        try:
            if 'configuration' in trans.webapp.api_controllers:
                config_dict = ( trans.webapp.api_controllers[ 'configuration' ]
                    .get_config_dict( trans.app.config, trans.user_is_admin() ) )
        except Exception, exc:
            pass
            
        return config_dict
            
        
        # SOURCE LINE 59
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


