# ckanext-iriu-theme

A custom CKAN theme extension for IRIU DataHub.

## Features

- Custom color scheme (teal/cyan palette)
- Modern, clean UI design
- Custom homepage with statistics
- Styled tags and dataset listings
- Custom About page
- Responsive design
- Custom footer with links

## Installation

This extension is designed to be installed in the IRIU DataHub development environment.

### For Development

1. The extension is automatically mounted in the dev container via docker-compose
2. Add `iriu_theme` to the `CKAN__PLUGINS` environment variable
3. Restart the CKAN container

### Configuration

Add to your `.env` file:

```bash
CKAN__PLUGINS=envvars iriu_theme image_view text_view recline_view datastore datapusher
CKAN_SITE_TITLE=IRIU DataHub
CKAN_SITE_LOGO=/images/iriu-logo.svg
```

## Customization

### Colors

Edit the CSS custom properties in `ckanext/iriu_theme/fanstatic/iriu-theme.css`:

```css
:root {
    --iriu-primary: #1a5f7a;      /* Main brand color */
    --iriu-secondary: #57c5b6;    /* Accent color */
    --iriu-accent: #159895;       /* Highlight color */
}
```

### Logo

Replace the logo at `ckanext/iriu_theme/public/images/iriu-logo.svg` with your own.

### Templates

Override CKAN templates by adding files to `ckanext/iriu_theme/templates/`.

## License

AGPL v3
