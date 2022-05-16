import falcon
import json


class ExceptionHandler:
    @staticmethod
    def handle_404(req, resp):
        """
              :param req: the request object
              :param resp: the response object
              :return:
        """
        resp.status = falcon.HTTP_404

        message = {
            'description': 'not found: Path=' + req.path,
            'status': 404,
            'title': 'No resource found for your request. Please verify your request.',
            'data': {}
        }
        resp.body = json.dumps(message)

    @staticmethod
    def handle_generic_error(ex, req, resp, params):
        statusCode = 500
        description = "There was an internal error. Try again later"

        if hasattr(ex, 'status'):
            statusCode = int(ex.status[:3])
        if hasattr(ex, 'title'):
            description = str(ex.title)


        message = {
            'title': 'Something went wrong',
            'status': statusCode,
            'description': description,
            'data': {}
        }
        resp.body = json.dumps(message)        
