rule auto_rule_20250726132944_2246 {
  strings:
    $o0 = "x43E88B00" wide ascii nocase
    $o1 = "aOoeqtw34466Bcn" wide ascii nocase
    $o2 = "dword_43B217" wide ascii nocase
    $o3 = "dword_43B7ED" wide ascii nocase
    $o4 = "aFsvbtckwrczpwk" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726132947_6270 {
  strings:
    $o0 = "dword_43B04C" wide ascii nocase
    $o1 = "dword_43B726" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726132951_1403 {
  condition:
    auto_rule_20250726132944_2246 or auto_rule_20250726132947_6270
}