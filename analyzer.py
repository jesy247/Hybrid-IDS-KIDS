import subprocess

def analyze_program():
    print("=== KIDS: Deep System Call Analyzer ===")
    program = input("Enter program name to analyze: ").strip()
    
    if not program:
        print("No program entered.")
        return
    
    try:
        # استخدام strace لجمع ال system calls
        result = subprocess.run(
            ["strace", "-c", program],
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stderr
        print("\n--- Analysis Results ---")
        print(output)

        # حساب عدد النداءات
        total_calls = 0
        for line in output.splitlines():
            parts = line.split()
            if len(parts) >= 5:
                try:
                    total_calls += int(parts[3])
                except:
                    pass

        print(f"\nTotal System Calls: {total_calls}")

        # تحديد النتيجة
        if total_calls > 200:
            print("Result: 🚨 Suspicious Behavior")
        else:
            print("Result: ✅ Normal Behavior")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_program()