def calculate_number_of_songs(hours: float, avg_song_length: float = 3.5) -> int:
    minute = hours * 60
    return (minute / avg_song_length)

print(calculate_number_of_songs(2, 4))