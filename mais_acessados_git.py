import requests
import pygal
from pygal.style import LightStyle
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(URL)
print('Status code: ', r.status_code)

response_dict = r.json()
print('Repositórios totais: ', response_dict['total_count'])

repo_dicts = response_dict['items']
nomes, plot_dicts= [], []

for repo_dict in repo_dicts:
    nomes.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'], 'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

meu_estilo = LightStyle
minha_config = pygal.Config()
minha_config.x_label_rotation = 45
minha_config.show_legend = False
minha_config.title_font_size = 24
minha_config.label_font_size = 14
minha_config.major_label_font_size = 18
minha_config.truncate_label = 15
minha_config.show_y_guides = False
minha_config.width = 1000
chart = pygal.Bar(minha_config, style=meu_estilo)
chart.title = 'Projetos no GitHub com mais estrelas'
chart.x_labels = nomes
chart.add('', plot_dicts)
chart.render_to_file('python_repositorio.svg')
