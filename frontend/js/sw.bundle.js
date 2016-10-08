const __version__ = 1;
const CACHE_NAME = `xture-cache-${__version__}`;


let filesToCache = [
    '/',
    '/static/build/js/main.bundle.js',
    '/static/build/js/sw.bundle.js',
    '/static/build/css/main.css',
];


self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(filesToCache);
        })
    );
});


self.addEventListener('fetch', (e) => {
    e.respondWith(
        caches.match(e.request).then(
            (resp) => {
                if ( e.request.url.match(/\/adventure\/$/) || e.request.url.match(/\/adventure\/nearby/)) { return fetch(e.request); }
                return resp || fetch(e.request).then((response) => {
                    if (response) {
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(e.request, response.clone());
                        });
                    }
                    return response;
                });
            },
            (err) => {
                return fetch(e.request).then((response) => {
                    if (response) {
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(e.request, response.clone());
                        });
                    }
                    return response;
                });
            }
        )
    );
});
