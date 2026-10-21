LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"строка не соответствует формату: {line!r}")

    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"неизвестный уровень: {level!r}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n):
    messages = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            text = event["message"]
            messages[text] = messages.get(text, 0) + 1

    ranked = sorted(messages.items(), key=lambda item: (-item[1], item[0]))
    return [[text, count] for text, count in ranked[:n]]


def format_report(counts, errors):
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for text, count in errors:
        lines.append(f"- {text} — {count}")
    return "\n".join(lines) + "\n"