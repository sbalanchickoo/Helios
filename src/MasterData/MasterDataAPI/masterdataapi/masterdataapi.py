from run import create_app
from routes.main import main
from routes.country import country_route
from routes.state import state_route
from routes.user import user_route

if __name__ == "__main__":
    app = create_app('default')
    app.register_blueprint(main)
    app.register_blueprint(country_route, url_prefix = "/masterdata/api/v1")
    app.register_blueprint(state_route)
    app.register_blueprint(user_route)
    app.run(host='0.0.0.0', debug=True)

