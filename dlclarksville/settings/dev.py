from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!



# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_HOST = 'smtp.elasticemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 2525
EMAIL_HOST_USER = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

import cloudinary
          
cloudinary.config( 
  cloud_name = "dum5thngj", 
  api_key = "649654183492732", 
  api_secret = "DnhztD3mYzhHh33lb_rpJY8s7BE" 
)
# cloudinary.config( 
#   cloud_name = os.getenv('CLOUD_NAME'), 
#   api_key = os.getenv("CLOUD_API_KEY"), 
#   api_secret = os.getenv("CLOUD_API_SECRET") 
# )


try:
    from .local import *
except ImportError:
    pass
