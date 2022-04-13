import re


def parser_html(html_str, open_tag_callback, data_callback, close_tag_callback):
    parser_html.open_tag_callback = open_tag_callback
    parser_html.data_callback = data_callback
    parser_html.close_tag_callback = close_tag_callback
    html_str = html_str.strip('\n').strip(' ')
    regexp = re.compile(r"(?:\s*<[^>]+>\s*)|(?:\s*</[^>]+>\s*)|(?:[^<][^<]*)")
    for val in re.findall(regexp, html_str):
        if val[0] != '<':
            parser_html.data_callback(val)
        elif val[:2] != '</':
            val = val.strip('\n').strip(' ').strip('\t')
            parser_html.open_tag_callback(val)
        else:
            val = val.strip('\n').strip(' ').strip('\t')
            parser_html.close_tag_callback(val)

setattr(parser_html, 'open_tag_callback', None)
setattr(parser_html, 'data_callback', None) # For testing
setattr(parser_html, 'close_tag_callback', None)
