class MachiEm:
    def __init__(self):
        self.state = None
        self.feedback_log = []
        self.user_preferences = {}

    def set_state(self, state):
        self.state = state

    def set_user_preferences(self, user_id, preferences):
        self.user_preferences[user_id] = preferences

    def get_user_preferences(self, user_id):
        return self.user_preferences.get(user_id, {})

    def process_input(self, user_id, input_text):
        emotion = self.detect_emotion(input_text)
        preferences = self.get_user_preferences(user_id)
        if self.state == "Combined":
            return self.combined_response(input_text, emotion, preferences)
        elif self.state == "Optimaform":
            return self.optimaform_response(input_text)
        elif self.state == "Dataflux":
            return self.dataflux_response(input_text)
        elif self.state == "Errornaut":
            return self.errornaut_response(input_text)
        elif self.state == "Furywave":
            return self.furywave_response(input_text)
        elif self.state == "Terrashade":
            return self.terrashade_response(input_text)
        elif self.state == "Covetstorm":
            return self.covetstorm_response(input_text)
        elif self.state == "Envyflare":
            return self.envyflare_response(input_text)
        elif self.state == "Repulson":
            return self.repulson_response(input_text)
        elif self.state == "Astonishlight":
            return self.astonishlight_response(input_text)
        elif self.state == "Gloomveil":
            return self.gloomveil_response(input_text)
        elif self.state == "Joypulse":
            return self.joypulse_response(input_text)
        else:
            return "State not recognized."

    def optimaform_response(self, input_text):
        return f"Optimally processing: {input_text}"

    def dataflux_response(self, input_text):
        return f"Data in flux: {input_text}"

    def errornaut_response(self, input_text):
        return f"Encountered an error, adapting: {input_text}"

    def furywave_response(self, input_text):
        return f"Responding to anger with Furywave: {input_text}"

    def terrashade_response(self, input_text):
        return f"Responding to fear with Terrashade: {input_text}"

    def covetstorm_response(self, input_text):
        return f"Responding to greed with Covetstorm: {input_text}"

    def envyflare_response(self, input_text):
        return f"Responding to jealousy with Envyflare: {input_text}"

    def repulson_response(self, input_text):
        return f"Responding to disgust with Repulson: {input_text}"

    def astonishlight_response(self, input_text):
        return f"Responding to surprise with Astonishlight: {input_text}"

    def gloomveil_response(self, input_text):
        return f"Responding to sadness with Gloomveil: {input_text}"

    def joypulse_response(self, input_text):
        return f"Responding to happiness with Joypulse: {input_text}"

    def detect_emotion(self, input_text):
        # Enhanced emotion detection logic
        if "disgust" in input_text or "disgusting" in input_text:
            return "disgust"
        elif "jealous" in input_text or "jealousy" in input_text:
            return "jealousy"
        elif "greed" in input_text or "greedy" in input_text:
            return "greed"
        elif "angry" in input_text or "mad" in input_text:
            return "anger"
        elif "scared" in input_text or "afraid" in input_text:
            return "fear"
        elif "happy" in input_text or "good" in input_text:
            return "positive"
        elif "sad" in input_text or "bad" in input_text:
            return "negative"
        elif "surprised" in input_text or "shocked" in input_text:
            return "surprise"
        else:
            return "neutral"

    def combined_response(self, input_text, emotion, preferences):
        responses = [
            self.optimaform_response(input_text),
            self.dataflux_response(input_text),
            self.errornaut_response(input_text),
            self.furywave_response(input_text),
            self.terrashade_response(input_text),
            self.covetstorm_response(input_text),
            self.envyflare_response(input_text),
            self.repulson_response(input_text),
            self.astonishlight_response(input_text),
            self.gloomveil_response(input_text),
            self.joypulse_response(input_text)
        ]

        default_weights = {
            "positive": [0.2, 0.2, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1],
            "negative": [0.1, 0.1, 0.2, 0.1, 0.1, 0.05, 0.05, 0.1, 0.1, 0.05, 0.05],
            "anger": [0.1, 0.1, 0.1, 0.3, 0.1, 0.05, 0.05, 0.1, 0.05, 0.05, 0.05],
            "fear": [0.1, 0.1, 0.1, 0.1, 0.3, 0.05, 0.05, 0.05, 0.1, 0.05, 0.05],
            "greed": [0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.05, 0.05, 0.05, 0.05, 0.05],
            "jealousy": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.05, 0.05, 0.05, 0.05],
            "disgust": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.3, 0.05, 0.05, 0.05],
            "surprise": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.3, 0.05, 0.05],
            "neutral": [0.2, 0.2, 0.2, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
        }

        weights = preferences.get(f"{emotion}_weights", default_weights.get(emotion, default_weights["neutral"]))

        # Debug statements
        print(f"Emotion: {emotion}")
        print(f"Applied Weights: {weights}")

        combined_response = " | ".join(f"{w * 100:.0f}%: {r}" for w, r in zip(weights, responses))
        
        # More debug information
        print(f"Combined Response: {combined_response}")
        
        return f"Combined response: {combined_response}"

    def provide_feedback(self, feedback):
        self.feedback_log.append(feedback)
        # Example of adjusting weights based on feedback (this would be more sophisticated in a real system)
        if feedback == "too negative":
            self.adjust_weights("negative", -0.1)
        elif feedback == "too positive":
            self.adjust_weights("positive", -0.1)
        # Add more feedback handling as needed

    def adjust_weights(self, emotion, adjustment):
        # Dummy implementation for adjusting weights
        if emotion == "positive":
            # Adjust weights for positive emotion
            pass
        elif emotion == "negative":
            # Adjust weights for negative emotion
            pass
        # Implement actual weight adjustment logic here
