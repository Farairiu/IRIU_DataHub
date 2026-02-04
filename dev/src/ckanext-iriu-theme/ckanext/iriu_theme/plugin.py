import os
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint


class IriuThemePlugin(plugins.SingletonPlugin):
    """
    IRIU DataHub Custom Theme Plugin

    This plugin provides custom theming for the IRIU DataHub including:
    - Custom logo and branding
    - Custom color scheme
    - Modified templates for header, footer, and homepage
    - Custom About page content
    - API documentation page
    - Styled tags and dataset displays
    - Bilingual support (English and French)
    """
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config_):
        # Add template directory
        toolkit.add_template_directory(config_, 'templates')

        # Add public directory for static assets (CSS, images, etc.)
        toolkit.add_public_directory(config_, 'public')

        # Add fanstatic directory for JavaScript/CSS resources
        toolkit.add_resource('fanstatic', 'iriu_theme')

    # ITemplateHelpers
    def get_helpers(self):
        """Return a dict of helper functions for templates."""
        return {
            'iriu_get_theme_config': self.get_theme_config,
            'iriu_get_featured_datasets_count': self.get_featured_datasets_count,
        }

    @staticmethod
    def get_theme_config():
        """Return theme configuration."""
        return {
            'site_title': toolkit.config.get('ckan.site_title', 'IRIU DataHub'),
            'site_description': toolkit.config.get('ckan.site_description',
                'IRIU DataHub - Open Data Platform for Research and Innovation'),
            'primary_color': '#1a5f7a',  # Deep teal
            'secondary_color': '#57c5b6',  # Light teal
            'accent_color': '#159895',  # Medium teal
            'background_color': '#f8f9fa',
            'footer_org': 'IRIU Team',
            'footer_year': '2024',
        }

    @staticmethod
    def get_featured_datasets_count():
        """Return the number of datasets to show on homepage."""
        return 4

    # ITranslation
    def i18n_directory(self):
        """Return the path to the i18n directory."""
        return os.path.join(os.path.dirname(__file__), 'i18n')

    def i18n_locales(self):
        """Return the list of locales this plugin supports."""
        return ['fr']

    def i18n_domain(self):
        """Return the gettext domain for this plugin."""
        return 'ckanext-iriu_theme'

    # IBlueprint
    def get_blueprint(self):
        """Return a Flask Blueprint for custom routes."""
        blueprint = Blueprint('iriu_theme', self.__module__)

        @blueprint.route('/api/guide')
        @blueprint.route('/api-guide')
        def api_docs():
            return toolkit.render('home/api.html')

        return blueprint
