const PROXY_CONFIG = [
  {
    context: ['/api/**', '/static/**'],
    target: 'http://localhost:80',
    secure: false,
    logLevel: 'debug',
    changeOrigin: true
  }
];

module.exports = PROXY_CONFIG;
