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

    def combined_response(self, input_text, emotion, preferences):
        weights = {
            "anger": 0.1,
            "fear": 0.1,
            "greed": 0.1,
            "jealousy": 0.05,
            "disgust": 0.1,
            "surprise": 0.1,
            "sadness": 0.05,
            "happiness": 0.05,
            "neutral": 0.2
        }
        if emotion == "disgust":
            weights["disgust"] = 0.3
        elif emotion == "greed":
            weights["greed"] = 0.3
        elif emotion == "jealousy":
            weights["jealousy"] = 0.3
        elif emotion == "surprise":
            weights["surprise"] = 0.3

        response = "Combined response: "
        response += f"{weights['neutral']*100}%: Optimally processing: {input_text} | "
        response += f"{weights['neutral']*100}%: Data in flux: {input_text} | "
        response += f"{weights['neutral']*100}%: Encountered an error, adapting: {input_text} | "
        response += f"{weights['anger']*100}%: Responding to anger with Furywave: {input_text} | "
        response += f"{weights['fear']*100}%: Responding to fear with Terrashade: {input_text} | "
        response += f"{weights['greed']*100}%: Responding to greed with Covetstorm: {input_text} | "
        response += f"{weights['jealousy']*100}%: Responding to jealousy with Envyflare: {input_text} | "
        response += f"{weights['disgust']*100}%: Responding to disgust with Repulson: {input_text} | "
        response += f"{weights['surprise']*100}%: Responding to surprise with Astonishlight: {input_text} | "
        response += f"{weights['sadness']*100}%: Responding to sadness with Gloomveil: {input_text} | "
        response += f"{weights['happiness']*100}%: Responding to happiness with Joypulse: {input_text}"

        return response

    def detect_emotion(self, input_text):
        # Placeholder for emotion detection logic
        if "disgusting" in input_text:
            return "disgust"
        elif "want everything" in input_text:
            return "greed"
        elif "jealous" in input_text:
            return "jealousy"
        elif "surprised" in input_text:
            return "surprise"
        elif "happy" in input_text:
            return "happiness"
        elif "sad" in input_text:
            return "sadness"
        elif "angry" in input_text:
            return "anger"
        elif "fear" in input_text:
            return "fear"
        else:
            return "neutral"
