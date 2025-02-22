# For more information please refer to https://github.com/checkout/checkout-sdk-python
import checkout_sdk
from checkout_sdk.checkout_sdk import CheckoutSdk
from checkout_sdk.files.files import FileRequest
from checkout_sdk.environment import Environment
from checkout_sdk.exception import CheckoutApiException, CheckoutArgumentException, CheckoutAuthorizationException
from checkout_sdk.oauth_scopes import OAuthScopes

# API Keys
api = CheckoutSdk.builder() \\
    .secret_key('secret_key') \\
    .environment(Environment.sandbox()) \\
    .build()
    # or Environment.production()

# OAuth
api = CheckoutSdk.builder() \\
    .oauth() \\
    .client_credentials('client_id', 'client_secret') \\
    .environment(Environment.sandbox()) \\
    .scopes([OAuthScopes.FILES, OAuthScopes.FILES_UPLOAD]) \\
    .build()

request = FileRequest()
request.file = 'path/to/file'
request.purpose = 'dispute_evidence'

try:
    response = api.disputes.upload_file(request)
except CheckoutApiException as err:
    # API error
    request_id = err.request_id
    status_code = err.http_status_code
    error_details = err.error_details
    http_response = err.http_response
except CheckoutArgumentException as err:
    # Bad arguments

except CheckoutAuthorizationException as err:
    # Invalid authorization