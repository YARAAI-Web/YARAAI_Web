rule auto_rule_20250726152015_1223 {
  strings:
    $o0 = "dword_4642C8" wide ascii nocase
    $o1 = "dword_4643F0" wide ascii nocase
    $o2 = "dword_46443C" wide ascii nocase
  condition:
    3 of ($o*)
}