rule auto_rule_20250726202958_3263 {
  strings:
    $o0 = "SHInvokePrinterCommandA" wide ascii nocase
    $o1 = "pqwTot" wide ascii nocase
    $o2 = "pszFirst" wide ascii nocase
    $o3 = "dword_445E4C" wide ascii nocase
    $o4 = "WriteProfileStringW" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726203001_7550 {
  strings:
    $o0 = "StrStrIA" wide ascii nocase
    $o1 = "dwFreeType" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726203006_1638 {
  condition:
    auto_rule_20250726202958_3263 or auto_rule_20250726203001_7550
}