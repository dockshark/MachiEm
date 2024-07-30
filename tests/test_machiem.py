import unittest
import sys
import os

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from MachiEm import MachiEm

class TestMachiEm(unittest.TestCase):
    def setUp(self):
        self.machiem = MachiEm()
        self.machiem.set_state("Combined")

    def test_combined_response_disgust(self):
        self.machiem.set_user_preferences("user1", {})
        response = self.machiem.process_input("user1", "This is disgusting!")
        expected = (
            "Combined response: 10%: Optimally processing: This is disgusting! | 10%: Data in flux: This is disgusting! | 10%: Encountered an error, adapting: This is disgusting! | "
            "10%: Responding to anger with Furywave: This is disgusting! | 10%: Responding to fear with Terrashade: This is disgusting! | 5%: Responding to greed with Covetstorm: This is disgusting! | "
            "5%: Responding to jealousy with Envyflare: This is disgusting! | 30%: Responding to disgust with Repulson: This is disgusting! | 5%: Responding to surprise with Astonishlight: This is disgusting! | "
            "5%: Responding to sadness with Gloomveil: This is disgusting! | 5%: Responding to happiness with Joypulse: This is disgusting!"
        )
        self.assertEqual(response, expected)

    def test_combined_response_greed(self):
        self.machiem.set_user_preferences("user1", {})
        response = self.machiem.process_input("user1", "I want everything!")
        expected = (
            "Combined response: 10%: Optimally processing: I want everything! | 10%: Data in flux: I want everything! | 10%: Encountered an error, adapting: I want everything! | "
            "10%: Responding to anger with Furywave: I want everything! | 10%: Responding to fear with Terrashade: I want everything! | 30%: Responding to greed with Covetstorm: I want everything! | "
            "5%: Responding to jealousy with Envyflare: I want everything! | 5%: Responding to disgust with Repulson: I want everything! | 10%: Responding to surprise with Astonishlight: I want everything! | "
            "5%: Responding to sadness with Gloomveil: I want everything! | 5%: Responding to happiness with Joypulse: I want everything!"
        )
        self.assertEqual(response, expected)

    def test_combined_response_jealousy(self):
        self.machiem.set_user_preferences("user1", {})
        response = self.machiem.process_input("user1", "I am so jealous!")
        expected = (
            "Combined response: 10%: Optimally processing: I am so jealous! | 10%: Data in flux: I am so jealous! | 10%: Encountered an error, adapting: I am so jealous! | "
            "10%: Responding to anger with Furywave: I am so jealous! | 10%: Responding to fear with Terrashade: I am so jealous! | 5%: Responding to greed with Covetstorm: I am so jealous! | "
            "30%: Responding to jealousy with Envyflare: I am so jealous! | 5%: Responding to disgust with Repulson: I am so jealous! | 5%: Responding to surprise with Astonishlight: I am so jealous! | "
            "5%: Responding to sadness with Gloomveil: I am so jealous! | 5%: Responding to happiness with Joypulse: I am so jealous!"
        )
        self.assertEqual(response, expected)

    def test_combined_response_happiness(self):
        self.machiem.set_user_preferences("user1", {})
        response = self.machiem.process_input("user1", "I am so happy!")
        expected = (
            "Combined response: 20%: Optimally processing: I am so happy! | 20%: Data in flux: I am so happy! | 10%: Encountered an error, adapting: I am so happy! | "
            "5%: Responding to anger with Furywave: I am so happy! | 5%: Responding to fear with Terrashade: I am so happy! | 5%: Responding to greed with Covetstorm: I am so happy! | "
            "5%: Responding to jealousy with Envyflare: I am so happy! | 5%: Responding to disgust with Repulson: I am so happy! | 5%: Responding to surprise with Astonishlight: I am so happy! | "
            "5%: Responding to sadness with Gloomveil: I am so happy! | 5%: Responding to happiness with Joypulse: I am so happy!"
        )
        self.assertEqual(response, expected)

    def test_combined_response_surprise(self):
        self.machiem.set_user_preferences("user1", {})
        response = self.machiem.process_input("user1", "I am so surprised!")
        expected = (
            "Combined response: 10%: Optimally processing: I am so surprised! | 10%: Data in flux: I am so surprised! | 10%: Encountered an error, adapting: I am so surprised! | "
            "10%: Responding to anger with Furywave: I am so surprised! | 10%: Responding to fear with Terrashade: I am so surprised! | 10%: Responding to greed with Covetstorm: I am so surprised! | "
            "5%: Responding to jealousy with Envyflare: I am so surprised! | 10%: Responding to disgust with Repulson: I am so surprised! | 30%: Responding to surprise with Astonishlight: I am so surprised! | "
            "5%: Responding to sadness with Gloomveil: I am so surprised! | 5%: Responding to happiness with Joypulse: I am so surprised!"
        )
        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
"""

# Write the updated content to test_machiem.py
test_machiem_path = '/mnt/data/MachiEm-main/MachiEm-main/tests/test_machiem.py'
with open(test_machiem_path, 'w') as file:
    file.write(test_machiem_updated_content) &#8203;:citation[oaicite:0]{index=0}&#8203;
