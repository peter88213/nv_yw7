[Project home page](../) > Changelog

------------------------------------------------------------------------

## Changelog


### Version 5.3.0

- Disabling the yw7 export when the project is locked.

API: 5.18
Based on novelibre 5.25.1


### Version 5.2.0

- Providing online help via the "Help" menu.

API: 5.18
Based on novelibre 5.23.0


### Version 5.1.1

- Fix a bug where the **File > New > Create from yw7...** command cannot be properly aborted.

API: 5.18
Based on novelibre 5.18.0


### Version 5.1.0

- Updated the messaging.
- Refactored the code, changing the import order.

API: 5.17
Based on novelibre 5.17.3

### Version 5.0.2

Library update:
- Refactor the code for better maintainability.

API: 5.0
Based on novelibre 5.0.28

### Version 4.3.0

- Use the new  notification prefix for the "Action canceled by user" message.

Compatibility: novelibre 4.12 API
Based on novxlib 4.8.0

### Version 4.2.13

- Refactor the code.

Compatibility: novelibre 4.3 API
Based on novxlib 4.6.7

### Version 4.2.12

- Refactor the XmlFixer code.
- Rename the project library to match the general schema.

Compatibility: novelibre 4.3 API
Based on novxlib 4.6.4

### Version 4.2.11

- Fixing overlapping strong and italic formatting. 

Compatibility: novelibre 4.3 API
Based on novxlib 4.6.4

### Version 4.2.10

- Fix a regression from version 4.2.9 where loading files saved with yWriter raises an exception.

Compatibility: novelibre 4.3 API
Based on novxlib 4.6.4

### Version 4.2.9

- Fix a bug where "boolean" custom fields written with "novelyst" cannot be read. 

Compatibility: novelibre 4.3 API
Based on novxlib 4.6.4

### Version 4.2.8

- Refactor: Change import order for a quick start.

Compatibility: novelibre 4.3 API
Based on novxlib 4.6.3

### Version 4.2.7

- Reading and parsing utf-16 encoded .yw7 files where the XML header doesn't
indicate the right encoding (iOS yWriter issue).

Compatibility: novelibre 4.3 API
Based on novxlib 4.6.3

### Version 4.2.6

- Use new routine for safe XML reading.

Compatibility: novelibre 4.3 API
Based on novxlib 4.6.2

### Version 4.2.5

- Refactor for future Python versions.
- Update changelog for semantic versioning.

Compatibility: novelibre 4.3 API
Based on novxlib 4.5.9

### Version 4.2.4

- Refactor for future Python versions.
- Update changelog for semantic versioning.

Compatibility: novelibre 4.3 API
Based on novxlib 4.5.8

### Version 4.2.3

- Refactor localization.

Compatibility: novelibre 4.3 API
Based on novxlib 4.4.0

### Version 4.2.2

- Library update.

Compatibility: novelibre 4.3 API
Based on novxlib 4.3.0

### Version 4.2.1

- Refactor the code for future API update,
  making the prefs argument of the Plugin.install() method optional.

Compatibility: novelibre 4.3 API
Based on novxlib 4.1.0

### Version 4.2.0

- Refactor the code for better maintainability.

Compatibility: novelibre 4.3 API
Based on novxlib 4.1.0

### Version 4.1.0

- Library update. Now reading and writing *.novx* version 1.4 files.
- Use factory methods and getters from the model's NvService object.

Compatibility: novelibre 4.1 API
Based on novxlib 4.0.1

### Version 3.0.3

- Indent the novx files up to the content paragraph level, but not inline elements within paragraphs.

Based on novxlib 3.5.2

### Version 3.0.2

- Fix a bug where single spaces between emphasized text in section content are lost when writing novx files.

Based on novxlib 3.5.0

### Version 3.0.1

- Replace the novx_to_yw7 module with novxlib.novx_to_shortcode.

Based on novxlib 3.0.0
Compatibility: novelibre 3.0 API

### Version 3.0.0

- Move the yw7 file format support from novxlib to here.
- Refactor the code for v3.0 API.

Based on novxlib 2.0.0
Compatibility: novelibre 3.0 API

### Version 2.1.1

- Move the menu entry above "Options".

Based on novxlib 1.4.2
Compatibility: novelibre 2.7 API

### Version 2.1.0

Update for "novelibre".

Based on novxlib 1.1.0

### Version 2.0.0

Preparations for renaming the application:
- Refactor the code for v2.0 API.
- Change the installation directory in the setup script.

Based on novxlib 1.1.0
Compatibility: noveltree 2.0 API

### Version 1.1.0

- Re-structure the website; adjust links.

Based on novxlib 1.1.0
Compatibility: noveltree 1.8 API

### Version 1.0.2

- Fix the plugin URL constant to enable update checking.

Based on novxlib 1.0.0
Compatibility: noveltree 1.0 API

### Version 1.0.1

- Fix the plugin API version constant.

Based on novxlib 1.0.0
Compatibility: noveltree 1.0 API

### Version 1.0.0

- Release under the GPLv3 license.

Based on novxlib 1.0.0
Compatibility: noveltree 1.0 API
