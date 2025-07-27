rule auto_rule_20250726091808_8282 {
  strings:
    $o0 = "lstrcatW" wide ascii nocase
    $o1 = "EFFh" wide ascii nocase
    $o2 = "dword_4011CC" wide ascii nocase
  condition:
    3 of ($o*)
}