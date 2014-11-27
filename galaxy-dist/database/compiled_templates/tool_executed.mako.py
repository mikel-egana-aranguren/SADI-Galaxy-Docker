# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1417014282.0602
_template_filename='templates/webapps/galaxy/tool_executed.mako'
_template_uri='tool_executed.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        trans = context.get('trans', UNDEFINED)
        h = context.get('h', UNDEFINED)
        tool = context.get('tool', UNDEFINED)
        len = context.get('len', UNDEFINED)
        out_data = context.get('out_data', UNDEFINED)
        job_errors = context.get('job_errors', UNDEFINED)
        num_jobs = context.get('num_jobs', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n\n<head>\n<title>Galaxy</title>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<link href="')
        # SOURCE LINE 7
        __M_writer(unicode(h.url_for('/static/style/base.css')))
        __M_writer(u'" rel="stylesheet" type="text/css" />\n<script type="text/javascript">\n  var inside_galaxy_frameset = false;\n\n  // refresh the history panel to include any new datasets created by the tool\n  if( top.Galaxy && top.Galaxy.currHistoryPanel ){\n        top.Galaxy.currHistoryPanel.refreshContents();\n  }\n\n')
        # SOURCE LINE 16
        if trans.user:  
            # SOURCE LINE 17
            __M_writer(u'      if (inside_galaxy_frameset)\n      {\n            //parent.frames.galaxy_tools.update_recently_used();\n      }\n')
            pass
        # SOURCE LINE 22
        __M_writer(u'  \n  if ( parent.handle_minwidth_hint ) {\n      parent.handle_minwidth_hint( -1 );\n  }\n\n  function main() {\n    // If called from outside the galaxy frameset, redirect there\n')
        # SOURCE LINE 29
        if tool.options.refresh:
            # SOURCE LINE 30
            __M_writer(u'      if ( ! inside_galaxy_frameset ) {\n        setTimeout( "refresh()", 1000 );\n        document.getElementById( "refresh_message" ).style.display = "block";\n      }\n')
            pass
        # SOURCE LINE 35
        __M_writer(u"  }\n\n  function refresh() {\n    top.location.href = '")
        # SOURCE LINE 38
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u'\';\n  }  \n\n</script>\n\n</head>\n\n<body onLoad="main()">\n\n<div class="donemessagelarge">\n\n')
        # SOURCE LINE 49
        if num_jobs > 1:
            # SOURCE LINE 50
            __M_writer(u'  ')
            jobs_str = "%d jobs have" % num_jobs 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['jobs_str'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            # SOURCE LINE 51
        else:
            # SOURCE LINE 52
            __M_writer(u'  ')
            jobs_str = "A job has" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['jobs_str'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 54
        if len(out_data) == 1:
            # SOURCE LINE 55
            __M_writer(u'  ')
            datasets_str = "dataset" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datasets_str'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            # SOURCE LINE 56
        else:
            # SOURCE LINE 57
            __M_writer(u'  ')
            datasets_str = "datasets" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datasets_str'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 59
        __M_writer(u'\n<p>\n  ')
        # SOURCE LINE 61
        __M_writer(unicode(jobs_str))
        __M_writer(u' been successfully added to the queue - resulting in the following ')
        __M_writer(unicode(datasets_str))
        __M_writer(u':\n</p>\n')
        # SOURCE LINE 63
        for _, data in out_data:
            # SOURCE LINE 64
            __M_writer(u'   <div style="padding: 10px"><b> ')
            __M_writer(unicode(data.hid))
            __M_writer(u': ')
            __M_writer(unicode(data.name))
            __M_writer(u'</b></div>\n')
            pass
        # SOURCE LINE 66
        __M_writer(u"\n<p>\nYou can check the status of queued jobs and view the resulting \ndata by refreshing the <b>History</b> pane. When the job has been run\nthe status will change from 'running' to 'finished' if completed \nsuccessfully or 'error' if problems were encountered.\n</p>\n\n")
        # SOURCE LINE 74
        if tool.options.refresh:
            # SOURCE LINE 75
            __M_writer(u'<p id="refresh_message" style="display: none;">You are now being redirected back to <a href="')
            __M_writer(unicode(h.url_for( '/' )))
            __M_writer(u'">Galaxy</a></div>\n')
            pass
        # SOURCE LINE 77
        __M_writer(u'\n</div>\n\n')
        # SOURCE LINE 80
        if job_errors:
            # SOURCE LINE 81
            __M_writer(u'<div class="errormessagelarge">\n  There were errors setting up ')
            # SOURCE LINE 82
            __M_writer(unicode(len(job_errors)))
            __M_writer(u' submitted job(s):\n  <ul>\n  <!-- Styling on this list is a little flat. Consider identing these error messages. -->\n')
            # SOURCE LINE 85
            for job_error in job_errors:
                # SOURCE LINE 86
                __M_writer(u'    <li><b>')
                __M_writer(unicode(job_error))
                __M_writer(u'</b></li>\n')
                pass
            # SOURCE LINE 88
            __M_writer(u'  </ul>\n</div>\n')
            pass
        # SOURCE LINE 91
        __M_writer(u'\n</body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


