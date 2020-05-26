languages = {
    'Python': 'Guido van Ross',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for x in languages:
    print(x, "was created by", languages.get(x))
