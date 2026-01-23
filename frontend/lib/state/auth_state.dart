class AuthState {
  static String? token;
  static String? userId;

  static bool get isLoggedIn => token != null;

  static void clear() {
    token = null;
    userId = null;
  }
}
