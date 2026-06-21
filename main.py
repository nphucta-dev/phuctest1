"""
2. Phân tích Đa hình — calculate_skill_damage()

Mỗi hệ tướng có công thức tính sát thương khác nhau hoàn toàn, nhưng tất cả đều dùng chung tên hàm. Khi Studio thêm Assassin hay Ranger, chỉ cần tạo lớp mới kế thừa Champion và override riêng — code ở feature_1.py gọi champ.calculate_skill_damage() không cần sửa một dòng nào (Open/Closed Principle).
3. Phân tích __add__

__add__ xử lý 2 trường hợp:

champion + champion → cộng 2 get_combat_power()
champion + int/float (hoặc int/float + champion qua __radd__) → cộng điểm chiến lực với một số

Nhờ __radd__, sum(team, 0) hoạt động được: Python gọi 0 + champ1 → champ1.__radd__(0) → champ1.get_combat_power() + 0, rồi tiếp tục cộng dồn.
"""

from models.warrior import Warrior
from models.mage import Mage
from features import view_pool, add_champion, compare_champions, team_power


def main():
    # Mock data ban đầu
    champion_pool = [
        Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
        Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
        Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0),
    ]

    while True:
        print("\n===== RIKKEI RPG - AUTO-BATTLER MANAGER =====")
        print("1. Hiển thị bể tướng hiện có")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực Đội Hình Ra Sân")
        print("5. Thoát chương trình")
        print("=============================================")
        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                view_pool(champion_pool)
            case "2":
                add_champion(champion_pool)
            case "3":
                compare_champions(champion_pool)
            case "4":
                team_power(champion_pool)
            case "5":
                print("Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5!")


if __name__ == "__main__":
    main()