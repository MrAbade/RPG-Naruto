from flask import Flask


def config_views(app: Flask):
    from .village_view import bp_village
    app.register_blueprint(bp_village, url_prefix='/villages')

    from .ninja_view import bp_ninja
    app.register_blueprint(bp_ninja, url_prefix='/ninjas')
