import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def hcap_blog_url(lang):
    '''Returns the url for the HCAP blog site.'''

    if lang == 'el':
        lang = ''
    else:
        lang = lang + '/'

    return 'https://data.hcap.gr/' + lang

class CpThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'cp_theme')


    # IRoutes

    def before_map(self, map):

        # Redirect the home-page to datasets page
        map.redirect('/', '/dataset', _redirect_code='301 Moved Permanently')

        # Redirect the user register page to datasets page
        map.redirect('/user/register', '/dataset', _redirect_code='301 Moved Permanently')

        # Redirect the organizations page to datasets page
        map.redirect('/organization', '/dataset', _redirect_code='301 Moved Permanently')
        map.redirect('/organization/', '/dataset', _redirect_code='301 Moved Permanently')

        # Redirect the groups page to datasets page
        map.redirect('/group', '/dataset', _redirect_code='301 Moved Permanently')
        map.redirect('/group/', '/dataset', _redirect_code='301 Moved Permanently')

        return map


    # ITemplateHelpers

    def get_helpers(self):
        '''
        Register the hcap_blog_url() function above as a template
        helper function.
        '''
        return {'cp_theme_hcap_blog_url': hcap_blog_url}