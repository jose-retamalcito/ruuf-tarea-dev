from typing import List, Dict
import json


def determine_long_side(width: int, height: int) -> tuple[int, int]:
    if (width >= height):
        return width, height

    return height, width


def pack_panels_in_roof(panel_long_side: int, panel_short_side: int, roof_long_side: int, roof_short_side: int) -> int:
    how_many_fit_long_side = roof_long_side // panel_long_side
    how_many_fit_short_side = roof_short_side // panel_short_side

    remaining_long = roof_long_side - how_many_fit_long_side * panel_long_side

    if remaining_long < panel_short_side or roof_short_side < panel_long_side:
        return how_many_fit_long_side * how_many_fit_short_side

    remaining_space_panels = pack_panels_in_roof(panel_long_side, panel_short_side, roof_short_side, remaining_long)

    total_panels = how_many_fit_long_side * how_many_fit_short_side + remaining_space_panels

    return total_panels


def calculate_panels(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> int:
    panel_long_side, panel_short_side = determine_long_side(panel_width, panel_height)
    roof_long_side, roof_short_side = determine_long_side(roof_width, roof_height)

    long_long_panels = pack_panels_in_roof(panel_long_side, panel_short_side, roof_long_side, roof_short_side)
    short_long_panels = pack_panels_in_roof(panel_long_side, panel_short_side, roof_short_side, roof_long_side)

    max_panels_in_roof = max(long_long_panels, short_long_panels)

    return max_panels_in_roof


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
