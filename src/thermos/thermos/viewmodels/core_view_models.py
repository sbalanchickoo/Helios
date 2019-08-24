# Standard library imports

# Third party imports

# Local application imports
from thermos.models.user import User
from .. import login_manager


# Retrieves the logged in user object for the global login_manager which will be saved in the http session
# Required by login manager, must be decorated with login_manager.user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

