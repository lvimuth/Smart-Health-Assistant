// screens/RecommendationScreen.js
import React from 'react';
import { View, Text } from 'react-native';

export default function RecommendationScreen({ route }) {
  const { recommendation } = route.params;
  return (
    <View>
      <Text>Health Recommendation:</Text>
      <Text>{recommendation}</Text>
    </View>
  );
}
