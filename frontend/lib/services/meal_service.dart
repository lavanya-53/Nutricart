import '../services/api_service.dart';

class MealService {
  static Future<Map<String, dynamic>> fetchTodayMealPlan() async {
    final json = await ApiService.get('/meal-plan/today');
    return json;
  }
}
