rule auto_rule_20250726074507_0853 {
  strings:
    $o0 = "uSize" wide ascii nocase
    $o1 = "lpClassName" wide ascii nocase
    $o2 = "uiHi" wide ascii nocase
  condition:
    3 of ($o*)
}