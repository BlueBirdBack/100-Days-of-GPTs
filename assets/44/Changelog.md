# Changelog

## In this article

- [Version 5.6](https://developer.wordpress.org/rest-api/changelog/#version-5-6)
- [Version 5.5](https://developer.wordpress.org/rest-api/changelog/#version-5-5)
- [Version 5.4](https://developer.wordpress.org/rest-api/changelog/#version-5-4)
- [Version 5.3](https://developer.wordpress.org/rest-api/changelog/#version-5-3)
- [Version 5.2](https://developer.wordpress.org/rest-api/changelog/#version-5-2)
- [Version 5.1](https://developer.wordpress.org/rest-api/changelog/#version-5-1)
- [Version 5.0](https://developer.wordpress.org/rest-api/changelog/#version-5-0)
- [Version 4.9.8](https://developer.wordpress.org/rest-api/changelog/#version-4-9-8)
- [Version 4.8.1](https://developer.wordpress.org/rest-api/changelog/#version-4-8-1)
- [Version 4.8.0](https://developer.wordpress.org/rest-api/changelog/#version-4-8-0)
- [Version 4.7.4](https://developer.wordpress.org/rest-api/changelog/#version-4-7-4)
- [Version 4.7.3](https://developer.wordpress.org/rest-api/changelog/#version-4-7-3)
- [Version 4.7.2](https://developer.wordpress.org/rest-api/changelog/#version-4-7-2)
- [Version 4.7.1](https://developer.wordpress.org/rest-api/changelog/#version-4-7-1)

This document details changes to the WP REST API since its public release in version 4.7.0.

## [Version 5.6](https://developer.wordpress.org/rest-api/changelog/#version-5-6)

- Introduce Application Passwords for API authentication. [r49109](https://core.trac.wordpress.org/changeset/49109)
- Introduce Batch Requests. [r49252](https://core.trac.wordpress.org/changeset/49252)
- Support a route-level validation callback. [r48945](https://core.trac.wordpress.org/changeset/48945)
- Move Site Health async tests to the REST API. [r49154](https://core.trac.wordpress.org/changeset/49154)
- Add a hook to fire once a post, its terms and meta update. [r49172](https://core.trac.wordpress.org/changeset/49172)
- Introduce search term handler. [r49103](https://core.trac.wordpress.org/changeset/49103)
- Introduce search post format handler. [r49132](https://core.trac.wordpress.org/changeset/49132)
- Allow for string ids in the search controller. [r49088](https://core.trac.wordpress.org/changeset/49088)
- Support a broader range of JSON media types. [r49329](https://core.trac.wordpress.org/changeset/49329)
- Support the `multipleOf` JSON Schema keyword. [r49063](https://core.trac.wordpress.org/changeset/49063)
- Support the `minProperties` and `maxProperties` JSON Schema keywords. [r49053](https://core.trac.wordpress.org/changeset/49053)
- Support the `patternProperties` JSON Schema keyword. [r49082](https://core.trac.wordpress.org/changeset/49082)
- Support the `anyOf` and `oneOf` JSON Schema keywords. [r49246](https://core.trac.wordpress.org/changeset/49246)
- Make sure all supported JSON Schema keywords are output in the index. [r49257](https://core.trac.wordpress.org/changeset/49257)
- Add HTTP/1.1 emulation to `wp.apiRequest`. [r49133](https://core.trac.wordpress.org/changeset/49133)
- Include a JSON `Accept` header in `wp.apiRequest`. [r49716](https://core.trac.wordpress.org/changeset/49716)
- Don’t validate the post status if it hasn’t changed. [r49302](https://core.trac.wordpress.org/changeset/49302)
- Support generating comment up links to custom posts controllers. [r49299](https://core.trac.wordpress.org/changeset/49299)

## [Version 5.5](https://developer.wordpress.org/rest-api/changelog/#version-5-5)

- Introduce Block Types endpoint. [r48173](https://core.trac.wordpress.org/changeset/48173)
- Introduce Plugins and Block Directory endpoints. [r48242](https://core.trac.wordpress.org/changeset/48242)
- Introduce Image Editor endpoint. [r48291](https://core.trac.wordpress.org/changeset/48291)
- Add additional fields to the Themes endpoint. [r47921](https://core.trac.wordpress.org/changeset/47921)
- Introduce `register_theme_feature()` API for use in the Themes endpoint. [r48171](https://core.trac.wordpress.org/changeset/48171)
- Allow POST requests to the Block Renderer endpoint. [r47756](https://core.trac.wordpress.org/changeset/47756)
- Register only a single Block Renderer endpoint shared by all block types. [r48069](https://core.trac.wordpress.org/changeset/48069)
- Add support for classic embeds to the oEmbed endpoint. [r48135](https://core.trac.wordpress.org/changeset/48135)
- Link to the REST route for the currently queried resource. [r48273](https://core.trac.wordpress.org/changeset/48273)
- Introduce support for default metadata values. [r48402](https://core.trac.wordpress.org/changeset/48402)
- Add the `Link` header to the list of exposed cors headers. [48112](https://core.trac.wordpress.org/changeset/48112)
- Add `Content-Disposition`, `Content-MD5` and `X-WP-Nonce` as allowed cors headers. [r48452](https://core.trac.wordpress.org/changeset/48452)
- Improve multi-type JSON Schema support. [r48306](https://core.trac.wordpress.org/changeset/48306)
- Only validate the `format` keyword if the `type` is a `string`. [r48300](https://core.trac.wordpress.org/changeset/48300)
- Support the `uuid` JSON Schema format. [47753](https://core.trac.wordpress.org/changeset/47753)
- Support the `hex-color` JSON Schema format. [r47450](https://core.trac.wordpress.org/changeset/47450)
- Support the `pattern` JSON Schema keyword. [r47810](https://core.trac.wordpress.org/changeset/47810)
- Support the `minItems`, `maxItems`, and `uniqueItems` JSON Schema keywords. [r47923](https://core.trac.wordpress.org/changeset/47923) [r48357](https://core.trac.wordpress.org/changeset/48357)
- Support the `minLength` and `maxLength` JSON Schema keywords. [r47627](https://core.trac.wordpress.org/changeset/47627)
- Check required properties are provided when validating an object. [r47809](https://core.trac.wordpress.org/changeset/47809)
- Support more JSON Schemas when filtering a response by context. [r47758](https://core.trac.wordpress.org/changeset/47758)
- Handle parameter types consistently within `WP_REST_Request::set_param()`. [r47559](https://core.trac.wordpress.org/changeset/47559)
- Deprecate back-filling of the `HTTP_RAW_POST_DATA` global variable. [r47926](https://core.trac.wordpress.org/changeset/47926)
- Issue a `_doing_it_wrong` when registering a route without a `permission_callback`. [r48526](https://core.trac.wordpress.org/changeset/48526)
- Issue a `_doing_it_wrong` when using the `wp_send_json()` family of functions during a REST API request. [r48361](https://core.trac.wordpress.org/changeset/48361)
- Ensure `rest_ensure_response()` upgrades `WP_HTTP_Response` to `WP_REST_Response`. [r47849](https://core.trac.wordpress.org/changeset/47849)
- Only force the main query to be `is_home()` during a REST API request. [r48053](https://core.trac.wordpress.org/changeset/48053)
- Ensure all keywords supported by the JSON Schema validator are permitted by `WP_REST_Controller::get_endpoint_args_for_item_schema()`. [r47911](https://core.trac.wordpress.org/changeset/47911)
- Ensure deprecation notices are triggered when preloading REST API data. [r48150](https://core.trac.wordpress.org/changeset/48150)
- See [REST API changes in WordPress 5.5](https://make.wordpress.org/core/2020/07/22/rest-api-changes-in-wordpress-5-5/) for further commentary.

## [Version 5.4](https://developer.wordpress.org/rest-api/changelog/#version-5-4)

- Introduce selective link embedding. [r47224](https://core.trac.wordpress.org/changeset/47224)
- Fix PHP warning in the comments controller if the commented-upon post type does not exist. [r47036](https://core.trac.wordpress.org/changeset/47036]
- Add `_doing_it_wrong` warning when registering an “array” setting without an items schema. [r47325](https://core.trac.wordpress.org/changeset/47325)
- Correctly infer empty objects passed via query parameters. [r47362](https://core.trac.wordpress.org/changeset/47362)
- Add a “tax_relation” parameter to the posts collection. [r46646](https://core.trac.wordpress.org/changeset/46646)
- Allow meta to be set when creating a new media record via REST. [r47261](https://core.trac.wordpress.org/changeset/47261)
- Permit access to the themes controller if the user can edit any post type. [r47361](https://core.trac.wordpress.org/changeset/47361).
- Add support for the `REDIRECT_HTTP_AUTHORIZATION` header. [r47239](https://core.trac.wordpress.org/changeset/47239)
- Add support for filtering the posts controller’s schema. [r47265](https://core.trac.wordpress.org/changeset/47265)
- Add `_doing_it_wrong` warning if a taxonomy’s specified `rest_base` is already in use by a different resource. [r47037](https://core.trac.wordpress.org/changeset/47037)
- Improve routing performance by matching REST API routes on namespace before performing regex checks. [r47260](https://core.trac.wordpress.org/changeset/47260)
- Don’t assume all item schemas have properties. [r47328](https://core.trac.wordpress.org/changeset/47328)
- Imrove performance by reusing previously-generated embedded objects when building collection response. [r47138](https://core.trac.wordpress.org/changeset/47138)
- List all core theme feature support details in `/themes` endpoint response. [r47258](https://core.trac.wordpress.org/changeset/47528)
- Fix links format in `OPTIONS` requests for non-variable routes. [r47326](https://core.trac.wordpress.org/changeset/47326)
- Apply all relevant block rendering filters when rendering block previews. [r47360](https://core.trac.wordpress.org/changeset/47360)

## [Version 5.3](https://developer.wordpress.org/rest-api/changelog/#version-5-3)

- Cache results of `get_item_schema` on controller instances for performance. [r45811](https://core.trac.wordpress.org/changeset/45811)
- Permit embedding of the `self` link relation in the search endpoint. [r46434](https://core.trac.wordpress.org/changeset/46434)
- Pass `null` as the post date property to reset post to initial “floating” date value. [r46249](https://core.trac.wordpress.org/changeset/46249)
- Prevent deletion of post revisions. [r45812](https://core.trac.wordpress.org/changeset/45812)
- Do not send response body if status is `204` or body is `null`. [r45809](https://core.trac.wordpress.org/changeset/45809)
- Support `object` and `array` types in `register_meta()` schemas. [r45807](https://core.trac.wordpress.org/changeset/45807)
- Support dot.nested hierarchical properties in `_fields` query parameter. [r46184](https://core.trac.wordpress.org/changeset/46184)
- Return term resources in `edit` context after `PUT` or `POST` request. [r46098](https://core.trac.wordpress.org/changeset/46098)
- Introduce `date_floating` property on status endpoint response objects. [r46252](https://core.trac.wordpress.org/changeset/46252)

## [Version 5.2](https://developer.wordpress.org/rest-api/changelog/#version-5-2)

- Fix undefined property notice when setting parent term to 0. [r44965](https://core.trac.wordpress.org/changeset/44965)
- Remove unused `validate_user_can_query_private_statuses()` attachments controller method. [r44934](https://core.trac.wordpress.org/changeset/44934)
- Ensure “Allow” header is returned for OPTIONS requests. [r44933](https://core.trac.wordpress.org/changeset/44933)
- Always pass query arguments through `urlencode_deep()` in `get_items()` methods to ensure they are encoded correctly. [r45267](https://core.trac.wordpress.org/changeset/45267)

## [Version 5.1](https://developer.wordpress.org/rest-api/changelog/#version-5-1)

- Introduce `rest_post_search_query` filter to allow query arguments to be manipulated for a post search query. [r44482](https://core.trac.wordpress.org/changeset/44482)
- Allow changing of letter casing in user email addresses. [r44641](https://core.trac.wordpress.org/changeset/44641)
- Trigger a `_doing_it_wrong()` warning if `register_rest_route()` is called before the `rest_api_init` hook. [r44568](https://core.trac.wordpress.org/changeset/44568)

## [Version 5.0](https://developer.wordpress.org/rest-api/changelog/#version-5-0)

- New Routes & Endpoints
  - Introduce `wp/v2/search` route implementing a new `WP_REST_Search_Controller`. Search types are handled by extending `WP_REST_Search_Handler`, and the active search type may be filtered using the `wp_rest_search_handlers` filter. [#39965](https://core.trac.wordpress.org/ticket/39965)
  - Introduce `wp/v2/blocks` route to retrieve individual reusable blocks. Requires authentication. [#45098](https://core.trac.wordpress.org/ticket/45098)
  - Introduce autosaves endpoints for all post types except `attachment`. Autosaves endpoints utilize the new `WP_REST_Autosaves_Controller` class, and saves only the `id`, `title`, `post_content` and `excerpt` for a post. Autosaves are enabled even for post types which do not support revisions. Requires authentication. [#43316](https://core.trac.wordpress.org/ticket/43316)
  - Introduce `wp/v2/block-renderer/<name>` routes to return dynamically generated markup for server-rendered blocks. The `name` component of the URL is structured as `namespace/block-id`, *e.g.* `core/archives`. Requires authentication. [#45098](https://core.trac.wordpress.org/ticket/45098)
  - Introduce `wp/v2/themes` endpoint to expose supported theme features to the block editor. This endpoint only returns data for the active theme. Requires authentication. [#45016](https://core.trac.wordpress.org/ticket/45016)
  - Introduce `wp/v2/types/wp_block` endpoint to expose block labels and capabilities relating to the new hidden post type `wp_block`. [#45098](https://core.trac.wordpress.org/ticket/45098)
- Additional Changes
  - Custom taxonomies must specify `show_in_rest` as `true` to be visible in the block editor.
  - Introduce `wp_is_json_request()` function to detemine if request is expecting a JSON response, and contextually silence PHP warnings if so. [r43730](https://core.trac.wordpress.org/changeset/43730)
  - Requests to public, viewable post types specifying the `edit` context now return two additional properties, `permalink_temlate` and `generated_slug`. [r43720](https://core.trac.wordpress.org/changeset/43720)
  - Respect the `?_fields=` filter when applying custom post properties with `register_rest_field`. [r43736](https://core.trac.wordpress.org/changeset/43736)
  - Permit users with `read_private_posts` capability to query for private posts. [r43694](https://core.trac.wordpress.org/changeset/43694)
  - Declare the `unfiltered_html` capability using JSON Hyper Schema `targetSchema`. [r43682](https://core.trac.wordpress.org/changeset/43682)
  - Introduce `block_version` property on the post object to denote the presence and version of blocks within the post. [r43770](https://core.trac.wordpress.org/changeset/43770)
  - Add new `rest_after_*` action hooks that fire after all write operations have completed. [r42864](https://core.trac.wordpress.org/changeset/42864)
- See [The REST API in WordPress 5.0](https://make.wordpress.org/core/2018/12/06/the-rest-api-in-wordpress-5-0/) for further commentary.

## [Version 4.9.8](https://developer.wordpress.org/rest-api/changelog/#version-4-9-8)

- Introduce [`?_fields=` global query parameter](https://developer.wordpress.org/rest-api/using-the-rest-api/global-parameters/#_fields) to limit the properties included in response objects to a specified subset. [#38131](https://core.trac.wordpress.org/ticket/38131)
- Add an `object_subtype` argument to the `$args` parameter for `register_meta()`: this parameter allows developers to specify the object subtypes (*i.e.* specific post types or taxonomies) for which the registered meta will appear when `show_in_rest` is true. Introduce new wrapper methods `register_post_meta()` and `register_term_meta()` which are recommended instead of `register_meta` when working with post or term meta. [r43378](https://core.trac.wordpress.org/changeset/43378)

## [Version 4.8.1](https://developer.wordpress.org/rest-api/changelog/#version-4-8-1)

- Add a filter to allow modifying the response after embedded data is added. [r41093](https://core.trac.wordpress.org/changeset/41093)
- `wp-api.js` client: Correctly interpret `settings` resource as a model rather than a collection. [r41126](https://core.trac.wordpress.org/changeset/41126)
- Fix `PUT` (and other) requests for nginx servers by tweaking REST API URLs. [r41140](https://core.trac.wordpress.org/changeset/41140)

## [Version 4.8.0](https://developer.wordpress.org/rest-api/changelog/#version-4-8-0)

- Improve strings added after 4.7.0 string freeze. [r40571](https://core.trac.wordpress.org/changeset/40571), [r40606](https://core.trac.wordpress.org/changeset/40606)
- Canonicalize header names in `WP_REST_Request::remove_header()`. [r40577](https://core.trac.wordpress.org/changeset/40577)
- Allow `Origin: null` from `file:` URLs. [r40600](https://core.trac.wordpress.org/changeset/40600)
- Set global `$post` variable when preparing revisions. [r40601](https://core.trac.wordpress.org/changeset/40601)
- Include `featured_media` in embed responses. [r40602](https://core.trac.wordpress.org/changeset/40602)
- Add `author`, `modified`, and `parent` sort order options for posts. [r40605](https://core.trac.wordpress.org/changeset/40605)
- Add endpoint for proxying requests to external oEmbed providers, and use it in the media modal instead of the `parse-embed` AJAX action.  **This is the first usage of the WP REST API in `wp-admin`.** [r40628](https://core.trac.wordpress.org/changeset/40628)
- Do not set `X-WP-Deprecated*` headers as often. [r40782](https://core.trac.wordpress.org/changeset/40782)
- Avoid sending blank `Last-Modified` headers with authenticated requests. [r40805](https://core.trac.wordpress.org/changeset/40805)
- Fix changing parameters with `$request->set_param()` for some requests. [r40815](https://core.trac.wordpress.org/changeset/40815)
- In the admin area, ensure the REST API endpoint URL is forced to `https` when necessary. [r40843](https://core.trac.wordpress.org/changeset/40843)

## [Version 4.7.4](https://developer.wordpress.org/rest-api/changelog/#version-4-7-4)

- Fix another (DST-related) issue with dates of posts. [r40325](https://core.trac.wordpress.org/changeset/40325)
- Add `gmt_offset` and `timezone_string` to the base `/wp-json` response. [r40336](https://core.trac.wordpress.org/changeset/40336)
- Confirm that the parent post object of an attachment exists in `WP_REST_Posts_Controller::check_read_permission()`. [r40337](https://core.trac.wordpress.org/changeset/40337)
- Allow fetching multiple users and terms at once via the `slug` parameters of the respective endpoints. [r40426](https://core.trac.wordpress.org/changeset/40426), [r40427](https://core.trac.wordpress.org/changeset/40427)

## [Version 4.7.3](https://developer.wordpress.org/rest-api/changelog/#version-4-7-3)

- Cast revision author ID to int. [r40078](https://core.trac.wordpress.org/changeset/40078)
- Correctly serve the index with `PATH_INFO`. [r40079](https://core.trac.wordpress.org/changeset/40079)
- Include the `status` property in `view` context responses from the Posts endpoints. [r40081](https://core.trac.wordpress.org/changeset/40081)
- `wp-api.js` client: Use `_.extend` instead of `_.union` when merging objects. [r40084](https://core.trac.wordpress.org/changeset/40084)
- To prepare for a full multisite implementation [in 4.8](https://make.wordpress.org/core/2017/02/08/improving-the-rest-api-users-endpoint-for-multisite-in-4-7-3-and-4-8/), do not allow access to users from a different site. [r40111](https://core.trac.wordpress.org/changeset/40111)
- Correctly parse body parameters for `DELETE` requests. [r40113](https://core.trac.wordpress.org/changeset/40113)
- Fix multiple issues with dates of posts and comments. [r40114](https://core.trac.wordpress.org/changeset/40114), [r40115](https://core.trac.wordpress.org/changeset/40115)
- `wp-api.js` client: Fix route discovery for custom namespaces. [r40117](https://core.trac.wordpress.org/changeset/40117)
- Fix the behavior of the `sticky` posts filter when no posts are sticky. [r40136](https://core.trac.wordpress.org/changeset/40136)
- Allow setting all post formats even if they are not supported by the theme. [r40137](https://core.trac.wordpress.org/changeset/40137)

## [Version 4.7.2](https://developer.wordpress.org/rest-api/changelog/#version-4-7-2)

- Unify object access handling for simplicity. [r39957](https://core.trac.wordpress.org/changeset/39957)

## [Version 4.7.1](https://developer.wordpress.org/rest-api/changelog/#version-4-7-1)

- Treat any falsy value as `false` in `'rest_allow_anonymous_comments'`. [r39566](https://core.trac.wordpress.org/changeset/39566)
- `wp-api.js` client: Fix setup of models used by `wp.api.collections` objects. [r39604](https://core.trac.wordpress.org/changeset/39604)
- Do not error on empty JSON body. [r39609](https://core.trac.wordpress.org/changeset/39609)
- Do not include the `password` argument for the `GET /wp/v2/media` endpoint. [r39610](https://core.trac.wordpress.org/changeset/39610)
- Allow sending empty or no-op comment updates. [r39628](https://core.trac.wordpress.org/changeset/39628)
- Add support for filename search in the `GET /wp/v2/media` endpoint. [r39629](https://core.trac.wordpress.org/changeset/39629)
- Fix PHP warnings when `get_theme_support( 'post-formats' )` is not an array. [r39630](https://core.trac.wordpress.org/changeset/39630)
- Improve the `rest_*_collection_params` filter docs and fix the terms filter. [r39631](https://core.trac.wordpress.org/changeset/39631)
- Allow schema `sanitization_callback` to be set to `null` to bypass built-in sanitization. [r39642](https://core.trac.wordpress.org/changeset/39642)
- Change which users are shown in the users endpoint. [r39844](https://core.trac.wordpress.org/changeset/39844)

