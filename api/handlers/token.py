from api import app, multy_auth
from api.models.user import UserModel


@app.route('/auth/token')
@multy_auth.login_required
def get_auth_token():
    user = multy_auth.current_user()
    # user = UserModel.query.filter_by(username=username).first()
    token = user.generate_auth_token()
    return {'token': token}