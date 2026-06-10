import sys

def main():
    try:
        with open(r'C:\Users\Dell\Desktop\Saurabh\ocr_results.txt', 'rb') as f:
            orig = f.read()
            
        print(f"Original file size: {len(orig)} bytes")
        print("First 20 bytes:", orig[:20])
        
        # Test decodings
        decodings = ['utf-8', 'latin-1', 'cp1252', 'utf-16', 'utf-16-le', 'utf-16-be']
        for dec in decodings:
            try:
                text = orig.decode(dec)
                # Count English words
                word_count = text.lower().count("error") + text.lower().count("file") + text.lower().count("png")
                print(f"Decoding {dec}: successfully decoded. English indicator word count: {word_count}")
                if word_count > 5:
                    print(f"--> Found correct encoding: {dec}!")
                    with open(r'C:\Users\Dell\Desktop\Saurabh\ocr_readable.txt', 'w', encoding='utf-8') as out:
                        out.write(text)
                    print("Written to C:/Users/Dell/Desktop/Saurabh/ocr_readable.txt")
                    return
            except Exception as e:
                print(f"Decoding {dec} failed: {e}")
                
        # Try with replace if all failed
        for dec in decodings:
            text = orig.decode(dec, errors='replace')
            word_count = text.lower().count("error") + text.lower().count("file") + text.lower().count("png")
            print(f"Decoding {dec} (replace): word count: {word_count}")
            if word_count > 5:
                print(f"--> Found near correct encoding (replace): {dec}")
                with open(r'C:\Users\Dell\Desktop\Saurabh\ocr_readable.txt', 'w', encoding='utf-8') as out:
                    out.write(text)
                print("Written to C:/Users/Dell/Desktop/Saurabh/ocr_readable.txt")
                return
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
