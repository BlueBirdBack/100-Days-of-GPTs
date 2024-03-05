# Develop

After reading the [Get Started](https://developer.chrome.com/docs/extensions/get-started) section, use this guide as an outline of extension components, their capabilities in Manifest V3 and how to combine them. First familiarize yourself with what extensions are capable of:

- [Design the user interface](https://developer.chrome.com/docs/extensions/develop#design-the-user-interface)
- [Control the browser](https://developer.chrome.com/docs/extensions/develop#control-the-browser)
- [Control the web](https://developer.chrome.com/docs/extensions/develop#control-the-web)

Then learn how to combine these features using the extensions [core concepts section](https://developer.chrome.com/docs/extensions/develop#core-concepts).

## Design the user interface

Most extensions need some kind of user interaction to work. The extensions platform provides a variety of ways to add interactions to your extension. These methods include popups triggered from the Chrome toolbar, side panels, context menus, and more.

### [Side panel](https://developer.chrome.com/docs/extensions/reference/api/sidePanel)

Use the `chrome.sidePanel` API to host content in the browser's side panel alongside the main content of a web page.

### [Action](https://developer.chrome.com/docs/extensions/reference/api/action)

Control the display of an extension's icon in the toolbar.

### [Menus](https://developer.chrome.com/docs/extensions/reference/api/contextMenus)

Add items to Google Chrome's context menu.



[Show more](https://developer.chrome.com/docs/extensions/develop/ui)

## Control the browser

Chrome's extension APIs make it possible to change the way your browser works.

### Override Chrome pages and settings

[Settings overrides](https://developer.chrome.com/docs/extensions/reference/manifest/chrome-settings-override) are a way for extensions to override selected Chrome settings. Additionally, extensions can use HTML [override pages](https://developer.chrome.com/docs/extensions/develop/ui/override-chrome-pages) to replace a page Google Chrome normally provides. An extension can override the bookmark manager, the history tab, or the new tab.

### Extending DevTools

DevTools extensions [add functionality to Chrome DevTools](https://developer.chrome.com/docs/extensions/how-to/devtools/extend-devtools) by accessing DevTools-specific extension APIs through a DevTools page added to the extension. You can also use the [`chrome.debugger`](https://developer.chrome.com/docs/extensions/reference/api/debugger) API to invoke Chrome's remote debugging protocol. Attach to one or more tabs to instrument network interaction, debug JavaScript, mutate the DOM, and more.

### Display notifications

The [`chrome.notifications`](https://developer.chrome.com/docs/extensions/how-to/ui/notifications) API lets you create notifications using templates and show these notifications to users in the user's system tray.

### Manage history

Use the [`chrome.history`](https://developer.chrome.com/docs/extensions/reference/api/history) API to interact with the browser's record of visited pages, and the [`chrome.browsingData`](https://developer.chrome.com/docs/extensions/reference/api/browsingData) API to manage other browsing data. Use [`chrome.topSites`](https://developer.chrome.com/docs/extensions/reference/api/topSites) to access the most visited sites.

### Control tabs and windows

Use APIs such as [`chrome.tabs`](https://developer.chrome.com/docs/extensions/reference/api/tabs), [`chrome.tabGroups`](https://developer.chrome.com/docs/extensions/reference/api/tabGroups) and [`chrome.windows`](https://developer.chrome.com/docs/extensions/reference/api/windows) to create, modify, and arrange the user's browser.

### Add keyboard shortcuts

Use the [`chrome.commands`](https://developer.chrome.com/docs/extensions/reference/api/commands) API to add keyboard shortcuts that trigger actions in your extension. For example, you can add a shortcut to open the browser action or send a command to the extension.

### Authenticate users

Use the [`chrome.identity`](https://developer.chrome.com/docs/extensions/reference/api/identity) API to get OAuth 2.0 access tokens.

### Manage extensions

The [`chrome.management`](https://developer.chrome.com/docs/extensions/reference/api/management) API provides ways to manage the list of extensions that are installed and running. It is particularly useful for extensions that override the built-in New Tab page.

### Provide suggestions

The [`chrome.omnibox`](https://developer.chrome.com/docs/extensions/reference/api/omnibox) API allows you to register a keyword with Google Chrome's omnibox (address bar).

### Update Chrome settings

Use the [`chrome.privacy`](https://developer.chrome.com/docs/extensions/reference/api/privacy) API to control usage of features in Chrome that can affect a user's privacy. Also see the [`chrome.proxy`](https://developer.chrome.com/docs/extensions/reference/api/privacy) API to manage Chrome's proxy settings.

### Manage downloads

Use the [`chrome.downloads`](https://developer.chrome.com/docs/extensions/reference/api/downloads) API to programmatically initiate, monitor, manipulate, and search for downloads.

### Use bookmarks and the reading list

Use the [`chrome.bookmarks`](https://developer.chrome.com/docs/extensions/reference/api/bookmarks) API and the [`chrome.readingList`](https://developer.chrome.com/docs/extensions/reference/api/readingList) API to create, organize, and otherwise manipulate these lists.

## Control the web

Dynamically change the content and behavior of web pages. You can control and modify the web by injecting scripts, intercepting network requests, and using web APIs to interact with web pages.

### Inject JavaScript and CSS

[Content scripts](https://developer.chrome.com/docs/extensions/develop/concepts/content-scripts) are files that run in the context of web pages. They use the standard Document Object Model (DOM), to read details of web pages the browser visits, make changes to them, and pass information to their parent extension.

### Access the active tab

The [`"activeTab"`](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab) permission gives an extension temporary access to the currently active tab when the user invokes the extension, for example by clicking its action. Access to the tab lasts while the user is on that page, and is revoked when the user navigates away or closes the tab.

### Control web requests

Use the [`chrome.declarativeNetRequest`](https://developer.chrome.com/docs/extensions/reference/api/declarativeNetRequest), [`chrome.webRequest`](https://developer.chrome.com/docs/extensions/reference/api/webRequest) and [`chrome.webNavigation`](https://developer.chrome.com/docs/extensions/reference/api/webNavigation) APIs to observe, block, and modify network requests.

### Audio recording and screen capture

Learn about different approaches for [recording audio and video from a tab, window, or screen](https://developer.chrome.com/docs/extensions/how-to/web-platform/screen-capture) using web platform APIs such as `chrome.tabCapture` or `getDisplayMedia()`.

### Modify website settings

Use the [`chrome.contentSettings`](https://developer.chrome.com/docs/extensions/reference/api/contentSettings) API to control whether websites can use features such as cookies, JavaScript, and plugins. More generally speaking, content settings allow you to customize Chrome's behavior on a per-site basis instead of globally.

## Core concepts

Using web platform and extension APIs you can build more complex features by combining different UI components and extension platform features.

### [Service workers](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers)

An extension service worker (service-worker.js) is an event-based script that the browser runs in the background. It is often used to process data, coordinate tasks in different parts of an extension, and as an extension's event manager.

### [Permissions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions)

Understand permissions: how they work and when to avoid asking for them when they're not needed.

### [Messaging](https://developer.chrome.com/docs/extensions/develop/concepts/messaging)

Many times content scripts, or other extension pages, need to send or receive information from the extension service worker. In these cases, either side can listen for messages sent from the other end, and respond on the same channel.

### [Native messaging](https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging)

Enable your extensions to exchange messages with native applications.

### [Avoid remotely hosted code](https://developer.chrome.com/docs/extensions/develop/migrate/improve-security)

In Manifest V3 extensions need to bundle all code they are using inside the extension itself. There are different strategies for doing this.

### [Storage](https://developer.chrome.com/docs/extensions/develop/concepts/storage-and-cookies)

Chrome Extensions have a specialized Storage API, available to all extension components. It includes four separate storage areas for specific use cases and an event listener that tracks whenever data is updated.

### [Offscreen documents](https://developer.chrome.com/docs/extensions/reference/api/offscreen)

Service workers don't have DOM access. The Offscreen API allows the extension to use DOM APIs in a hidden document without interrupting the user experience by opening new windows or tabs.

### [Cross origin isolation](https://developer.chrome.com/docs/extensions/develop/concepts/cross-origin-isolation)

Cross-origin isolation enables a web page to use powerful features such as `SharedArrayBuffer`. An extension can opt into cross-origin isolation by specifying the appropriate values for the `"cross_origin_embedder_policy"` and `"cross_origin_opener_policy"` manifest keys.

## More topics



### Security and privacy

- [Stay secure](https://developer.chrome.com/docs/extensions/develop/security-privacy/stay-secure)
- [Protect user privacy](https://developer.chrome.com/docs/extensions/develop/security-privacy/user-privacy)



### Migrate to Manifest V3

- #### [What is Manifest V3?](https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3)

- #### [Manifest V3 rollout timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline)

- #### [Migration guide](https://developer.chrome.com/docs/extensions/develop/migrate)

