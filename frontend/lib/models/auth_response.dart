class AuthResponse {
  final String userId;
  final String token;

  AuthResponse({
    required this.userId,
    required this.token,
  });

  factory AuthResponse.fromJson(Map<String, dynamic> json) {
    return AuthResponse(
      userId: json['user_id'],
      token: json['token'],
    );
  }
}
