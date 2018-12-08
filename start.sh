#/usr/bin/env bash

YEAR="${1}"
DAY="${2}"
DAY_NO_ZEROS="$(echo $DAY | sed 's/^0*//')"

OUTPUT="${YEAR}/python/day${DAY}.py"

PUZZLE_URL="https://adventofcode.com/${YEAR}/day/${DAY_NO_ZEROS}/input"
PUZZLE_FILE="input${DAY}.txt"

curl "${PUZZLE_URL}" -H "cookie: session=${AOC_SESSION_COOKIE}" -o "${PUZZLE_FILE}" 2>/dev/null

mkdir -p "$(dirname ${OUTPUT})"
echo "#Advent of Code - Day ${DAY}" > ${OUTPUT}
mv ${PUZZLE_FILE} "${YEAR}/data/${PUZZLE_FILE}"

code "${OUTPUT}"