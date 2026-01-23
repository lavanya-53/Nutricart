import 'package:flutter/material.dart';
import '../../widgets/system_status_banner.dart';

class GroceryListScreen extends StatelessWidget {
  const GroceryListScreen({super.key});

  // MOCK DATA — matches GET /groceries/weekly contract exactly
  final Map<String, dynamic> mockGroceries = const {
    "generated_from": "meal_plan",
    "items": [
      {
        "name": "Semolina",
        "quantity": 1,
        "unit": "kg",
        "source_reason": "meal",
      },
      {
        "name": "Vegetables",
        "quantity": 2,
        "unit": "kg",
        "source_reason": "reengineering",
      },
      {
        "name": "Milk",
        "quantity": 1,
        "unit": "liter",
        "source_reason": "substitution",
      }
    ]
  };

  @override
  Widget build(BuildContext context) {
    final items = mockGroceries['items'] as List;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Weekly Groceries'),
      ),
      body: Column(
        children: [
          const SystemStatusBanner(),

          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: items.length,
              itemBuilder: (context, index) {
                final item = items[index];
                return _GroceryItemCard(item: item);
              },
            ),
          ),
        ],
      ),
    );
  }
}

class _GroceryItemCard extends StatelessWidget {
  final Map<String, dynamic> item;

  const _GroceryItemCard({required this.item});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        title: Text(item['name']),
        subtitle: Text(
          '${item['quantity']} ${item['unit']}\n'
          'Added because: ${item['source_reason']}',
        ),
        trailing: const Icon(Icons.shopping_cart_outlined),
      ),
    );
  }
}
