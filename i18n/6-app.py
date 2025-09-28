@babel.locale_selector
def get_locale():
    """Determine the locale with priority: URL parameter > user > header > default"""
    # 1. URL parameter
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    # 2. User preference (only if supported)
    if getattr(g, "user", None):
        user_locale = g.user.get("locale")
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    # 3. Request header
    header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if header_locale:
        return header_locale
    # 4. Default
    return app.config['BABEL_DEFAULT_LOCALE']
