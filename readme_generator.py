from glob import glob
from common.meta import get_metadata


def write_table_row(first: str, second: str, third: str, f):
    f.write('|' + first + '|' + second + '|' + third + '|\n')


def create_url(idx, day, y):
    url = 'https://adventofcode.com/'
    return "[{day}]({url}{year}/day/{index}) {emoji}" \
        .format(day=day.name, year=y, index=str(idx), emoji=day.emoji, url=url)


def get_files(day, y):
    raw_files = glob('year{year}/{day}/*.py'.format(day=day, year=y))
    a = [x.replace('year' + str(y), '').replace('\\', '/')[1:] for x in raw_files]
    print(a)
    return a


def main():
    """Generate README files for all years."""
    year_folders = glob("*/")
    years = sorted(
        [int(y.split('year')[1]) for y in list(filter(lambda d: 'year' in d, [x.strip('..\\') for x in year_folders]))])
    
    print(f"Generating README files for years: {years}")
    
    for year in years:
        f = open('./year{year}/README.md'.format(year=year), 'w', encoding="utf-8")

        # File header
        f.write('# 🎄 🎅 Advent of code {year} 🎅 🎄\n'.format(year=year))
        f.write('My Advent of Code (Season {year}) solutions written in Python 😀\n\n'.format(year=year))

        # Table Header
        write_table_row('#', 'Problem ☃', 'Solution ❄', f)
        write_table_row('---', '-------------', ':-------------:', f)

        directories = glob("*year{year}/*/".format(year=year))
        directories = sorted(
            [int(y) for y in [x.replace('year' + str(year) + '\\', '').strip('\\') for x in directories] if y.isnumeric()])

        for day_idx in directories:
            day_str = str(day_idx)
            files = get_files(day_str, year)

            file_links = ""
            if len(files) == 1:
                file_links = "[Part 1 & 2]({file})".format(file=files[0])
            if len(files) == 2:
                for i, file in enumerate(files):
                    if i > 0:
                        file_links += " - "
                    file_links += "[Part {p}]({file})".format(file=files[i], p=i + 1)
            write_table_row(day_str, create_url(day_str, get_metadata(year)[day_idx], year), file_links, f)

        f.close()
        print(f"  Generated year{year}/README.md")
    
    print("\nREADME generation complete!")


if __name__ == '__main__':
    main()
