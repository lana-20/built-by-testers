#!/bin/bash
# Validate measurement CSV files for consistency and accuracy

set -e

CSV_FILE="${1:-../data/creator_sites.csv}"

if [ ! -f "$CSV_FILE" ]; then
    echo "Error: CSV file not found: $CSV_FILE"
    exit 1
fi

echo "Validating measurements in: $CSV_FILE"
echo ""

# Check header
header=$(head -1 "$CSV_FILE")
expected_header="site,url,creator,category,focus_area,cli_ms,cli_usd,turns_cli,mcp_ms,mcp_usd,turns_mcp,notes"

if [ "$header" != "$expected_header" ]; then
    echo "⚠️  Warning: CSV header mismatch"
    echo "Expected: $expected_header"
    echo "Got:      $header"
fi

# Validate measurements
echo "Checking measurements..."
echo ""

line_no=1
while IFS=',' read -r site url creator category focus cli_ms cli_usd turns_cli mcp_ms mcp_usd turns_mcp notes
do
    line_no=$((line_no + 1))

    if [ $line_no -eq 2 ]; then continue; fi  # Skip header

    # Check numeric fields
    if ! [[ "$cli_ms" =~ ^[0-9]+$ ]]; then
        echo "❌ Line $line_no: Invalid CLI ms: $cli_ms"
    fi

    if ! [[ "$mcp_ms" =~ ^[0-9]+$ ]]; then
        echo "❌ Line $line_no: Invalid MCP ms: $mcp_ms"
    fi

    # Calculate ratio if both present
    if [ "$cli_ms" -gt 0 ] && [ "$mcp_ms" -gt 0 ]; then
        ratio=$(echo "scale=1; $mcp_ms / $cli_ms" | bc)
        echo "✓ $site: CLI ${cli_ms}ms, MCP ${mcp_ms}ms, Ratio ${ratio}×"
    fi
done < "$CSV_FILE"

echo ""
echo "Validation complete!"
