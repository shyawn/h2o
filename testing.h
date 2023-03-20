

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

