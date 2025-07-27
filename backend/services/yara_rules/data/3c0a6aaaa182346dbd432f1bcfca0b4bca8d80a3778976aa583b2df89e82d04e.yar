rule auto_rule_20250726085240_4542 {
  strings:
    $o0 = "LibraryA" wide ascii nocase
    $o1 = "dword_460600" wide ascii nocase
    $o2 = "dword_45FFC0" wide ascii nocase
    $o3 = "GetStringTypeW" wide ascii nocase
  condition:
    4 of ($o*)
}