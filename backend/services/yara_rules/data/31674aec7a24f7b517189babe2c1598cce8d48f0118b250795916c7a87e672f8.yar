rule auto_rule_20250726215611_8530 {
  strings:
    $o0 = "dword_43B235" wide ascii nocase
    $o1 = "dword_43B56A" wide ascii nocase
    $o2 = "dword_43B542" wide ascii nocase
    $o3 = "dword_43B3B0" wide ascii nocase
    $o4 = "dword_43B436" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726215612_1791 {
  strings:
    $o0 = "dword_43B104" wide ascii nocase
    $o1 = "dword_43B4F0" wide ascii nocase
    $o2 = "a58Rtmfzwnxtlll" wide ascii nocase
    $o3 = "dword_43B616" wide ascii nocase
    $o4 = "dword_43B0A5" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726215617_8004 {
  condition:
    auto_rule_20250726215611_8530 or auto_rule_20250726215612_1791
}