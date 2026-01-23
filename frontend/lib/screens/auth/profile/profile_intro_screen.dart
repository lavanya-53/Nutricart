import 'package:flutter/material.dart';
import 'basicscreen.dart';
import '../meal_plan/today_meal_screen.dart';
import '../../pantry/pantry_screen.dart';
import '../../groceries/grocery_list_screen.dart';

class ProfileIntroScreen extends StatelessWidget {
  const ProfileIntroScreen({super.key});

  // TEMP mock data (matches API contract exactly)
  final Map<String, dynamic> mockProfile = const {
    'age': 24,
    'gender': 'Female',
    'region': 'Bangalore',
    'health_conditions': ['Diabetes'],
    'dietary_preferences': ['Vegetarian'],
    'allergies': ['Peanuts'],
  };

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Your Profile')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Profile Summary',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),

            _infoRow('Age', mockProfile['age'].toString()),
            _infoRow('Gender', mockProfile['gender']),
            _infoRow('Region', mockProfile['region']),
            _infoRow(
              'Health Conditions',
              mockProfile['health_conditions'].join(', '),
            ),
            _infoRow(
              'Dietary Preferences',
              mockProfile['dietary_preferences'].join(', '),
            ),
            _infoRow(
              'Allergies',
              mockProfile['allergies'].join(', '),
            ),

            const Spacer(),

            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const BasicProfileScreen(),
                  ),
                );
              },
              child: const Text('Edit Profile'),
            ),
           const SizedBox(height: 12),

ElevatedButton(
  onPressed: () {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => const PantryScreen(),
      ),
    );
  },
  child: const Text("View Pantry"),
),
const SizedBox(height: 12),

ElevatedButton(
  onPressed: () {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => const GroceryListScreen(),
      ),
    );
  },
  child: const Text("View Grocery List"),
),

            const SizedBox(height: 12),

            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const TodayMealScreen(),
                  ),
                );
              },
              child: const Text("View Today's Meal Plan"),
            ),
          ],
        ),
      ),
    );
  }

  Widget _infoRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        children: [
          Expanded(
            child: Text(
              label,
              style: const TextStyle(fontWeight: FontWeight.w600),
            ),
          ),
          Expanded(child: Text(value)),
        ],
      ),
    );
  }
}
