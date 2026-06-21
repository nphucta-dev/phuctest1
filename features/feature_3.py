def _find_champion(champion_pool, champion_id):
    """Bẫy 3: tìm tướng theo mã, trả về None nếu không thấy."""
    for champ in champion_pool:
        if champ.champion_id == champion_id.upper():
            return champ
    return None


def compare_champions(champion_pool):
    """
    So sánh 2 quân cờ bằng toán tử > (Operator Overloading __gt__).
    Polymorphism: get_combat_power() tự gọi đúng calculate_skill_damage() của từng hệ.
    """
    print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")
    id1 = input("Nhập mã tướng thứ nhất: ").strip()
    id2 = input("Nhập mã tướng thứ hai: ").strip()

    c1 = _find_champion(champion_pool, id1)
    c2 = _find_champion(champion_pool, id2)

    if c1 is None:
        print(f"Mã tướng {id1} không hợp lệ, bỏ qua!")
        return
    if c2 is None:
        print(f"Mã tướng {id2} không hợp lệ, bỏ qua!")
        return

    print("\nThông tin so sánh:")
    print(f"{c1.champion_id} - {c1.name} | Hệ: {type(c1).__name__} | Chiến lực: {c1.get_combat_power()}")
    print(f"{c2.champion_id} - {c2.name} | Hệ: {type(c2).__name__} | Chiến lực: {c2.get_combat_power()}")

    # Operator Overloading __gt__ — Lesson 04
    if c1 > c2:
        print(f"Kết quả: {c1.champion_id} - {c1.name} mạnh hơn {c2.champion_id} - {c2.name}.")
    elif c2 > c1:
        print(f"Kết quả: {c2.champion_id} - {c2.name} mạnh hơn {c1.champion_id} - {c1.name}.")
    else:
        print("Kết quả: Hai quân cờ có chiến lực ngang nhau.")