# Dripyard Meridian (Drupal Theme)

Meridian is the latest Dripyard premium-inspired Drupal theme, built for editorial sites and creative studios that want bold typography, layered atmospheres, and a clean content-first layout.

## Highlights

- Sticky glass header with scroll anchoring
- Hero and highlighted regions tailored for launch campaigns
- Editorial node cards with typography-forward styling
- Modular regions for multi-column footers
- Lightweight behaviors with no external dependencies

## Requirements

- Drupal 10 or 11
- Base theme: `stable9`

## Installation

1. Copy the theme folder into `themes/custom/dripyard_meridian`.
2. Enable the theme in the Drupal UI or with Drush:

```bash
drush theme:enable dripyard_meridian
drush config:set system.theme default dripyard_meridian
```

## Regions

- Header
- Primary menu
- Secondary menu
- Hero
- Highlighted
- Content
- Sidebar first
- Sidebar second
- Footer primary
- Footer secondary
- Footer tertiary

## Quality Checks

```bash
python scripts/validate.py lint
python scripts/validate.py test
```

## License

MIT
