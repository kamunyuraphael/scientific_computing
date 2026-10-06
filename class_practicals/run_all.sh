#!/usr/bin/env bash
# Runs every task script and stores its console output in outputs/
mkdir -p outputs figures
cd code
for f in Task_*.py; do
  echo "Running $f ..."
  python3 "$f" > "../outputs/${f%.py}.txt" 2>&1
done
echo "Done. Console outputs in outputs/, figures in figures/"
