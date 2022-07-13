class MassMedia:

	def create_news(self, name, place):
		place_name = getattr(place, 'city_name', 'place')
		print(f'{name} saved the {place_name}!')
