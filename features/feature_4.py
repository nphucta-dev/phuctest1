from features.feature_3 import _find_champion


def team_power(champion_pool):
    """
    Tính tổng chiến lực đội hình bằng toán tử + (Operator Overloading).

    sum(team, 0) hoạt động nhờ __radd__:
    - Python tính 0 + champ1 → champ1.__radd__(0) → get_combat_power() + 0
    - Tiếp tục cộng dồn với champ2, champ3...
    """
    print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---")
    raw = input("Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: ")
    id_list = [x.strip().upper() for x in raw.split(",") if x.strip()]

    team = []
    for cid in id_list:
        champ = _find_champion(champion_pool, cid)
        if champ is None:
            print(f"Mã tướng {cid} không hợp lệ, bỏ qua!")
        else:
            team.append(champ)

    if not team:
        print("Không có quân cờ hợp lệ nào trong đội hình!")
        return

    print("\nDanh sách đội hình:")
    for i, champ in enumerate(team, 1):
        print(f"{i}. {champ.champion_id} - {champ.name} | Chiến lực: {champ.get_combat_power()}")

    # __radd__ cho phép sum() khởi đầu từ 0
    total = sum(team, 0)
    print(f"Tổng chiến lực đội hình: {total}")