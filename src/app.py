import falcon
import pathlib
from falcon_swagger_ui import register_swaggerui_app

import src.common.constants as constants
from src.common.cors import Cors
from src.common.require_json import RequireJSON
from src.common.handlers import ExceptionHandler as handler
from src.common import routes

#init falcon
app = falcon.API(middleware=[Cors(), RequireJSON()])

# add routes
routes.Router(app)

STATIC_PATH = pathlib.Path(__file__).parent / 'static'

# global handler exception of application
app.add_error_handler(falcon.HTTPError, handler.handle_generic_error)
app.add_error_handler(Exception, handler.handle_generic_error)

app.add_static_route('/static', str(STATIC_PATH))

# handler for not found resources
app.add_sink(handler.handle_404, '^((?!static).)*$')

# register swagger
register_swaggerui_app(app, constants.SWAGGERUI_URL, constants.SCHEMA_URL, page_title=constants.PAGE_TITLE,
                       favicon_url=constants.FAVICON_URL,
                       config={'supportedSubmitMethods': ['get', 'post', 'put', 'delete'], })
