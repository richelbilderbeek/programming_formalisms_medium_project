"""Profile the functions of The Small Project and The Medium Project."""
import cProfile

from src.pfmp_richelbilderbeek.medium import (
    get_datas,  # noqa: F401
    get_sorting_functions,
    get_speed_measurements,
    get_test_datas,
    save_speed_measurements,
)

if __name__ == "__main__":
    speed_measurements = get_speed_measurements(
        datas = get_test_datas(),
        functions = get_sorting_functions(),
    )
    save_speed_measurements(speed_measurements, "speeds.csv")

    cProfile.run(
        "get_speed_measurements("
        "datas = get_datas(data_lengths = [2, 4, 6, 8, 10]), "
        "functions = get_sorting_functions())",
    )

