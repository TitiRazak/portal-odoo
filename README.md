# PARTNER DATA IMPORT Module for Odoo

## Overview
The PARTNER DATA IMPORT module enhances Odoo's data import capabilities, focusing on managing partner data imports. It integrates with the `sale`, `portal`, and `point_of_sale` modules to provide a comprehensive solution for partner data management.

## Features
- **Currency Management**: Assign a currency to partners directly from the partner form.
- **Sales Data Tracking**: Keep track of historical sales values and counts, and compute current sales totals and counts.
- **Badge System**: Implement a badge system based on sales values, awarding partners with 'Waterman/women' or 'Roi/reine du spot' badges.
- **Integration with POS and Sales**: Link with `sale.order` and `pos.order` to compute sales-related data.
- **Portal Layout Customization**: Display partner badges in the portal layout.
- **View Customizations**: Enhance partner views to include sales values, counts, and badges.
- **Search Filters**: Add custom search filters for partners based on their badge status.
- **Sale Report Enhancements**: Integrate the badge system into the sale report for better tracking and analysis.

## Installation
To install this module:
1. Clone the repository into your Odoo addons directory.
2. Update the module list within Odoo.
3. Navigate to Apps and search for 'PARTNER DATA IMPORT'. Click 'Install' to proceed with the installation.

## Dependencies
This module depends on the following Odoo modules:
- `base`
- `sale`
- `portal`
- `point_of_sale`

Ensure these modules are installed and operational before installing the PARTNER DATA IMPORT module.

## Usage
After installation, the module will automatically add new fields to the `res.partner` model. The badge system and sales values will be updated based on the specified criteria within the code. The module also includes XML changes that customize the portal layout and partner views to display the new fields and badges.

## Assets
The module includes JavaScript and XML assets that are loaded into the Point of Sale and web assets.

## License
This module is licensed under the LGPL-3 license.

## Support
For support, please open an issue in the repository or contact the module maintainer.

## Contributing
Contributions are welcome. Please fork the repository, make your changes, and submit a pull request for review.

