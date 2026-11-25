import os

REPLY = "Thank you for your email. I am out of office permanently: I quit to become a barista, and your message now joins a queue I no longer monitor, which is the first honest SLA I have ever given."

MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_NAME = "entry.txt"


def validate_reply(reply):
    if not (MIN_CHARS <= len(reply) <= MAX_CHARS):
        raise ValueError("reply must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(reply)))
    if "\n" in reply or "\r" in reply:
        raise ValueError("reply must be a single line")
    if not reply.strip():
        raise ValueError("reply must not be only whitespace")


def write_entry(reply, out_dir):
    validate_reply(reply)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(reply)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(REPLY, out_dir)


if __name__ == "__main__":
    main()
