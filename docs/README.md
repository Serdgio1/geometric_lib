# Geometric Library

## Overview

This library provides functions to calculate areas and perimeters for basic geometric shapes: circle, rectangle, and square. It is designed for educational and practical use, supporting efficient computation and a clear API.

## Features

- Calculate area and perimeter for:
  - Circle
  - Rectangle
  - Square
  - Triangle
- Simple Python API
- Accurate mathematical formulas

## Math Formulas

Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Usage

Example usage for each shape:

```
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter

# Circle
r = 5
print("Circle area:", circle_area(r))
print("Circle perimeter:", circle_perimeter(r))

# Rectangle
a, b = 4, 6
print("Rectangle area:", rectangle_area(a, b))
print("Rectangle perimeter:", rectangle_perimeter(a, b))

# Square
a = 3
print("Square area:", square_area(a))
print("Square perimeter:", square_perimeter(a))
```

## Structure

- `circle.py` — Circle formulas
- `rectangle.py` — Rectangle formulas
- `square.py` — Square formulas
- `ellipse.py` — Ellipse formulas
- `triangle.py` — (if implemented)
- `docs/README.md` — Documentation

## History

Recent changes:

- 2ef615e 2025-09-30 Added `rectangle.py`
- d078c8d 2021-03-04 L-03: Docs added
- 8ba9aeb 2021-03-04 L-03: Circle and square added

## Requirements

- Python 3.x

## License

MIT License
