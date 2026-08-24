def solution(genres, plays):
    infos = []
    for index, (genre, play) in enumerate(zip(genres, plays)):
        current_info = {
            'index' : index,
            'genre' : genre,
            'play' : play
        }
        infos.append(current_info)
    
    infos.sort(key=lambda x: (x['genre'], x['play']), reverse=True)
    result = [info['index'] for info in infos[:2]]
    return result