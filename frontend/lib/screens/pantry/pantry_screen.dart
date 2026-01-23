import 'package:flutter/material.dart';
import '../../widgets/system_status_banner.dart';

class PantryScreen extends StatelessWidget {
  const PantryScreen({super.key});

  // MOCK DATA — matches GET /pantry contract exactly
  final List<Map<String, dynamic>> mockPantry = const [
    {
      "name": "Rice",
      "quantity": 2,
      "unit": "kg",
      "expiry": "2025-03-01",
    },
    {
      "name": "Milk",
      "quantity": 1,
      "unit": "liter",
      "expiry": null,
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Your Pantry"),
      ),
      body: Column(
        children: [
          const SystemStatusBanner(),

          Expanded(
            child: mockPantry.isEmpty
                ? const _EmptyPantryView()
                : ListView.builder(
                    padding: const EdgeInsets.all(16),
                    itemCount: mockPantry.length,
                    itemBuilder: (context, index) {
                      final item = mockPantry[index];
                      return _PantryItemCard(item: item);
                    },
                  ),
          ),
        ],
      ),
    );
  }
}

class _PantryItemCard extends StatelessWidget {
  final Map<String, dynamic> item;

  const _PantryItemCard({required this.item});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        title: Text(item['name']),
        subtitle: Text(
          '${item['quantity']} ${item['unit']}'
          '${item['expiry'] != null ? '\nExpiry: ${item['expiry']}' : ''}',
        ),
        trailing: const Icon(Icons.kitchen),
      ),
    );
  }
}

class _EmptyPantryView extends StatelessWidget {
  const _EmptyPantryView();

  @override
  Widget build(BuildContext context) {
    return const Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.inventory_2_outlined, size: 48),
          SizedBox(height: 12),
          Text(
            'Your pantry is empty',
            style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 8),
          Text(
            'Add items to track groceries accurately.',
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }
}
