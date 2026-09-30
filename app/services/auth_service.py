import dropbox

from app.core.config import settings


class AuthService:

    def create_oauth_flow(self, session):
        return dropbox.DropboxOAuth2Flow(
            consumer_key=settings.dropbox_app_key,
            redirect_uri=settings.dropbox_redirect_uri,
            session=session,
            csrf_token_session_key="dropbox-auth-csrf-token",
            token_access_type="offline",
            scope=[
                "files.metadata.read",
                "files.content.read",
                "files.content.write",
            ],
        )