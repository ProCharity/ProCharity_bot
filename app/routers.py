from app import api
from app.apis.users import UsersList, User_item
from app.apis.auth.refresh import Refresh
from app.apis.auth.login import Login
from app.apis.auth.password_reset import PasswordReset
from app.apis.auth.registration import UserRegister
from app.apis.auth.invitation_checker import InvitationChecker
from app.apis.auth.send_reg_invitation import SendRegistrationInvitation
from app.webhook import Create_categories, Create_tasks
from app.apis.messages import SendPushEmailMessage

api.add_resource(UsersList, '/api/users/')
api.add_resource(User_item, '/api/users/<int:id>/')

api.add_resource(InvitationChecker, '/api/auth/invitation_checker')
api.add_resource(Login, '/api/auth/login/')
api.add_resource(Refresh, '/api/auth/token_refresh/')
api.add_resource(PasswordReset, '/api/auth/password_reset/')
api.add_resource(UserRegister, '/api/auth/register/')
api.add_resource(SendRegistrationInvitation, '/api/auth/Invitation')

api.add_resource(SendPushEmailMessage, '/api/send_message/')
api.add_resource(Create_tasks, '/api/v1/tasks/')
api.add_resource(Create_categories, '/api/v1/categories/')
