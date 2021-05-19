from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

web = webdriver.Chrome(ChromeDriverManager().install())
web.implicitly_wait(20)
web.get('https://s2.torrents-igruha.org/')
search_input = 'Dead Or Alive'
web.find_element_by_id('story').send_keys(search_input)
web.find_element_by_xpath('//*[@title="Найти"]').click()
actual_result = web.find_elements_by_class_name('article-film1')
assert len(actual_result) > 0
print('Кількість знайдених: ', len(actual_result))
