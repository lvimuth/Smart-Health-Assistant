// screens/HomeScreen.js
import React, { useState } from 'react';
import { View, Text, Button, TextInput } from 'react-native';
import axios from 'axios';

export default function HomeScreen({ navigation }) {
  const [steps, setSteps] = useState('');
  const [sleep, setSleep] = useState('');
  const [heartRate, setHeartRate] = useState('');

  const submitData = () => {
    axios.post('http://your-server-url/api/recommendation/', {
      steps: steps,
      sleep_hours: sleep,
      heart_rate: heartRate
    }).then(response => {
      navigation.navigate('Recommendations', { recommendation: response.data.recommendation });
    });
  };

  return (
    <View>
      <Text>Steps:</Text>
      <TextInput value={steps} onChangeText={setSteps} keyboardType="numeric" />
      <Text>Sleep Hours:</Text>
      <TextInput value={sleep} onChangeText={setSleep} keyboardType="numeric" />
      <Text>Heart Rate:</Text>
      <TextInput value={heartRate} onChangeText={setHeartRate} keyboardType="numeric" />
      <Button title="Get Recommendation" onPress={submitData} />
    </View>
  );
}
