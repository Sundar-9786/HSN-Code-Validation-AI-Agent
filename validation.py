import pandas as pd
import re


file_path = "HSN_SAC.xlsx"
df = pd.read_excel(file_path, dtype={"HSNCode": str})


def load_hsn_data(file_path):
    #df = pd.read_excel(file_path)
    return df.set_index('HSNCode')['Description'].to_dict()



def hierarchical_check(hsn_code, hsn_dict):
    # Get all parent prefixes from longest to shortest
    parent_codes = [hsn_code[:i] for i in range(len(hsn_code)-1, 1, -1)]
    found_parents = [(code, hsn_dict[code]) for code in parent_codes if code in hsn_dict]
    return found_parents


def validate_hsn_code(hsn_code, hsn_dict):
    # Format Validation
    if not re.match(r'^\d{2,8}$', hsn_code):
        return {
            "Code": hsn_code,
            "Valid": False,
            "Reason": "Invalid format. Code must be 2 to 8 digits."
        }

    # Existence Validation
    if hsn_code in hsn_dict:
        return {
            "Code": hsn_code,
            "Valid": True,
            "Description": hsn_dict[hsn_code]
        }

    hierarchy = hierarchical_check(hsn_code, hsn_dict)
    if hierarchy:
        return {
            "Code": hsn_code,
            "Valid": False,
            "Reason": "Exact code not found.",
            "Suggestions": hierarchy
        }

    return {
        "Code": hsn_code,
        "Valid": False,
        "Reason": "HSN code not found in master data.",
        "Suggestions": []
    }




def validate_multiple_hsn_codes(code_list, hsn_dict):
    results = []
    for code in code_list:
        result = validate_hsn_code(code.strip(), hsn_dict)
        results.append(result)
    return results
#Purpose
#Strips each code of extra spaces

#Calls your single validation function

#Returns a list of result dicts






def print_validation_result(result):
    if result['Valid']:
        print(f"✅ VALID HSN CODE: {result['Code']}")
        print(f"   ➤ Description: {result['Description']}\n")
    else:
        print(f"❌ INVALID HSN CODE: {result['Code']}")
        print(f"   ➤ Reason: {result['Reason']}")
        if result.get("Suggestions"):
            print("   🔎 Did you mean (Parent Categories)?")
            for code, desc in result['Suggestions']:
                print(f"      • {code}: {desc}")
        print()




def print_batch_results(results):
    print("\n🔎 HSN Code Validation Summary:\n")
    for res in results:
        print_validation_result(res)



if __name__ == "__main__":
    file_path = "HSN_SAC.xlsx"  # Your uploaded file
    hsn_dict = load_hsn_data(file_path)

    #test_codes = ["01012100", "1234", "abcdefgh", "01", "99999999", "0101","01013010","01012100","01011010","37040010"]
    test_codes = ["01011010", "010110", "0101","01","01012100","0101291","6005420"]

    results = validate_multiple_hsn_codes(test_codes, hsn_dict)
    print_batch_results(results)




