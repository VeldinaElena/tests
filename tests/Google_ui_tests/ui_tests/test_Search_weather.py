from tests.Google_ui_tests.ui_actions import SearchActions

search_data = "The weather in saint petersburg"


class TestSearchWeather:

    def test_search_weather(self):
        SearchActions.search_weather(search_data)
        SearchActions.open_first_link()
        weather_result = SearchActions.get_results()
        print(f'Saint Petersburg has following weather: {weather_result}')
