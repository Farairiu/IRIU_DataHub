import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class IriuThemePlugin(plugins.SingletonPlugin):
    """
    IRIU DataHub Custom Theme Plugin

    This plugin provides custom theming for the IRIU DataHub including:
    - Custom logo and branding
    - Custom color scheme
    - Modified templates for header, footer, and homepage
    - Custom About page content
    - Styled tags and dataset displays
    """
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

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
