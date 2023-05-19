from src.pfmp_richelbilderbeek.medium import get_test_datas
from src.pfmp_richelbilderbeek.medium import get_sorting_functions
from src.pfmp_richelbilderbeek.medium import get_speed_measurements
from src.pfmp_richelbilderbeek.medium import save_speed_measurements

if __name__ == "__main__":
    speed_measurements = get_speed_measurements(
        datas = get_test_datas(), 
        functions = get_sorting_functions()
    )
    save_speed_measurements(speed_measurements, "speeds.csv")
