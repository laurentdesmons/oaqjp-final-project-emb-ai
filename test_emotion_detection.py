import json
import unittest
import EmotionDetection

class TestEmotionDetection(unittest.TestCase):
    def get_dominant_emotion(self, text_to_analyse:str):
        result = json.loads(EmotionDetection.emotion_detection.emotion_detector(text_to_analyse))
        return result['dominant_emotion']

    def test_joy(self):
        result = self.get_dominant_emotion('I am glad this happened')
        self.assertEqual(result, 'joy')

    def test_anger(self):
        result = self.get_dominant_emotion('I am really mad about this')
        self.assertEqual(result, 'anger')

    def test_disgust(self):
        result = self.get_dominant_emotion('I feel disgusted just hearing about this')
        self.assertEqual(result, 'disgust')

    def test_sadness(self):
        result = self.get_dominant_emotion('I am so sad about this')
        self.assertEqual(result, 'sadness')

    def test_fear(self):
        result = self.get_dominant_emotion('I am really afraid that this will happen')
        self.assertEqual(result, 'fear')

if __name__ == '__main__':
    unittest.main()