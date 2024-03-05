# Manifest file format

 Every extension must have a `manifest.json` file in its root directory that lists important information about the structure and behavior of that extension. This page explains the structure of extension manifests and the features they can include.

## Examples

The following example manifests show the basic manifest structure and some commonly used features as a starting point for creating your own manifest:

#### Minimal manifest

```json
{
  "manifest_version": 3,
  "name": "Minimal Manifest",
  "version": "1.0.0",
  "description": "A basic example extension with only required keys",
  "icons": {
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
}
```

#### Register a content script

```json
{
  "manifest_version": 3,
  "name": "Run script automatically",
  "description": "Runs a script on www.example.com automatically when user installs the extension",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "content_scripts": [
    {
      "js": [
        "content-script.js"
      ],
      "matches": [
        "http://*.example.com//"
      ]
    }
  ]
}
```

#### Inject a content script

```json
{
  "manifest_version": 3,
  "name": "Click to run",
  "description": "Runs a script when the user clicks the action toolbar icon.",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "background": {
    "service_worker": "service-worker.js"
  },
  "action": {
    "default_icon": {
      "16": "images/icon-16.png",
      "32": "images/icon-32.png",
      "48": "images/icon-48.png",
      "128": "images/icon-128.png"
    }
  },
  "permissions": ["scripting", "activeTab"]
}
```

#### Side panel

```json
{
  "manifest_version": 3,
  "name": "Side panel extension",
  "version": "1.0",
  "description": "Extension with a default side panel.",
  "icons": {
    "16": "images/icon-16.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "side_panel": {
    "default_path": "sidepanel.html"
  },
  "permissions": ["sidePanel"]
}
```

#### Popup with permissions

```json
{
  "manifest_version": 3,
  "name": "Popup extension that requests permissions",
  "description": "Extension that includes a popup and requests host permissions and storage permissions .",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  },
  "action": {
    "default_popup": "popup.html"
  },
  "host_permissions": [
    "https://*.example.com/"
  ],
  "permissions": [
    "storage"
  ]
}
```

## Manifest keys

The following is a list of all supported manifest keys.

### Keys required by the Extensions platform

- `"manifest_version"`

  An integer specifying the version of the manifest file format that your extension uses. The only supported value is `3`.

