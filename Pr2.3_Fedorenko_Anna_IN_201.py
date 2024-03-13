def main():
  #Отримання значення температури в Цельсіях
  celsius = float(input("Введіть значення температури в градусах Цельсія: "))

  #Розрахунок температури за шкалою Фаренгейта
  fahrenheit = (celsius * 9/5) + 32

  #Розрахунок температури за шкалою Кельвіна
  kelvin = celsius + 273.15

  #Виведення результатів
  print(f"Температура за шкалою Фаренгейта: {fahrenheit:.2f}°F")
  print(f"Температура за шкалою Кельвіна: {kelvin:.2f}K")

if __name__ == "__main__":
  main()
