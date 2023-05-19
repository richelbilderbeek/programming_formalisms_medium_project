import cProfile

from src.pfmp_richelbilderbeek.medium import get_datas
from src.pfmp_richelbilderbeek.medium import get_test_datas
from src.pfmp_richelbilderbeek.medium import get_sorting_functions
from src.pfmp_richelbilderbeek.medium import get_speed_measurements
from src.pfmp_richelbilderbeek.medium import save_speed_measurements

if __name__ == "__main__":
    if 1 == 2:
        speed_measurements = get_speed_measurements(
            datas = get_test_datas(), 
            functions = get_sorting_functions()
        )
        save_speed_measurements(speed_measurements, "speeds.csv")

    cProfile.run(
        "get_speed_measurements("
        "datas = get_datas(data_lengths = [2, 4, 6, 8, 10]), "
        "functions = get_sorting_functions())"
    )