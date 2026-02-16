# ===== GAME RULE =====
# One wrong option = GAME OVER
# Game stops instantly on failure


def game_over(reason):
    print("\n❌ GAME OVER ❌")
    print(reason)
    exit()


# ===== GLOBAL STATE =====
inventory = []
lonely = True
malik_found = False
duet = False
business = False
malik_alive = True
achievement_dose = False


# ===== INTRO (LONELY START) =====
print("You wake up alone inside the Wagh Bakri factory.")
print("No friends. No hope. Just machines and tea fumes.\n")


# ===== Q1 =====
def q1():
    print("Q1: You hear footsteps.")
    print("1. Hide silently")
    print("2. Call for help")
    c = input("> ")
    if c == "1":
        q2()
    else:
        game_over("Guards hear you and drag you away.")


# ===== TEDDY ENCOUNTER =====
def q2():
    print("\nQ2: Teddy appears — fat physics teacher.")
    print("He smells like chai alcohol.")
    print("1. Offer him chai")
    print("2. Laugh at him")
    c = input("> ")
    if c == "1":
        q3()
    else:
        game_over("Angry Teddy uses physics and chai rage.")


def q3():
    print("\nQ3: Teddy is drunk on chai.")
    print("1. Let him pass out")
    print("2. Push him")
    c = input("> ")
    if c == "1":
        q4()
    else:
        game_over("Teddy falls on you. Instant death.")


# ===== MAN ENCOUNTER =====
def q4():
    print("\nQ4: Man the muscular guard blocks path.")
    print("1. Stay hidden")
    print("2. Try to fight")
    c = input("> ")
    if c == "1":
        q5()
    else:
        game_over("Man breaks every bone in your body.")


# ===== DOSE ACHIEVEMENT =====
def q5():
    global achievement_dose
    print("\nQ5: Dose appears.")
    print("1. Say 'dose mama'")
    print("2. Ignore Dose")
    c = input("> ")
    if c == "1":
        achievement_dose = True
        print("\n🏆 ACHIEVEMENT UNLOCKED 🏆")
        print("DOSE DEFEATED BY WORDS\n")
        q6()
    else:
        game_over("Dose alerts the guards.")


# ===== MALIK INTRO =====
def q6():
    global malik_found, lonely
    print("Q6: You feel extremely lonely.")
    print("1. Keep going alone")
    print("2. Trust a voice calling you")
    c = input("> ")
    if c == "2":
        malik_found = True
        lonely = False
        malik_intro()
    else:
        game_over("Loneliness consumes you.")


def malik_intro():
    print("\n🔥 MALIK SPAWNS 🔥")
    print("Malik: 'malik tere bande hum'\n")
    q7()


# ===== DUET SONG =====
def q7():
    global duet
    print("Q7: Malik suggests a duet.")
    print("1. Sing duet")
    print("2. Say no")
    c = input("> ")
    if c == "1":
        duet = True
        print("\n🎵 DUET SONG ACTIVATED 🎵")
        q8()
    else:
        game_over("Without unity, you fail.")


# ===== BUSINESS =====
def q8():
    global business
    print("\nQ8: Lehna appears.")
    print("1. Do business")
    print("2. Threaten Lehna")
    c = input("> ")
    if c == "1" and duet:
        business = True
        inventory.extend(["Fake Sword", "Tea Bomb"])
        print("\n💼 BUSINESS SUCCESS 💼")
        print("Inventory:", inventory)
        q9()
    else:
        game_over("Lehna betrays you.")


# ===== WEAPON CHOICE =====
def q9():
    print("\nQ9: Choose one weapon.")
    print("1. Fake Sword")
    print("2. Tea Bomb")
    c = input("> ")
    if c == "2":
        inventory.clear()
        inventory.append("Tea Bomb")
        q10()
    else:
        game_over("Fake Sword breaks instantly.")


# ===== MALIK SACRIFICE =====
def q10():
    global malik_alive
    print("\nQ10: Blast door closing!")
    print("1. Malik holds door")
    print("2. You hold door")
    c = input("> ")
    if c == "1":
        malik_alive = False
        print("\n😢 Malik sacrifices himself.")
        print("Malik: 'jeet ke aana...'")
        q11()
    else:
        game_over("Door crushes you.")


# ===== FINAL BOSS =====
def q11():
    print("\n⚔️ FINAL BOSS: WAGH ⚔️")
    print("1. Use Tea Bomb")
    print("2. Talk")
    c = input("> ")
    if c == "1" and "Tea Bomb" in inventory:
        q12()
    else:
        game_over("Wagh destroys you.")


def q12():
    print("\nFinal attack:")
    print("1. Strategic throw")
    print("2. Random throw")
    c = input("> ")
    if c == "1":
        true_ending()
    else:
        game_over("You miss. Wagh wins.")


# ===== TRUE ENDING =====
def true_ending():
    print("\n🔥🔥🔥 TRUE ENDING 🔥🔥🔥")
    print("The Tea Bomb explodes.")
    print("WAGH BAKRI FACTORY BURNS.")
    if malik_alive:
        print("Malik stands beside you.")
    else:
        print("You remember Malik. His sacrifice saved everything.")
    if achievement_dose:
        print("🏆 Secret Achievement: DOSE MAMA 🏆")
    print("\n🏆 YOU WIN 🏆")
    exit()


# ===== START GAME =====
q1()
