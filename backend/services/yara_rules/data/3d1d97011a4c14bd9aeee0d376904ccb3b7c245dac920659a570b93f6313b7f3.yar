rule auto_rule_20250726163904_1556 {
  strings:
    $o0 = "dword_777B8" wide ascii nocase
    $o1 = "dword_77728" wide ascii nocase
    $o2 = "dword_783D4" wide ascii nocase
  condition:
    3 of ($o*)
}