import 'package:flutter/material.dart';
import '../../dashboard/dashboard_screen.dart';

class ProfilePreferencesScreen extends StatelessWidget {
  const ProfilePreferencesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Profile Summary'),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Profile Summary',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),

            _infoRow('Age', '24'),
            _infoRow('Gender', 'Female'),
            _infoRow('Region', 'Bangalore'),
            _infoRow('Health Conditions', 'Diabetes'),
            _infoRow('Dietary Preferences', 'Vegetarian'),
            _infoRow('Allergies', 'Peanuts'),

            const SizedBox(height: 32),

            ElevatedButton(
              onPressed: () {},
              child: const Text('Edit Profile'),
            ),
            const SizedBox(height: 12),

            ElevatedButton(
              onPressed: () {},
              child: const Text('View Pantry'),
            ),
            const SizedBox(height: 12),

            ElevatedButton(
              onPressed: () {},
              child: const Text('View Grocery List'),
            ),
            const SizedBox(height: 12),

            ElevatedButton(
              onPressed: () {},
              child: const Text("View Today's Meal Plan"),
            ),

            const SizedBox(height: 32),

            ElevatedButton(
              onPressed: () {
                Navigator.pushAndRemoveUntil(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const DashboardScreen(),
                  ),
                  (route) => false,
                );
              },
              child: const Text('Finish'),
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
