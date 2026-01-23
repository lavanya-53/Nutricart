class UserProfile {
  final String userId;
  final int age;
  final String gender;
  final double weight;
  final String region;
  final List<String> healthConditions;
  final List<String> dietaryPreferences;
  final List<String> allergies;

  UserProfile({
    required this.userId,
    required this.age,
    required this.gender,
    required this.weight,
    required this.region,
    required this.healthConditions,
    required this.dietaryPreferences,
    required this.allergies,
  });

  factory UserProfile.fromJson(Map<String, dynamic> json) {
    return UserProfile(
      userId: json['user_id'],
      age: json['age'],
      gender: json['gender'],
      weight: (json['weight'] as num).toDouble(),
      region: json['region'],
      healthConditions:
          List<String>.from(json['health_conditions'] ?? []),
      dietaryPreferences:
          List<String>.from(json['dietary_preferences'] ?? []),
      allergies: List<String>.from(json['allergies'] ?? []),
    );
  }
}
