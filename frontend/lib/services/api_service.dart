import 'dart:convert';
import 'package:http/http.dart' as http;
import '../state/auth_state.dart';

class ApiService {
  static const String _baseUrl = 'http://10.0.2.2:8000';

  /// Common headers (with token if logged in)
  static Map<String, String> _headers() {
    final headers = {
      'Content-Type': 'application/json',
    };

    if (AuthState.token != null) {
      headers['Authorization'] = 'Bearer ${AuthState.token}';
    }

    return headers;
  }

  /// GET
  static Future<dynamic> get(String path) async {
    final response = await http.get(
      Uri.parse('$_baseUrl$path'),
      headers: _headers(),
    );

    _handleErrors(response);
    return jsonDecode(response.body);
  }

  /// POST
  static Future<dynamic> post(String path, Map<String, dynamic> body) async {
    final response = await http.post(
      Uri.parse('$_baseUrl$path'),
      headers: _headers(),
      body: jsonEncode(body),
    );

    _handleErrors(response);
    return jsonDecode(response.body);
  }

  /// PUT
  static Future<dynamic> put(String path, Map<String, dynamic> body) async {
    final response = await http.put(
      Uri.parse('$_baseUrl$path'),
      headers: _headers(),
      body: jsonEncode(body),
    );

    _handleErrors(response);
    return jsonDecode(response.body);
  }

  /// DELETE
  static Future<dynamic> delete(String path) async {
    final response = await http.delete(
      Uri.parse('$_baseUrl$path'),
      headers: _headers(),
    );

    _handleErrors(response);
    return jsonDecode(response.body);
  }

  static void _handleErrors(http.Response response) {
    if (response.statusCode >= 400) {
      throw Exception(
        'API Error ${response.statusCode}: ${response.body}',
      );
    }
  }
}
