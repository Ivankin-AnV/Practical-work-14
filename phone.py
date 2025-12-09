from typing import Optional


class Phone:
    brand: str
    model: str
    price: float
    color: str
    storage_gb: int
    is_in_stock: bool

    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        storage_gb: int,
        is_in_stock: bool
    ):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.storage_gb = storage_gb
        self.is_in_stock = is_in_stock

    def get_full_name(self) -> str:
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        if not (0 <= discount_percent <= 100):
            raise ValueError("Скидка должна быть от 0 до 100%.")
        self.price -= self.price * discount_percent / 100

    def check_availability(self) -> str:
        return "В наличии" if self.is_in_stock else "Нет в наличии"

    def __str__(self) -> str:
        status = "есть в наличии" if self.is_in_stock else "нет в наличии"
        return (
            f"Телефон {self.get_full_name()} — {self.color}, "
            f"{self.storage_gb}GB, цена: {self.price}₽, {status}"
        )


def run_demonstration():
    print("=== Каталог телефонов ===")

    phone1 = Phone("Apple", "iPhone 14", 80000, "черный", 128, True)
    phone2 = Phone("Samsung", "Galaxy S23", 75000, "белый", 256, True)
    phone3 = Phone("Xiaomi", "Mi 11", 42000, "синий", 128, False)

    print(phone1)
    print(phone2)
    print(phone3)

    print("\n--- Cтатус ---")
    print(phone1.get_full_name(), "-", phone1.check_availability())
    print(phone3.get_full_name(), "-", phone3.check_availability())

    print("\n--- Скидки ---")
    print("Цена до:", phone2.price)
    phone2.apply_discount(10)
    print("Цена после:", phone2.price)

if __name__ == "__main__":
    run_demonstration()
