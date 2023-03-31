#include <stddef.h>
#include <stdint.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include "testing.h"


// #define SIZE_MAX 0xffffffffffffffffui64
#define H2O_STRLIT(s) (s), sizeof(s) - 1




const h2o_url_scheme_t H2O_URL_SCHEME_HTTP = {{H2O_STRLIT("http")}, 80, 0};
const h2o_url_scheme_t H2O_URL_SCHEME_HTTPS = {{H2O_STRLIT("https")}, 443, 1};
const h2o_url_scheme_t H2O_URL_SCHEME_MASQUE = {{H2O_STRLIT("masque")}, 65535, 0 /* ??? masque might or might not be over TLS */};

int main(){
    int intsec, returned_value;
    time_t seconds;
    char * url, * scheme, * host, * port, * path;
    size_t url_len;
    h2o_url_t * parsed;
    printf ("hi\n");
    time (&seconds);
    intsec = (int) seconds;
    srand (intsec);

    scheme = (char *) malloc (10 * sizeof (char));
    port = (char *) malloc (10 * sizeof (char));
    url = (char *) malloc (500 * sizeof (char));
    parsed = (h2o_url_t *) malloc (sizeof (h2o_url_t));
    parsed -> scheme = (h2o_url_scheme_t *) malloc (sizeof (h2o_url_scheme_t));
    printf ("hi\n");
    scheme = new_scheme ();
    printf ("hi\n");
    host = new_host ();
    printf ("hi\n");
    sprintf (port, "%d", new_port());
    printf ("hi\n");
    path = new_path();
    printf ("hi\n");
    url = new_url (scheme, host, port, path);
    printf ("hi\n");
    printf("Url: %s\n", url);
    url_len = strlen (scheme) + strlen (host) + strlen (port) + 1;
    printf ("%d\n", url_len);
    printf ("hi\n");
    returned_value = h2o_url_parse(url, url_len, parsed);
    printf ("hi\n");
    printf ("%s %d %d %d\n", parsed -> scheme -> name.base, parsed -> scheme -> name.len, parsed -> scheme -> default_port, parsed -> scheme -> is_ssl);
    printf ("%s %d %s %d %s %d\n", parsed -> authority.base, parsed -> authority.len, parsed -> host.base, parsed -> host.len, parsed -> path.base, parsed -> path.len);
    printf ("%d\n", parsed -> _port);


    
    printf ("result: %d\n", returned_value);

    return 0;
}

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

char get_random_character()
{
	unsigned int i;
    i = rand () % 62 + 65;
    return (char) i;
}

char get_random_character_host () {
    unsigned int i, a;
    i = rand () % 2;
    if (i) {
        a = rand () % 13 + 45;
        while (a == 47) {
            a = rand () % 12 + 46;
        }
    }
    else {
        a = rand () % 26 + 97;
    }
    return (char) a;
}

char get_random_character_path () {
    unsigned int a;
    a = rand () % 94 + 33;
    while (a == 34 | a == 42 | a == 47 | a == 58 | a == 60 | a == 62 | a == 63 | a == 92 | a == 124){
        a = rand () % 94 + 33;
    }
    return (char) a;
}

char get_random_small_alphabet () {
    unsigned int a;
    a = rand () % 26 + 97;
    return (char) a;
}

char * new_scheme () {
    int choose_scheme;
    char * scheme;
    choose_scheme = rand () % 3;
    if (choose_scheme == 0) {
        strcpy (scheme, "http://");
    }
    else if (choose_scheme == 1) {
        strcpy (scheme, "https://");
    }
    else {
        strcpy (scheme, "masque://");
    }
    return scheme;
}

char * new_host () {
    int toggle, idx, host_len, after_dot_len;
    char * host;

    toggle = rand () % 2;
    
    if (toggle) {
        idx = rand () % 100000;
        host = (char *) malloc (strlen(host_list[idx]) * sizeof (char));
        strcpy (host, host_list[idx]);
    }
    else {
        host_len = rand () % 15 + 5;
        after_dot_len = rand () % 2 + 2; 
        host = (char *) malloc ((host_len) * sizeof (char));
        for (int i = 0; i < host_len - (after_dot_len + 1); i ++) {
            host[i] = get_random_character_host ();
        }
        host[host_len - (after_dot_len + 1)] = '.';
        for (int i = host_len - after_dot_len; i < host_len; i++) {
            host[i] = get_random_small_alphabet ();
        }
    }
    return host;
}

uint16_t new_port () {
    uint16_t new_uint16;
    new_uint16 = rand () % 65535 + 1;
    return new_uint16;
}

char * new_path () {
    int path_len;
    char * path;

    path_len = rand () % 29 + 2;
    path = (char *) malloc (path_len * sizeof (char));
    path[0] = '/';
    for (int i = 1; i < path_len; i++) {
        path[i] = get_random_character_path ();
    }
    return path;
}

char * new_url (char * scheme, char * host, char * port, char * path) {
    char * url;

    //url = (char *) malloc (500 * sizeof (char));
    //port = (char *) malloc (6 * sizeof (char));
    printf ("%s\n", url);
    strcat (url, scheme);
    printf ("%s %d\n", scheme, strlen(scheme));
    printf ("%s %s %d\n", url, host, strlen (host));
    strcat (url, host);
    strcat (url, ":");
    printf ("%s %d\n", port, strlen(port));
    strcat (url, port);
    printf ("%s %d\n", path, strlen (path));
    strcat (url, path);
    printf ("%s\n", url);
    return url;
}

h2o_iovec_t new_h2o_iovec () {
    h2o_iovec_t new_h2o_iovec;
    new_h2o_iovec.base = (char *) malloc (1000 * sizeof (char));
    return new_h2o_iovec;
}

const h2o_url_scheme_t * new_h2o_url_scheme () {
    h2o_url_scheme_t * new_h2o_scheme = (h2o_url_scheme_t *) malloc (sizeof (h2o_url_scheme_t));
    new_h2o_scheme -> name = new_h2o_iovec ();
    return new_h2o_scheme;
}

h2o_url_t * new_h2o_url () {
    //h2o_url_t * new_h2o_url = (h2o_url_t *) malloc (sizeof (h2o_url_t));
    h2o_url_t * new_h2o_url;
    h2o_url_scheme_t * new_h2o_scheme;
    h2o_iovec_t new_authority;
    h2o_iovec_t new_host;
    h2o_iovec_t new_path;
    new_h2o_url -> scheme = new_h2o_url_scheme ();
    new_h2o_url -> authority = new_h2o_iovec ();
    new_h2o_url -> host = new_h2o_iovec ();
    new_h2o_url -> path = new_h2o_iovec ();
    new_h2o_url -> _port = new_port ();
    return new_h2o_url;
}

