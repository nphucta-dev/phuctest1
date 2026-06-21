from abc import ABC, abstractmethod


class Champion(ABC):
    """
    Lớp trừu tượng (Abstract Base Class) — khuôn mẫu cho mọi hệ tướng.

    Không thể khởi tạo trực tiếp Champion(...).
    Mọi lớp con BẮT BUỘC override calculate_skill_damage() theo đặc thù hệ tộc.

    Attributes:
        champion_id (str): Mã định danh quân cờ (VD: WAR01).
        name (str): Tên tướng.
        base_hp (int): Máu cơ bản. Tối thiểu 100.
        base_atk (int): Sức công kích cơ bản. Tối thiểu 100.
    """

    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name
        # Bẫy 2: tự reset về 100 nếu <= 0
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """
        Polymorphism — Lesson 03:
        Mỗi hệ tướng tự định nghĩa công thức sát thương riêng.
        Buộc override: không override → TypeError khi khởi tạo.
        """
        pass

    def get_combat_power(self):
        """
        Điểm chiến lực tổng hợp = base_hp + calculate_skill_damage() * 1.5
        Gọi calculate_skill_damage() qua đa hình — tự dispatch đúng hệ tướng.
        """
        return int(self.base_hp + self.calculate_skill_damage() * 1.5)

    def __add__(self, other):
        """
        Operator Overloading: nạp chồng toán tử +.
        - Champion + Champion → cộng 2 điểm chiến lực
        - Champion + int/float → cộng chiến lực với số (hỗ trợ vòng lặp cộng dồn)
        """
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        if isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        """
        __radd__ cho phép sum(team, 0) hoạt động:
        Python gọi 0 + champ → champ.__radd__(0) → get_combat_power() + 0
        """
        if isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __gt__(self, other):
        """
        Operator Overloading: nạp chồng toán tử >.
        So sánh điểm chiến lực giữa 2 quân cờ.
        """
        if not isinstance(other, Champion):
            print("Chỉ có thể so sánh giữa các quân cờ!")
            return NotImplemented
        return self.get_combat_power() > other.get_combat_power()