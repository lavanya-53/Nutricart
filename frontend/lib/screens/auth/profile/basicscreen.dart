import 'package:flutter/material.dart';
import 'profile_preferences_screen.dart';

class BasicProfileScreen extends StatelessWidget {
  const BasicProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Basic Details'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const TextField(
                decoration: InputDecoration(
                  labelText: 'Health condition',
                  helperText: 'Used to avoid unsafe meals.',
                ),
              ),
              const SizedBox(height: 16),

              const TextField(
                decoration: InputDecoration(
                  labelText: 'Dietary preference',
                  helperText: 'Filters meals to match your lifestyle.',
                ),
              ),
              const SizedBox(height: 16),

              const TextField(
                decoration: InputDecoration(
                  labelText: 'Preferred cuisine',
                  helperText: 'Improves taste relevance.',
                ),
              ),
              const SizedBox(height: 16),

              const TextField(
                decoration: InputDecoration(
                  labelText: 'Location / Region',
                  helperText: 'Adapts grocery availability.',
                ),
              ),
              const SizedBox(height: 24),

              const Divider(),
              const SizedBox(height: 12),

              const Text(
                'Current selections:',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 8),

              const Text('• Health condition: Not set'),
              const Text('• Dietary preference: Not set'),
              const Text('• Preferred cuisine: Not set'),
              const Text('• Location: Not set'),

              const SizedBox(height: 24),

              ElevatedButton(
                onPressed: () {
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(
                      builder: (_) => const ProfilePreferencesScreen(),
                    ),
                  );
                },
                child: const Text('Next'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
