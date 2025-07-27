rule auto_rule_20250726202047_4989 {
  strings:
    $o0 = "LongPathNameW" wide ascii nocase
    $o1 = "dword_4C126C" wide ascii nocase
    $o2 = "dword_4C15E0" wide ascii nocase
  condition:
    3 of ($o*)
}