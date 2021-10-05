# ViPR Client
A tool for downloading sequence data from the Virus Pathogen Resource (ViPR)

## Usage

```
usage: vipr-client [-h] [--family FAMILY] [--from-year FROM_YEAR] [--host HOST] [--continent CONTINENT]

optional arguments:
  -h, --help            show this help message and exit
  --family FAMILY       Virus family, (default: 'influenza')
  --from-year FROM_YEAR Starting from year, (default: 2 years ago)
  --host HOST           Host organism, (default: 'human')
  --continent CONTINENT Continent, (default: 'North America')
```

## Output

Current output is JSON-formatted output from the ViPR API. Output format and options are subject to change.