- `"name"`

  A string that identifies the extension in the [Chrome Web Store](https://chrome.google.com/webstore), the install dialog, and the user's Chrome Extensions page (`chrome://extensions`). The maximum length is 75 characters. For information on using locale-specific names, see [Internationalization](https://developer.chrome.com/docs/extensions/reference/api/i18n).

- `"version"`

  A string that identifies the extension's version number. For information on version number formatting, see [Version](https://developer.chrome.com/docs/extensions/reference/manifest/version).

### Keys required by Chrome Web Store

- `"description"`

  A string that describes the extension on both the Chrome Web Store and the user's extension management page. The maximum length is 132 characters. For information on localizing descriptions, see [Internationalization](https://developer.chrome.com/docs/extensions/reference/api/i18n).

- `"icons"`

  One or more icons that represent your extension. For information about best practices, see [Icons](https://developer.chrome.com/docs/extensions/reference/manifest/icons).

### Optional keys

- `"action"`

  Defines the appearance and behavior of the extension's icon in the Google Toolbar. For more information, see [`chrome.action`](https://developer.chrome.com/docs/extensions/reference/api/action).

- `"author"`

  Specifies the email address of the account that was used to create the extension.

- `"background"`

  Specifies the JavaScript file containing the extension's service worker, which acts as an event handler. For more information, see [About extension service workers](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers).

- `"chrome_settings_overrides"`

  Defines overrides for selected Chrome settings. For more information, see [Overriding Chrome settings](https://developer.chrome.com/docs/extensions/reference/manifest/chrome-settings-override).

- `"chrome_url_overrides"`

  Defines overrides for default Chrome pages. For more information, see [Override Chrome pages](https://developer.chrome.com/docs/extensions/develop/ui/override-chrome-pages).

- `"commands"`

  Defines keyboard shortcuts within the extension. For more information, see [chrome.commands](https://developer.chrome.com/docs/extensions/reference/api/commands).

- `"content_scripts"`

  Specifies JavaScript or CSS files to be used when the user opens certain web pages. For more information, see [Content scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts).

- `"content_security_policy"`

  Defines restrictions on the scripts, styles, and other resources an extension can use. For more information, see [Content security policy](https://developer.chrome.com/docs/extensions/reference/manifest/content-security-policy).

- `"cross_origin_embedder_policy"`

  Specifies a value for the Cross-Origin-Embedder-Policy HTTP header, which configures embedding of cross-origin resources in an extension page.

- `"cross_origin_opener_policy"`

  Specifies a value for the Cross-Origin-Opener-Policy HTTP header, which lets you ensure that a top-level extension page doesn't share a browsing context group with cross-origin documents.

- `"declarative_net_request"`

  Defines static rules for the [declarativeNetRequest](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest) API, which allows blocking and modifying of network requests.

- `"default_locale"`

  A string that defines the default language of an extension that supports multiple locales. Examples include "en" and "pt_BR". This key is required in localized extensions, and must not be used in extensions that aren't localized. For more information, see [Internationalization](https://developer.chrome.com/docs/extensions/reference/api/i18n).

- `"devtools_page"`

  Defines pages that use the [DevTools](https://developer.chrome.com/docs/extensions/how-to/devtools/extend-devtools) APIs.

- `"export"`

  Allows resources to be exported from the extension. For more information, see [Export](https://developer.chrome.com/docs/extensions/reference/manifest/shared-modules#export).

- `"externally_connectable"`

  Specifies what other pages and extensions can connect to your extensions. For more information, see [`"externally_connectable"`](https://developer.chrome.com/docs/extensions/reference/manifest/externally-connectable).

- `"homepage_url"`

  A string specifying a URL for the extension's homepage. If this is undefined, the homepage defaults to the extension's Chrome Web Store page. This field is particularly useful if you [host the extension](https://developer.chrome.com/docs/extensions/how-to/distribute/host-extensions) on your own site.

- `"host_permissions"`

  Lists the web pages your extension is allowed to interact with, defined using URL match patterns. User permission for these sites is requested at install time. For more information, see [Host permissions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions).

- `"import"`

  Allows resources to be imported into the extension. For more information, see [Import](https://developer.chrome.com/docs/extensions/reference/manifest/shared-modules#import).

- `"incognito"`

  Defines how the extension behaves in incognito mode. Supported values are `"spanning"`, `"split"`, and `"not_allowed"`. For more information, see [Incognito](https://developer.chrome.com/docs/extensions/reference/manifest/incognito).

- `"key"`

  Specifies your extension's ID for various development use cases. For more information, see [Key](https://developer.chrome.com/docs/extensions/reference/manifest/key).

- `"minimum_chrome_version"`

  Defines the oldest Chrome version that can install your extension. The value must be a substring of an existing Chrome browser version string, such as `"107"` or `"107.0.5304.87"`. Users with versions of Chrome older than the minimum version see a "Not compatible" warning in the Chrome Web Store, and are unable to install your extension. If you add this to an existing extension, users whose Chrome version is older won't receive automatic updates to your extension. This includes business users in [ephemeral](https://support.google.com/chrome/a/answer/3538894) mode.

- `"oauth2"`

  Allows the use of an OAuth 2.0 security ID. The value of this key must be an object with `"client_id"` and `"scopes"` properties. For details, see the [OAuth 2.0 tutorial](https://developer.chrome.com/docs/extensions/how-to/integrate/oauth).

- `"omnibox"`

  Allows the extension to register a keyword in Chrome's address bar. For more information, see [Omnibox](https://developer.chrome.com/docs/extensions/reference/api/omnibox).

- `"optional_host_permissions"`

  Declares optional [host permissions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions) for your extension.

- `"optional_permissions"`

  Declares [optional permissions](https://developer.chrome.com/docs/extensions/reference/api/permissions#step-2-declare-optional-permissions-in-the-manifest) for your extension.

- `"options_page"`

  Specifies a path to an options.html file for the extension to use as an options page. For more information, see [Give users options](https://developer.chrome.com/docs/extensions/develop/ui/options-page).

- `"options_ui"`

  Specifies a path to an HTML file that lets a user change extension options from the Chrome Extensions page. For more information, see [Embedded options](https://developer.chrome.com/docs/extensions/develop/ui/options-page#embedded_options).

- `"permissions"`

  Enables use of particular extension APIs. See [Permissions](https://developer.chrome.com/docs/extensions/reference/permissions) for a general explanation. Reference pages for individual APIs list the permissions they require.

- `"requirements"`

  Lists technologies required to use the extension. For a list of supported requirements, see [Requirements](https://developer.chrome.com/docs/extensions/reference/manifest/requirements).

- `"sandbox"`

  Defines a set of extension pages that don't have access to extension APIs or direct access to non-sandboxed pages. For more information, see [Sandbox](https://developer.chrome.com/docs/extensions/reference/manifest/sandbox).

- `"short_name"`

  A string containing a shortened version of the extension's name to be used when character space is limited. The maximum length is 12 characters. If this is undefined, a truncated version of the "name" key displays instead.

- `"side_panel"`

  Identifies an HTML file to display in a [sidePanel](https://developer.chrome.com/docs/extensions/reference/api/sidePanel).

- `"storage"`

  Declares a JSON schema for the [managed storage area](https://developer.chrome.com/docs/extensions/reference/storage#property-managed). For more information, see [Manifest for storage areas](https://developer.chrome.com/docs/extensions/reference/manifest/storage).

- `"tts_engine"`

  Registers the extension as a text to speech engine. For more information, see the [ttsEngine](https://developer.chrome.com/docs/extensions/reference/api/ttsEngine) API.

- `"update_url"`

  A string containing the URL of the extension's updates page. Use this key if you're [hosting your extension](https://developer.chrome.com/docs/extensions/how-to/distribute/host-extensions) outside the Chrome Web Store.

- `"version_name"`

  A string describing the extension's version. Examples include `"1.0 beta"` and `"build rc2"`. If this is unspecified, the "version" value displays on the extension management page instead.

- `"web_accessible_resources"`

  Defines files within the extension that can be accessed by web pages or other extensions. For more information, see [Web Accessible Resources](https://developer.chrome.com/docs/extensions/reference/manifest/web-accessible-resources).

### Optional ChromeOS keys

- `"file_browser_handlers"`

  Provides access to the [`fileBrowserHandler`](https://developer.chrome.com/docs/extensions/reference/api/fileBrowserHandler) API, which lets extensions access the ChromeOS file browser.

- `"file_handlers"`

  Specifies file types for ChromeOS extensions to handle. For more information, see [`file_handlers`](https://developer.chrome.com/docs/extensions/reference/manifest/file-handlers).

- `"file_system_provider_capabilities"`

  Allows access to the [`fileSystemProvider`](https://developer.chrome.com/docs/extensions/reference/api/fileSystemProvider) API, which lets extensions create file systems that ChromeOS can use.

- `"input_components"`

  Allows the use of the Input Method Editor API. For more information, see [`input_components`](https://developer.chrome.com/docs/extensions/reference/manifest/input-components).

