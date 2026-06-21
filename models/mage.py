from models.champion import Champion


class Mage(Champion):
    """
    Hệ Pháp Sư — Lesson 01 (Inheritance + super()).

    Thuộc tính riêng:
        ability_power (float): Hệ số nhân sức mạnh phép thuật (VD: 1.5, 2.0).

    Công thức sát thương kỹ năng: base_atk * ability_power
    """

    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power if ability_power > 0 else 1.0

    def calculate_skill_damage(self):
        """Polymorphism: công thức riêng của Mage."""
        return self.base_atk * self.ability_power

    def get_extra_stat_label(self):
        return f"Mana: {self.ability_power}"