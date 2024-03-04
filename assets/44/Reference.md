# Reference

## In this article

- [REST API Developer Endpoint Reference](https://developer.wordpress.org/rest-api/reference/#rest-api-developer-endpoint-reference)
- [A Distributed API](https://developer.wordpress.org/rest-api/reference/#a-distributed-api)

[↑︎ Back to top](https://developer.wordpress.org/rest-api/reference/#wp--skip-link--target)

The WordPress REST API is organized around [REST](http://en.wikipedia.org/wiki/Representational_state_transfer), and is designed to have predictable, resource-oriented URLs and to use HTTP response codes to indicate API errors. The API uses built-in HTTP features, like HTTP authentication and HTTP verbs, which can be understood by off-the-shelf HTTP clients, and supports cross-origin resource sharing to allow you to interact securely with the API from a client-side web application.

The REST API uses JSON exclusively as the request and response format, including error responses. While the REST API does not completely conform to the [HAL standard](http://stateless.co/hal_specification.html), it does implement HAL’s `._links` and `._embedded` properties for linking API resources, and is fully discoverable via hyperlinks in the responses.

The REST API provides public data accessible to any client anonymously, as well as private data only available after [authentication](https://developer.wordpress.org/rest-api/authentication/). Once authenticated the REST API supports most content management actions, allowing you to build alternative dashboards for a site, enhance your plugins with more responsive management tools, or build complex single-page applications.

This API reference provides information on the specific endpoints available through the API, their parameters, and their response data format.

## [REST API Developer Endpoint Reference](https://developer.wordpress.org/rest-api/reference/#rest-api-developer-endpoint-reference)

| Resource                                                     | Base Route                      |
| :----------------------------------------------------------- | :------------------------------ |
| [Posts](https://developer.wordpress.org/rest-api/reference/posts/) | `/wp/v2/posts`                  |
| [Post Revisions](https://developer.wordpress.org/rest-api/reference/post-revisions/) | `/wp/v2/posts/<id>/revisions`   |
| [Categories](https://developer.wordpress.org/rest-api/reference/categories/) | `/wp/v2/categories`             |
| [Tags](https://developer.wordpress.org/rest-api/reference/tags/) | `/wp/v2/tags`                   |
| [Pages](https://developer.wordpress.org/rest-api/reference/pages/) | `/wp/v2/pages`                  |
| [Page Revisions](https://developer.wordpress.org/rest-api/reference/page-revisions/) | `/wp/v2/pages/<id>/revisions`   |
| [Comments](https://developer.wordpress.org/rest-api/reference/comments/) | `/wp/v2/comments`               |
| [Taxonomies](https://developer.wordpress.org/rest-api/reference/taxonomies/) | `/wp/v2/taxonomies`             |
| [Media](https://developer.wordpress.org/rest-api/reference/media/) | `/wp/v2/media`                  |
| [Users](https://developer.wordpress.org/rest-api/reference/users/) | `/wp/v2/users`                  |
| [Post Types](https://developer.wordpress.org/rest-api/reference/post-types/) | `/wp/v2/types`                  |
| [Post Statuses](https://developer.wordpress.org/rest-api/reference/post-statuses/) | `/wp/v2/statuses`               |
| [Settings](https://developer.wordpress.org/rest-api/reference/settings/) | `/wp/v2/settings`               |
| [Themes](https://developer.wordpress.org/rest-api/reference/themes/) | `/wp/v2/themes`                 |
| [Search](https://developer.wordpress.org/rest-api/reference/search-results/) | `/wp/v2/search`                 |
| [Block Types](https://developer.wordpress.org/rest-api/reference/block-types/) | `/wp/v2/block-types`            |
| [Blocks](https://developer.wordpress.org/rest-api/reference/blocks/) | `/wp/v2/blocks`                 |
| [Block Revisions](https://developer.wordpress.org/rest-api/reference/block-revisions/) | `/wp/v2/blocks/<id>/autosaves/` |
| [Block Renderer](https://developer.wordpress.org/rest-api/reference/rendered-blocks/) | `/wp/v2/block-renderer`         |
| [Block Directory Items](https://developer.wordpress.org/rest-api/reference/block-directory-items/) | `/wp/v2/block-directory/search` |
| [Plugins](https://developer.wordpress.org/rest-api/reference/plugins/) | `/wp/v2/plugins`                |

## [A Distributed API](https://developer.wordpress.org/rest-api/reference/#a-distributed-api)

Unlike many other REST APIs, the WordPress REST API is distributed and available individually on each site that supports it. This means there is no singular API root or base to contact; instead, we have [a discovery process](https://developer.wordpress.org/rest-api/discovery/) that allows interacting with sites without prior contact. The API also exposes self-documentation at the index endpoint, or via an `OPTIONS` request to any endpoint, allowing human- or machine-discovery of endpoint capabilities.

