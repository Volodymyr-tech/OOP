from src.class_lawngrass import LawnGrass


def test_grass():
    grass = LawnGrass(
        "Футбольный газон", "мелкие семена для посыпа поля весной", 10, 100000, "England", "1 week", "green"
    )

    assert grass.name == "Футбольный газон"
    assert grass.description == "мелкие семена для посыпа поля весной"
    assert grass.price == 10
    assert grass.quantity == 100000
    assert grass.country == "England"
    assert grass.germination_period == "1 week"
    assert grass.color == "green"
