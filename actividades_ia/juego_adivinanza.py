import random


class GuessingGame:
    def __init__(self, low: int = 1, high: int = 10) -> None:
        self.low = low
        self.high = high
        self.number = random.randint(self.low, self.high)
        self.attempts = 0

    def prompt_guess(self) -> int:
        while True:
            try:
                guess = int(input(f"Adivina el número entre {self.low} y {self.high}: "))
                return guess
            except ValueError:
                print("Entrada inválida. Introduce un número entero.")

    def check_guess(self, guess: int) -> bool:
        self.attempts += 1
        if guess == self.number:
            print(f"Correcto. Lo lograste en {self.attempts} intentos.")
            return True
        if guess < self.number:
            print("El número es mayor.")
            return False
        print("El número es menor.")
        return False

    def play(self) -> None:
        print("Juego de Adivinanza IA")
        while True:
            guess = self.prompt_guess()
            if self.check_guess(guess):
                break


if __name__ == "__main__":
    game = GuessingGame()
    game.play()