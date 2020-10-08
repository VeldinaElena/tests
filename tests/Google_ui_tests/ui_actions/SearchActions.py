from tests.Google_ui_tests.page_objects.SearchPage import SearchPage


def search_weather(search_data):
    page = SearchPage()
    page.input_search_data(search_data)
    page.click_search()


def open_first_link():
    SearchPage().open_first_link()


def get_results():
    return SearchPage().get_results()
