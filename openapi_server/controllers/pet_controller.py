import connexion
import six

from openapi_server.models.document import Document  # noqa: E501
from openapi_server import util


def upload_document(body):  # noqa: E501
    """Add a new pet to the store

     # noqa: E501

    :param body: Document file that needs to be uploaded in order to be verified
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Document.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
