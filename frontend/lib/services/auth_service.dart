import '../models/auth_response.dart';
import 'api_service.dart';

class AuthService {
  /// POST /auth/login
  static Future<AuthResponse> login({
    required String email,
    required String password,
  }) async {
    try {
      final json = await ApiService.post(
        '/auth/login',
        {
          'email': email,
          'password': password,
        },
      );

      return AuthResponse.fromJson(json);
    } catch (e) {
      throw _mapAuthError(e.toString());
    }
  }

  /// POST /auth/register
  static Future<AuthResponse> register({
    required String email,
    required String password,
    required String name,
  }) async {
    try {
      final json = await ApiService.post(
        '/auth/register',
        {
          'email': email,
          'password': password,
          'name': name,
        },
      );

      return AuthResponse.fromJson(json);
    } catch (e) {
      throw 'Registration failed. Please try again.';
    }
  }

  static String _mapAuthError(String error) {
    if (error.contains('Invalid password') ||
        error.contains('Invalid credentials')) {
      return 'Invalid email or password';
    }

    if (error.contains('User not found')) {
      return 'Account does not exist';
    }

    return 'Login failed. Please try again.';
  }
}
