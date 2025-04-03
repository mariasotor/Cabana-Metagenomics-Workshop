```

fastq_paths="$1"

echo "ID,R1,R2" > manifest.csv  # Create header row

while read line; do  # Use semicolon for better readability
    if [[ $line == *"_1.fastq" ]]; then  # Check for _1 first
        read1="$line"
        # Construct read2 filename directly
        read2="${line%_1.fastq}_2.fastq"

        if [[ ! -f "$read2" ]]; then
            echo "Error: Cannot find corresponding R2 file for $read1" >&2
            continue  # Skip to the next line in the input file
        fi

        lane_id=$(basename "${line%_1.fastq}")
        echo "$lane_id,$read1,$read2" >> manifest.csv
    fi
done < "$fastq_paths"


```
