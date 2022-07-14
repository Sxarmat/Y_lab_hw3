class MassMedia:

	def create_news(self, hero, place):
		hero_name = hero.name
		place_name = getattr(place, 'city_name', 'place')
		print(f'{hero_name} saved the {place_name}!')
