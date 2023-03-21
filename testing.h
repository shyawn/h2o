typedef struct st_h2o_iovec_t {
    char *base;
    size_t len;
} h2o_iovec_t;

typedef struct st_h2o_url_scheme_t {
    h2o_iovec_t name;
    uint16_t default_port;
    int is_ssl;
} h2o_url_scheme_t;

typedef struct st_h2o_url_t {
    const h2o_url_scheme_t *scheme;
    h2o_iovec_t authority; /* i.e. host:port */
    h2o_iovec_t host;
    h2o_iovec_t path;
    uint16_t _port;
} h2o_url_t;

size_t h2o_strtosize(const char *s, size_t len);
static h2o_iovec_t h2o_iovec_init(const void *base, size_t len);
const char *h2o_url_parse_hostport(const char *s, size_t len, h2o_iovec_t *host, uint16_t *port);
static int parse_authority_and_path(const char *src, const char *url_end, h2o_url_t *parsed);
static const char *parse_scheme(const char *s, const char *end, const h2o_url_scheme_t **scheme);
int h2o_url_parse(const char *url, size_t url_len, h2o_url_t *parsed);
char get_random_character();
char * new_url ();
size_t new_url_len ();
char * new_base ();
size_t new_len ();
uint16_t new_uint16 ();
h2o_iovec_t new_h2o_iovec ();
const h2o_url_scheme_t * new_h2o_url_scheme ();
h2o_url_t * new_h2o_url ();