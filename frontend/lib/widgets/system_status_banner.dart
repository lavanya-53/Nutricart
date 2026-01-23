import 'package:flutter/material.dart';

class SystemStatusBanner extends StatelessWidget {
  final String message;
  final IconData icon;
  final Color color;

  const SystemStatusBanner({
    super.key,
    this.message = 'Using fallback rules due to limited data',
    this.icon = Icons.info_outline,
    this.color = Colors.orange,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(12),
      color: color.withOpacity(0.1),
      child: Row(
        children: [
          Icon(icon, color: color),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              message,
              style: TextStyle(color: color),
            ),
          ),
        ],
      ),
    );
  }
}
