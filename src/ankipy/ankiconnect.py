import requests


class AnkiConnect:
	"""Interact with the AnkiConnect API."""

	def __init__(self, port: int = 8765, version: int = 6) -> None:
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

	def create_deck(self, deck_name: str) -> int:
		"""Creates a deck."""
		deck_data = {
			'action': 'createDeck',
			'version': self.version,
			'params': {'deck': deck_name}
		}
		created_deck_json = requests.post(self.url, json=deck_data).json()

		if created_deck_json['error'] is None:
			return created_deck_json['result']
		else:
			return created_deck_json['error']

	def suspend(self, card_ids: list) -> bool:
		"""Suspend a card. Returns true if successful."""
		request_data = {
			'action': 'suspend',
			'version': self.version,
			'params': {
				'cards': card_ids
			}
		}
		suspend_request = requests.get(self.url, json=request_data).json()
		return suspend_request['result']

	def unsuspend(self, card_ids: list) -> bool:
		"""Unsuspend a card. Returns true if successful."""
		request_data = {
			'action': 'unsuspend',
			'version': self.version,
			'params': {
				'cards': card_ids
			}
		}
		unsuspend_request = requests.get(self.url, json=request_data).json()
		return unsuspend_request['result']

	def are_suspended(self, card_ids: list) -> bool:
		"""Checks if a list of cards a suspended."""
		request_data = {
			'action': 'areSuspended',
			'version': self.version,
			'params': {
				'cards': card_ids
			}
		}
		are_suspended_request = requests.get(self.url, json=request_data).json()
		if are_suspended_request['error'] is None:
			return are_suspended_request['result']
		else:
			return are_suspended_request['error']
