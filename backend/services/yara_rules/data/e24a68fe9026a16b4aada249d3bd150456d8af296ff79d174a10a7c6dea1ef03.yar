rule auto_rule_20250726102319_8312 {
  strings:
    $o0 = "x2B01" wide ascii nocase
    $o1 = "BDAh" wide ascii nocase
    $o2 = "dword_422840" wide ascii nocase
    $o3 = "C16h" wide ascii nocase
    $o4 = "dword_428505" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726102322_8316 {
  strings:
    $o0 = "dword_42852D" wide ascii nocase
    $o1 = "x2531" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726102325_2340 {
  condition:
    auto_rule_20250726102319_8312 or auto_rule_20250726102322_8316
}