import requests


class AnkiConnect:
	"""Interact with the AnkiConnect API."""

	def __init__(self, port: int, version: int = 6) -> None:
		self.version = version
		self.port = port
		self.url = f'http://localhost:{str(port)}'

	def get_deck_names(self) -> list:
		"""Returns a list of decks."""
		request_json = requests.get(
			self.url, json={'action': 'deckNames', 'version': self.version}).json()
		if request_json['error'] is None:
			return request_json['result']
		else:
			return request_json['error']

	def create_deck(self, deck_name: str):
		"""Creates a deck."""
		deck_data = {
			'action': 'createDeck',
			'version': 6,
			'params': {'deck': deck_name}
		}
		created_deck_json = requests.post(self.url, json=deck_data).json()

		if created_deck_json['error'] is None:
			return created_deck_json['result']
		else:
			return created_deck_json['error']
