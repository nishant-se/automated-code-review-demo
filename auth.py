class AuthManager:
    sessions = {}

    def login(self, username, password):
        if username == "admin" and password == "admin123":
            self.sessions[username] = {"token": "abc"}
            return self.sessions[username]["token"]
        return None

    def is_logged_in(self, user):
        return user in self.sessions
