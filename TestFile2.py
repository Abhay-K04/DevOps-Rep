"""A tiny, dependency-free AI chatbot using keyword intent matching."""

import random
import re


INTENTS = {
	"greeting": {
		"keywords": {"hello", "hi", "hey"},
		"responses": ["Hello!", "Hi there!", "Hey—how can I help?"],
	},
	"help": {
		"keywords": {"help", "what", "can", "do"},
		"responses": ["I can chat, tell the time, or answer simple questions."],
	},
	"name": {
		"keywords": {"name", "who"},
		"responses": ["I am MiniAI, a small Python chatbot."],
	},
	"bye": {
		"keywords": {"bye", "goodbye", "exit", "quit"},
		"responses": ["Goodbye!"],
	},
}


def predict_intent(message: str) -> str:
	"""Choose the intent with the most matching words."""
	words = set(re.findall(r"[a-z]+", message.lower()))
	scores = {
		intent: len(words & data["keywords"])
		for intent, data in INTENTS.items()
	}
	best_intent = max(scores, key=scores.get)
	return best_intent if scores[best_intent] else "unknown"


def respond(message: str) -> str:
	intent = predict_intent(message)
	if intent == "unknown":
		return "I am still learning. Try asking for help."
	return random.choice(INTENTS[intent]["responses"])


def main() -> None:
	print("MiniAI: Hello! Type 'quit' to stop.")
	while True:
		message = input("You: ").strip()
		if not message:
			continue
		answer = respond(message)
		print(f"MiniAI: {answer}")
		if predict_intent(message) == "bye":
			break


if __name__ == "__main__":
	main()
