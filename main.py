from pathlib import Path
 
from logstats import count_levels, format_report, top_errors
 
HERE = Path(__file__).parent
 
 
def main():
    name = input().strip()
    log_path = HERE / name
 
    with open(log_path, encoding="utf-8") as log:
        counts = count_levels(log)
 
    with open(log_path, encoding="utf-8") as log:
        errors = top_errors(log, 3)
 
    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))
 
    report = format_report(counts, errors)
    with open(HERE / "report.txt", "w", encoding="utf-8") as out:
        out.write(report)
 
 
if __name__ == "__main__":
    main()