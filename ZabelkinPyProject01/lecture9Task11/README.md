Цель: Потренировать композицию — когда один класс содержит объекты другого класса.

Класс Song:

init(self, title, artist, duration) — название, исполнитель, длительность в секундах

display_info(self) — возвращает строку: "Исполнитель - Название (MM:SS)"

Класс Playlist:

init(self, name) — название плейлиста

songs — список песен (инициализируется пустым)

add_song(self, song) — добавить песню в плейлист

remove_song(self, song_title) — удалить песню по названию

total_duration(self) — вернуть общую длительность плейлиста (в секундах)

display_playlist(self) — вывести все песни в плейлисте

Требования:

Создай несколько песен (минимум 3)

Создай плейлист "My Favorites"

Добавь песни в плейлист

Удали одну песню

Выведи:

Все песни в плейлисте

Общую длительность в формате "Total duration: MM:SS"

Пример:

Playlist: My Favorites
1. Queen - Bohemian Rhapsody (05:55)
2. The Beatles - Hey Jude (07:11)

Total duration: 13:06