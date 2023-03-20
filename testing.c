#include <stddef.h>
#include <stdint.h>
#include <assert.h>
#include <string.h>
#include <stdio.h>

// #define SIZE_MAX 0xffffffffffffffffui64
#define H2O_STRLIT(s) (s), sizeof(s) - 1

#include "testing.h"


const h2o_url_scheme_t H2O_URL_SCHEME_HTTP = {{H2O_STRLIT("http")}, 80, 0};
const h2o_url_scheme_t H2O_URL_SCHEME_HTTPS = {{H2O_STRLIT("https")}, 443, 1};
const h2o_url_scheme_t H2O_URL_SCHEME_MASQUE = {{H2O_STRLIT("masque")}, 65535, 0 /* ??? masque might or might not be over TLS */};

size_t h2o_strtosize(const char *s, size_t len)
{
    uint64_t v = 0, m = 1;
    const char *p = s + len;

    if (len == 0)
        goto Error;

    while (1) {
        int ch = *--p;
        if (!('0' <= ch && ch <= '9'))
            goto Error;
        v += (ch - '0') * m;
        if (p == s)
            break;
        m *= 10;
        /* do not even try to overflow */
        if (m == 10000000000000000000ULL)
            goto Error;
    }

    if (v >= SIZE_MAX)
        goto Error;
    return v;

Error:
    return SIZE_MAX;
}

static h2o_iovec_t h2o_iovec_init(const void *base, size_t len)
{
    /* intentionally declared to take a "const void*" since it may contain any type of data and since _some_ buffers are constant */
    h2o_iovec_t buf;
    buf.base = (char *)base;
    buf.len = len;
    return buf;
}

const char *h2o_url_parse_hostport(const char *s, size_t len, h2o_iovec_t *host, uint16_t *port)
{
    const char *token_start = s, *token_end, *end = s + len;

    *port = 65535;

    if (token_start == end)
        return NULL;

    if (*token_start == '[') {
        /* is IPv6 address */
        ++token_start;
        if ((token_end = memchr(token_start, ']', end - token_start)) == NULL)
            return NULL;
        *host = h2o_iovec_init(token_start, token_end - token_start);
        token_start = token_end + 1;
    } else {
        for (token_end = token_start; !(token_end == end || *token_end == '/' || *token_end == ':'); ++token_end)
            ;
        *host = h2o_iovec_init(token_start, token_end - token_start);
        token_start = token_end;
    }

    /* disallow zero-length host */
    if (host->len == 0)
        return NULL;

    /* parse port */
    if (token_start != end && *token_start == ':') {
        size_t p;
        ++token_start;
        if ((token_end = memchr(token_start, '/', end - token_start)) == NULL)
            token_end = end;
        if ((p = h2o_strtosize(token_start, token_end - token_start)) >= 65535)
            return NULL;
        *port = (uint16_t)p;
        token_start = token_end;
    }

    return token_start;
}


static int parse_authority_and_path(const char *src, const char *url_end, h2o_url_t *parsed)
{
    const char *p = h2o_url_parse_hostport(src, url_end - src, &parsed->host, &parsed->_port);
    if (p == NULL)
        return -1;
    parsed->authority = h2o_iovec_init(src, p - src);
    if (p == url_end) {
        parsed->path = h2o_iovec_init(H2O_STRLIT("/"));
    } else {
        if (*p != '/')
            return -1;
        parsed->path = h2o_iovec_init(p, url_end - p);
    }
    return 0;
}

static const char *parse_scheme(const char *s, const char *end, const h2o_url_scheme_t **scheme)
{
    if (end - s >= 5 && memcmp(s, "http:", 5) == 0) {
        *scheme = &H2O_URL_SCHEME_HTTP;
        return s + 5;
    } else if (end - s >= 6 && memcmp(s, "https:", 6) == 0) {
        *scheme = &H2O_URL_SCHEME_HTTPS;
        return s + 6;
    } else if (end - s >= 7 && memcmp(s, "masque:", 7) == 0) {
        *scheme = &H2O_URL_SCHEME_MASQUE;
        return s + 7;
    }
    return NULL;
}


int h2o_url_parse(const char *url, size_t url_len, h2o_url_t *parsed)
{
    const char *url_end, *p;

    if (url_len == SIZE_MAX)
        url_len = strlen(url);
    url_end = url + url_len;

    /* check and skip scheme */
    if ((p = parse_scheme(url, url_end, &parsed->scheme)) == NULL)
        return -1;

    /* skip "//" */
    if (!(url_end - p >= 2 && p[0] == '/' && p[1] == '/'))
        return -1;
    p += 2;

    return parse_authority_and_path(p, url_end, parsed);
}

int main(){
    unsigned long long testValue = 0xFFFFFFFFFFFFFFFF;
    uint8_t *Data = &testValue;
    const char *url = (const char *)Data;
    size_t url_len;
    h2o_url_t uri;
    h2o_url_t *parsed = &uri;
    int ret;
    printf("Test\n");
    const char *url_end, *p;

    if (url_len == SIZE_MAX)
        url_len = strlen(url);
    url_end = url + url_len;

    /* check and skip scheme */
    if ((p = parse_scheme(url, url_end, &parsed->scheme)) == NULL)
        ret = -1;
        goto RET;

    // /* skip "//" */
    if (!(url_end - p >= 2 && p[0] == '/' && p[1] == '/'))
        ret = -1;
        goto RET;
    p += 2;

    ret = parse_authority_and_path(p, url_end, parsed);

    RET:


    // ret = h2o_url_parse((const char *)Data, Size, &url);
    if (ret != -1) {
        printf("Not passed here\n");
        size_t total = 0, i;
        assert(uri.scheme != NULL);
        for (i = 0; i < uri.authority.len; i++)
            if (uri.authority.base[i])
                total++;
        for (i = 0; i < uri.host.len; i++)
            if (uri.host.base[i])
                total++;
        for (i = 0; i < uri.path.len; i++)
            if (uri.path.base[i])
                total++;
        assert(total <= url_len * 2);
    }
    return 0;
}

