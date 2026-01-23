import 'package:flutter/material.dart';
import '../../../widgets/system_status_banner.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('NutriCart Dashboard'),
      ),
      body: Column(
        children: [
          const SystemStatusBanner(),

          Expanded(
            child: ListView(
              padding: const EdgeInsets.all(16),
              children: const [
                _SectionCard(
                  title: "Today's Meals",
                  content: "Breakfast • Lunch • Dinner • Snack",
                ),
                SizedBox(height: 16),

                _SectionCard(
                  title: "Highlighted Changes",
                  content: "No meal changes detected today",
                ),
                SizedBox(height: 16),

                _SectionCard(
                  title: "Health Insight",
                  content: "Your iron intake is stable today",
                ),
                SizedBox(height: 16),

                _SectionCard(
                  title: "Grocery Summary",
                  content: "3 items may need restocking",
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _SectionCard extends StatelessWidget {
  final String title;
  final String content;

  const _SectionCard({
    required this.title,
    required this.content,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              title,
              style: const TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Text(content),
          ],
        ),
      ),
    );
  }
}

