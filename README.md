# ankipy

A python package for interacting with the AnkiConnect API.

Currently the library is capable of:

- Suspending/Unsuspending notes.
- Checking if notes are suspended.
- Creating decks.
- Getting a list of decks.

# Getting Started

Getting started is simple, first create an `AnkiConnect` object.

```python
 from ankipy.ankiconnect import AnkiConnect
 ac =
AnkiConnect(port=8765)
```

### Decks

You can get a list of decks with `get_deck_names()`

```python
 ac.get_deck_names()
```

Result:

```json
["Default", "Japanese"]
```

Creating a deck is done with `create_deck()`

```python
ac.create_deck("PyDeck")
```

### Notes

#### Suspended Notes

You can use a notes ID to suspend it. The function will return True if it was successful, and False if it wasn't.

```python
ac.suspend([1234567890])
```

Unsuspending notes is done with `unsuspend`

```python
ac.unsuspend([1234567890])
```

You can check if a list of cards is unsuspended using `are_suspended()`

```python
ac.are_suspended([1234567890, 0987654321])
```
