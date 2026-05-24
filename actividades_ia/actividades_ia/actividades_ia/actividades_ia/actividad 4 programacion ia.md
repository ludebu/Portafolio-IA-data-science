# Actividad 4 - Programación Asistida por IA

**Objetivo**

Explorar herramientas de programación asistida por Inteligencia Artificial para desarrollar código, autocompletar funciones y corregir errores automáticamente.

**Herramientas utilizadas**

- GitHub Codespaces
- GitHub Copilot
- ChatGPT
- Cursor AI

**Descripción del proyecto**

Se desarrolló un juego simple de adivinanza en Python donde el usuario debe descubrir un número aleatorio generado por el sistema.

**Código desarrollado**

python
import random

print("Juego de Adivinanza IA")

numero = random.randint(1, 10)
intentos = 0

while True:
    usuario = int(input("Adivina el número entre 1 y 10: "))
    intentos += 1

    if usuario == numero:
        print(f"Correcto. Lo lograste en {intentos} intentos.")
        break

    elif usuario < numero:
        print("El número es mayor.")

    else:
        print("El número es menor.")


---

**Uso de IA en programación**

**Autocompletado con Copilot**

GitHub Copilot sugirió automáticamente fragmentos de código y estructuras condicionales.

**Resultados**
- Mayor velocidad de desarrollo.
- Reducción de errores sintácticos.
- Mejora de productividad.

**Refactorización con IA**

Se utilizó IA para transformar el código procedural en programación orientada a objetos mediante clases.

**Resultados**
- Código más organizado.
- Mejor reutilización.
- Mayor escalabilidad.

**Experimentación**

**Corrección automática de errores con IA**

Durante la experimentación se introdujo intencionalmente un error tipográfico en la función `print()` escribiendo:

python prit("Juego de Adivinanza IA")


Al ejecutar el programa, Python generó un error `NameError` indicando que la función no estaba definida.

Posteriormente, el asistente de IA integrado en GitHub Codespaces detectó automáticamente el problema y sugirió reemplazar `prit()` por `print()`.

**Resultado**

La IA logró:
- identificar el error,
- explicar la causa,
- proponer una solución correcta,
- ejecutar nuevamente el programa sin errores.

Esto demuestra cómo las herramientas de Inteligencia Artificial pueden mejorar significativamente el proceso de debugging y desarrollo de software.


**Comparación de herramientas**

| Herramienta | Función principal | Resultado |
|---|---|---|
| Copilot | Autocompletado | Muy útil |
| ChatGPT | Explicación y corrección | Alta precisión |
| Cursor AI | Refactorización | Excelente organización |

---

# Reflexión crítica

La Inteligencia Artificial no reemplaza completamente al programador, pero sí transforma la manera en que se desarrolla software. Herramientas como GitHub Copilot y Codespaces permiten automatizar tareas repetitivas, sugerir código, detectar errores y acelerar significativamente el proceso de programación.

Durante esta actividad se observó que la IA fue capaz de identificar y corregir errores sintácticos de manera automática, además de proponer mejoras estructurales mediante programación orientada a objetos. Esto demuestra que la IA funciona como un asistente de productividad que ayuda al desarrollador a trabajar de forma más eficiente.

Sin embargo, confiar ciegamente en el código generado por IA puede representar riesgos importantes. La IA puede producir errores lógicos, vulnerabilidades de seguridad o soluciones poco optimizadas si el programador no revisa cuidadosamente el resultado. Por esta razón, el pensamiento crítico, la validación humana y el conocimiento técnico siguen siendo fundamentales en el desarrollo de software.

En conclusión, la IA no sustituye al programador, sino que lo empodera, permitiéndole enfocarse en tareas más complejas, creativas y analíticas dentro del proceso de desarrollo tecnológico.

# Conclusiones

- La IA acelera el desarrollo de código.
- Las herramientas de autocompletado mejoran productividad.
- La validación humana sigue siendo necesaria.
- La programación asistida por IA representa el futuro del desarrollo de software.

# Evidencias

**Captura de Codespaces**

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/a3f8a2d8-8299-4285-84a9-ca166ee7b1e0" />


**Código generado**

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/f7197216-2227-4f17-9711-1a240273fa1a" />


**Corrección automática de errores**

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/e9d6f1e0-d067-4faf-a56c-7fb98718f76d" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/8b5421db-c767-483c-b37b-06b14b2781da" />

**Refactorizando**

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b25ba1f2-5095-4ec2-a5ec-e3d4ac6ed8cc" />



