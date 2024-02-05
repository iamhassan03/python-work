def calculate_population(
    init_population, birth_rate, death_rate, immigrant_rate, years
):
    population = init_population
    total_secs = 365 * 24 * 60 * 60

    for year in range(1, years + 1):
        births = total_secs // birth_rate
        deaths = total_secs // death_rate
        immigrants = total_secs // immigrant_rate

        population += births + immigrants - deaths

        print(f"Population after {year} years is: {population}")


def main():
    init_population = int(input("Enter Initial Population: ").strip())
    birth_rate = int(input("Enter Birth Rate: ").strip())
    death_rate = int(input("Enter Death Rate: ").strip())
    immigrant_rate = int(input("Enter Immigrant Rate: ").strip())
    years = int(input("Enter no. of Years: ").strip())

    calculate_population(init_population, birth_rate, death_rate, immigrant_rate, years)


if __name__ == "__main__":
    main()
