rule auto_rule_20250726213814_2248 {
  strings:
    $o0 = "_close" wide ascii nocase
    $o1 = "xtoa" wide ascii nocase
    $o2 = "dword_46482C" wide ascii nocase
  condition:
    3 of ($o*)
}