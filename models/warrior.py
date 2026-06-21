from models.champion import Champion


class Warrior(Champion):
    """
    Hệ Chiến Binh — Lesson 01 (Inheritance + super()).

    Thuộc tính riêng:
        shield_bonus (int): Lượng giáp cộng thêm vào sát thương kỹ năng.

    Công thức sát thương kỹ năng: base_atk * 2 + shield_bonus
    """

    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus if shield_bonus > 0 else 0

    def calculate_skill_damage(self):
        """Polymorphism: công thức riêng của Warrior."""
        return self.base_atk * 2 + self.shield_bonus

    def get_extra_stat_label(self):
        return f"Armor: {self.shield_bonus}"