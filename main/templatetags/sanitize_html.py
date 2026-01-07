import nh3

from django import template
from django.utils.safestring import mark_safe


register = template.Library()


ALLOWED_TAGS = {
    "a",
    "blockquote",
    "br",
    "code",
    "del",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "img",
    "li",
    "ol",
    "p",
    "pre",
    "span",
    "strong",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
}

ALLOWED_ATTRIBUTES = {
    "a": {
        "href",
        "title",
    },
    "img": {
        "src",
        "alt",
        "title",
        "width",
        "height",
    },
    "td": {
        "colspan",
        "rowspan",
    },
    "th": {
        "colspan",
        "rowspan",
        "scope",
    },
}

ALLOWED_URL_SCHEMES = {
    "http",
    "https",
    "mailto",
}


@register.filter
def sanitize_html(value):
    sanitized = nh3.clean(
        value or "",
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        url_schemes=ALLOWED_URL_SCHEMES,
        link_rel="noopener noreferrer",
        clean_content_tags={"script", "style"},
    )

    return mark_safe(sanitized)