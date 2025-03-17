from faker import Faker

fake = Faker('zh_CN')  # 指定中文语言环境

# 自定义中文电影标题生成器
def generate_chinese_movie_title():
    themes = [
        ['星辰', '江湖', '长安', '山海', '龙门', '青鸟', '白夜', '黄河', '孤城', '锦衣'],
        ['传奇', '往事', '密令', '恋歌', '奇缘', '风云', '迷踪', '谍影', '物语', '惊魂'],
        ['之', '·'],  # 连接词
        ['破晓', '黎明', '暗战', '密码', '密码', '迷局', '秘史', '未央', '夜行', '追凶']
    ]
    return f'《{fake.random_element(themes[0])}' \
           f'{fake.random_element(themes[2])}' \
           f'{fake.random_element(themes[3])}》'

# 生成电影数据
movies = []
for _ in range(10):
    movies.append({
        'title': generate_chinese_movie_title(),
        'year': str(fake.random_int(min=1980, max=2023))  # 生成年份字符串
    })

# 打印结果
print("movies = [")
for movie in movies:
    print(f"    {{'title': '{movie['title']}', 'year': '{movie['year']}'}},")
print("]")