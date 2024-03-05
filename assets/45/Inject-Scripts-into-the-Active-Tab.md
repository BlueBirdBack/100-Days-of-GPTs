# Inject scripts into the active tab

Simplify the styling of the current page by clicking the extension toolbar icon.

## Overview

This tutorial builds an extension that simplifies the styling of the Chrome extension and Chrome Web Store documentation pages so that they are easier to read.

In this guide, we're going to explain how to do the following:

- Use the extension service worker as the event coordinator.
- Preserve user privacy through the `"activeTab"` permission.
- Run code when the user clicks the extension toolbar icon.
- Insert and remove a style sheet using the [Scripting](https://developer.chrome.com/docs/extensions/reference/api/scripting) API.
- Use a keyboard shortcut to execute code.

## Before you start

This guide assumes that you have basic web development experience. We recommend checking out [Hello World](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world) for an introduction to the extension development workflow.

## Build the extension

To start, create a new directory called `focus-mode` that will hold the extension's files. If you prefer, you can download the complete source code from [GitHub](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.focus-mode).

### Step 1: Add the extension data and icons

Create a file called `manifest.json` and include the following code.

```json
{
  "manifest_version": 3,
  "name": "Focus Mode",
  "description": "Enable focus mode on Chrome's official Extensions and Chrome Web Store documentation.",
  "version": "1.0",
  "icons": {
    "16": "images/icon-16.png",
    "32": "images/icon-32.png",
    "48": "images/icon-48.png",
    "128": "images/icon-128.png"
  }
}
```

To learn more about these manifest keys, check out the "Run scripts on every tab" tutorial that explains the extension's [metadata](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-on-every-tab#step-1) and [icons](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-on-every-tab#step-2) in more detail.

Create an `images` folder then [download the icons](https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.focus-mode/images) into it.

### Step 2: Initialize the extension

Extensions can monitor browser events in the background using the [extension's service worker](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers). Service workers are special JavaScript environments that handle events and terminate when they're not needed.

Start by registering the service worker in the `manifest.json` file:

```json
{
  ...
  "background": {
    "service_worker": "background.js"
  },
  ...
}
```

Create a file called `background.js` and add the following code:

```js
chrome.runtime.onInstalled.addListener(() => {
  chrome.action.setBadgeText({
    text: "OFF",
  });
});
```

The first event our service worker will listen for is [`runtime.onInstalled()`](https://developer.chrome.com/docs/extensions/reference/api/runtime#event-onInstalled). This method allows the extension to set an initial state or complete some tasks on installation. Extensions can use the [Storage API](https://developer.chrome.com/docs/extensions/reference/api/storage) and [IndexedDB](https://developer.mozilla.org/docs/Web/API/IndexedDB_API) to store the application state. In this case, though, since we're only handling two states, we will use the *action's badge* text itself to track whether the extension is 'ON' or 'OFF'.

**Key term:** The [action's badge](https://developer.chrome.com/docs/extensions/reference/api/action#badge) is a colored banner on top of the extension action (toolbar icon).

### Step 3: Enable the extension action

The *extension action* controls the extension's toolbar icon. So whenever the user clicks the extension icon, it will either run some code (like in this example) or display a popup. Add the following code to declare the extension action in the `manifest.json` file:

```json
{
  ...
  "action": {
    "default_icon": {
      "16": "images/icon-16.png",
      "32": "images/icon-32.png",
      "48": "images/icon-48.png",
      "128": "images/icon-128.png"
    }
  },
  ...
}
```

#### Use the activeTab permission to protect user privacy

The [`activeTab`](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab) permission grants the extension *temporary* ability to execute code on the active tab. It also allows access to [sensitive properties](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab#what-activeTab-allows) of the current tab.

This permission is enabled when the user ***invokes\*** the extension. In this case, the user invokes the extension by clicking on the extension action.

💡 **What other user interactions enable the activeTab permission in my own extension?**

- Pressing a keyboard shortcut combination.
- Selecting a context menu item.
- Accepting a suggestion from the omnibox.
- Opening an extension popup.

The `"activeTab"` permission allows users to *purposefully* choose to run the extension on the focused tab; this way, it protects the user's privacy. Another benefit is that it does not trigger a [permission warning](https://developer.chrome.com/docs/extensions/develop/concepts/permission-warnings#permissions_with_warnings).

To use the `"activeTab"` permission, add it to the manifest's permission array:

```json
{
  ...
  "permissions": ["activeTab"],
  ...
}
```

### Step 4: Track the state of the current tab

After the user clicks the extension action, the extension will check if the URL matches a documentation page. Next, it will check the state of the current tab and set the next state. Add the following code to `background.js`:

```js
const extensions = 'https://developer.chrome.com/docs/extensions'
const webstore = 'https://developer.chrome.com/docs/webstore'

chrome.action.onClicked.addListener(async (tab) => {
  if (tab.url.startsWith(extensions) || tab.url.startsWith(webstore)) {
    // Retrieve the action badge to check if the extension is 'ON' or 'OFF'
    const prevState = await chrome.action.getBadgeText({ tabId: tab.id });
    // Next state will always be the opposite
    const nextState = prevState === 'ON' ? 'OFF' : 'ON'

    // Set the action badge to the next state
    await chrome.action.setBadgeText({
      tabId: tab.id,
      text: nextState,
    });
  }
});
```

### Step 5: Add or remove the style sheet

Now it's time to change the layout of the page. Create a file named `focus-mode.css` and include the following code:

```js
body > .scaffold > :is(top-nav, navigation-rail, side-nav, footer),
main > :not(:last-child),
main > :last-child > navigation-tree,
main .toc-container {
  display: none;
}

main > :last-child {
  margin-top: min(10vmax, 10rem);
  margin-bottom: min(10vmax, 10rem);
}
```

Insert or remove the style sheet using the [Scripting](https://developer.chrome.com/docs/extensions/reference/api/scripting) API. Start by declaring the `"scripting"` permission in the manifest:

```json
{
  ...
  "permissions": ["activeTab", "scripting"],
  ...
}
```

**Success:** The Scripting API does not trigger a [permission warning](https://developer.chrome.com/docs/extensions/develop/concepts/permission-warnings#permissions_with_warnings).

Finally, in `background.js` add the following code to change the layout of the page:

```js
  ...
    if (nextState === "ON") {
      // Insert the CSS file when the user turns the extension on
      await chrome.scripting.insertCSS({
        files: ["focus-mode.css"],
        target: { tabId: tab.id },
      });
    } else if (nextState === "OFF") {
      // Remove the CSS file when the user turns the extension off
      await chrome.scripting.removeCSS({
        files: ["focus-mode.css"],
        target: { tabId: tab.id },
      });
    }
  }
});
```

💡 **Can I use the Scripting API to inject code instead of a style sheet?**

Yes. You can use [`scripting.executeScript()`](https://developer.chrome.com/docs/extensions/reference/api/scripting#injected-code) to inject JavaScript.

### *Optional: Assign a keyboard shortcut*

Just for fun, add a shortcut to make it easier to enable or disable focus mode. Add the `"commands"` key to the manifest.

```json
{
  ...
  "commands": {
    "_execute_action": {
      "suggested_key": {
        "default": "Ctrl+B",
        "mac": "Command+B"
      }
    }
  }
}
```

The `"_execute_action"` key runs the same code as the `action.onClicked()` event, so no additional code is needed.

## Test that it works

Verify that the file structure of your project looks like the following:

![The contents of the focus mode folder: manifest.json, background.js, focus-mode.css, and images folder.](https://developer.chrome.com/static/docs/extensions/get-started/tutorial/scripts-activetab/image/the-contents-the-focus-m-6e0ec866ea578.png)

### Load your extension locally

To load an unpacked extension in developer mode, follow the steps in [Hello World](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked).

### Test the extension on a documentation page

First, open any of the following pages:

- [Welcome to the Chrome Extension documentation](https://developer.chrome.com/docs/extensions)
- [Publish in the Chrome Web Store](https://developer.chrome.com/docs/webstore/publish)
- [Scripting API](https://developer.chrome.com/docs/extensions/reference/api/scripting)

Then, click the extension action. If you set up a [keyboard shortcut](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-activetab#step-6), you can test it by pressing `Ctrl + B` or `Cmd + B`.

It should go from this:

![Focus Mode extension OFF](https://developer.chrome.com/static/docs/extensions/get-started/tutorial/scripts-activetab/image/focus-mode-extension-off-dc8f9326aa92b.png)Focus Mode extension off

To this:

![Focus Mode extension ON](https://developer.chrome.com/static/docs/extensions/get-started/tutorial/scripts-activetab/image/focus-mode-extension-on-c248a59b498ea.png)Focus Mode extension on

## 🎯 Potential enhancements

Based on what you've learned today, try to accomplish any of the following:

- Improve the CSS style sheet.
- Assign a different keyboard shortcut.
- Change the layout of your favorite blog or documentation site.

## Keep building.

Congratulations on finishing this tutorial 🎉. Continue leveling up your skills by completing other tutorials on this series:

| Extension                                                    | What you will learn                                          |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [Reading time](https://developer.chrome.com/docs/extensions/get-started/tutorial/scripts-on-every-tab) | To insert an element on a specific set of pages automatically. |
| [Tabs Manager](https://developer.chrome.com/docs/extensions/get-started/tutorial/popup-tabs-manager) | To create a popup that manages browser tabs.                 |

## Continue exploring

We hope you enjoyed building this Chrome extension and are excited to continue your extension development learning journey. We recommend the following learning paths:

- The [developer's guide](https://developer.chrome.com/docs/extensions/develop) has dozens of additional links to pieces of documentation relevant to advanced extension creation.
- Extensions have access to powerful APIs beyond what's available on the open web. The [Chrome APIs documentation](https://developer.chrome.com/docs/extensions/reference/api) walks through each API.

