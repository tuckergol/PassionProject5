# model.py

class CountryModel:
    def __init__(self):
        self.countries = [
            {"name": "United States", "image_url": "image_url_usa.jpg"},
            {"name": "United Kingdom", "image_url": "image_url_uk.jpg"},
            {"name": "Canada", "image_url": "image_url_canada.jpg"},
            {"name": "Australia", "image_url": "image_url_australia.jpg"},
            {"name": "France", "image_url": "image_url_france.jpg"},
            {"name": "Germany", "image_url": "image_url_germany.jpg"},
            {"name": "Italy", "image_url": "image_url_italy.jpg"},
            {"name": "Japan", "image_url": "image_url_japan.jpg"},
            {"name": "China", "image_url": "image_url_china.jpg"},
            {"name": "India", "image_url": "image_url_india.jpg"},
            {"name": "Russia", "image_url": "image_url_russia.jpg"},
            {"name": "Brazil", "image_url": "image_url_brazil.jpg"},
            {"name": "Mexico", "image_url": "image_url_mexico.jpg"},
            {"name": "Spain", "image_url": "image_url_spain.jpg"},
            {"name": "South Africa", "image_url": "image_url_south_africa.jpg"},
            {"name": "Argentina", "image_url": "image_url_argentina.jpg"},
            {"name": "Egypt", "image_url": "image_url_egypt.jpg"},
            {"name": "Turkey", "image_url": "image_url_turkey.jpg"},
            {"name": "Greece", "image_url": "image_url_greece.jpg"},
            {"name": "Netherlands", "image_url": "image_url_netherlands.jpg"},
            {"name": "Switzerland", "image_url": "image_url_switzerland.jpg"},
            {"name": "South Korea", "image_url": "image_url_south_korea.jpg"},
            {"name": "Sweden", "image_url": "image_url_sweden.jpg"},
            {"name": "Norway", "image_url": "image_url_norway.jpg"},
            {"name": "Denmark", "image_url": "image_url_denmark.jpg"},
            {"name": "Ireland", "image_url": "image_url_ireland.jpg"},
            {"name": "New Zealand", "image_url": "image_url_new_zealand.jpg"},
            {"name": "Singapore", "image_url": "image_url_singapore.jpg"},
            {"name": "Malaysia", "image_url": "image_url_malaysia.jpg"},
            {"name": "Thailand", "image_url": "image_url_thailand.jpg"},
            {"name": "Vietnam", "image_url": "image_url_vietnam.jpg"},
            {"name": "Indonesia", "image_url": "image_url_indonesia.jpg"},
            {"name": "Philippines", "image_url": "image_url_philippines.jpg"},
            {"name": "Saudi Arabia", "image_url": "image_url_saudi_arabia.jpg"},
            {"name": "Qatar", "image_url": "image_url_qatar.jpg"},
            {"name": "Israel", "image_url": "image_url_israel.jpg"},
            {"name": "Jordan", "image_url": "image_url_jordan.jpg"},
            {"name": "Lebanon", "image_url": "image_url_lebanon.jpg"},
        ]

    def get_country_info(self):
        current_country = random.choice(self.countries)
        return {"country": current_country}

country_model = CountryModel()
