import 'package:flutter/material.dart';
import '../../../widgets/system_status_banner.dart';
import '../../../services/meal_service.dart';

class TodayMealScreen extends StatefulWidget {
  const TodayMealScreen({super.key});

  @override
  State<TodayMealScreen> createState() => _TodayMealScreenState();
}

class _TodayMealScreenState extends State<TodayMealScreen> {
  bool _loading = true;
  String? _error;
  List meals = [];

  @override
  void initState() {
    super.initState();
    _loadMeals();
  }

  Future<void> _loadMeals() async {
    try {
      final data = await MealService.fetchTodayMealPlan();
      setState(() {
        meals = data['meals'];
        _loading = false;
      });
    } catch (e) {
      setState(() {
        _error = e.toString();
        _loading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Today's Meals")),
      body: Column(
        children: [
          const SystemStatusBanner(),

          Expanded(
            child: _loading
                ? const Center(child: CircularProgressIndicator())
                : _error != null
                    ? Center(child: Text(_error!))
                    : ListView.builder(
                        padding: const EdgeInsets.all(16),
                        itemCount: meals.length,
                        itemBuilder: (context, index) {
                          return _MealCard(meal: meals[index]);
                        },
                      ),
          ),
        ],
      ),
    );
  }
}

class _MealCard extends StatelessWidget {
  final Map<String, dynamic> meal;

  const _MealCard({required this.meal});

  @override
  Widget build(BuildContext context) {
    final nutrition = meal['nutrition'];
    final explanation = meal['explanation'];

    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              meal['name'],
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            Text(
              meal['type'].toString().toUpperCase(),
              style: const TextStyle(color: Colors.grey),
            ),

            const Divider(height: 24),

            Text("Calories: ${nutrition['calories']} kcal"),
            Text("Protein: ${nutrition['protein']} g"),
            Text("Carbs: ${nutrition['carbs']} g"),
            Text("Fat: ${nutrition['fat']} g"),

            const SizedBox(height: 12),
            const Text(
              "Why this meal?",
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            Text("• ${explanation['what_changed']}"),
            Text("• ${explanation['why_changed']}"),
            Text("• ${explanation['health_impact']}"),
          ],
        ),
      ),
    );
  }
}
