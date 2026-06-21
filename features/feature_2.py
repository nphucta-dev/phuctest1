from models.warrior import Warrior
from models.mage import Mage


def _input_int(prompt, default=100):
    """Helper: nhập số nguyên, trả về default nếu nhập sai hoặc <= 0."""
    try:
        val = int(input(prompt).strip())
        return val if val > 0 else default
    except ValueError:
        print(f"Giá trị không hợp lệ, dùng mặc định {default}.")
        return default


def _input_float(prompt, default=1.0):
    """Helper: nhập số thực, trả về default nếu nhập sai hoặc <= 0."""
    try:
        val = float(input(prompt).strip())
        return val if val > 0 else default
    except ValueError:
        print(f"Giá trị không hợp lệ, dùng mặc định {default}.")
        return default


def add_champion(champion_pool):
    """Tạo tướng mới (Warrior hoặc Mage) và thêm vào bể tướng."""
    print("\n--- THÊM QUÂN CỜ MỚI ---")
    print("1. Warrior (Chiến binh)")
    print("2. Mage (Pháp sư)")
    choice = input("Chọn hệ tướng (1-2): ").strip()

    match choice:
        case "1":
            _forge_warrior(champion_pool)
        case "2":
            _forge_mage(champion_pool)
        case _:
            print("Lựa chọn không hợp lệ!")


def _check_duplicate(champion_pool, champion_id):
    """Bẫy 4: kiểm tra trùng mã tướng."""
    for champ in champion_pool:
        if champ.champion_id == champion_id.upper():
            print(f"Mã tướng {champion_id} đã tồn tại trong bể tướng!")
            return True
    return False


def _forge_warrior(champion_pool):
    print("\n--- TẠO TƯỚNG WARRIOR ---")
    champion_id = input("Nhập mã tướng: ").strip().upper()
    if _check_duplicate(champion_pool, champion_id):
        return

    name = input("Nhập tên tướng: ").strip().title()
    base_hp = _input_int("Nhập HP: ")
    base_atk = _input_int("Nhập ATK: ")
    shield_bonus = _input_int("Nhập Armor: ", default=0)

    warrior = Warrior(champion_id, name, base_hp, base_atk, shield_bonus)
    champion_pool.append(warrior)
    print(f"\nThêm tướng Warrior thành công!")
    print(f"Mã: {warrior.champion_id} | Tên: {warrior.name} | Chiến lực: {warrior.get_combat_power()}")


def _forge_mage(champion_pool):
    print("\n--- TẠO TƯỚNG MAGE ---")
    champion_id = input("Nhập mã tướng: ").strip().upper()
    if _check_duplicate(champion_pool, champion_id):
        return

    name = input("Nhập tên tướng: ").strip().title()
    base_hp = _input_int("Nhập HP: ")
    base_atk = _input_int("Nhập ATK: ")
    ability_power = _input_float("Nhập Ability Power (VD: 1.5): ", default=1.0)

    mage = Mage(champion_id, name, base_hp, base_atk, ability_power)
    champion_pool.append(mage)
    print(f"\nThêm tướng Mage thành công!")
    print(f"Mã: {mage.champion_id} | Tên: {mage.name} | Chiến lực: {mage.get_combat_power()}")