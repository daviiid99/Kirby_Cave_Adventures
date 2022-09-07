class Boss :

	def __init__(self, boss) :
		self.available_boss = {
		"frosty" : {
			"HP" : 20,
			"HABILITY" : "ice"
		}
		}

		self.hp = boss["HP"]