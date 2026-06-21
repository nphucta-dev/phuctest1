def view_pool(champion_pool):
    """
    Hiển thị bể tướng.
    Duck Typing / Polymorphism: gọi calculate_skill_damage() và get_combat_power()
    đồng nhất trên mọi hệ tướng — Python tự dispatch đúng phiên bản.
    """
    print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
    if not champion_pool:
        print("Bể tướng hiện đang trống.")
        return

    header = f"{'Mã':<7}| {'Tên tướng':<22}| {'Hệ':<10}| {'HP':<7}| {'ATK':<7}| {'Chỉ số riêng':<20}| Chiến lực"
    print(header)
    print("-" * 101)

    for champ in champion_pool:
        champ_type = type(champ).__name__
        extra = champ.get_extra_stat_label()
        power = champ.get_combat_power()
        print(
            f"{champ.champion_id:<7}| {champ.name:<22}| {champ_type:<10}| "
            f"{champ.base_hp:<7}| {champ.base_atk:<7}| {extra:<20}| {power}"
        )

    print("-" * 101)