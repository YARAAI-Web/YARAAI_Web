rule auto_rule_20250726181605_1621 {
  strings:
    $o0 = "TrailDown1" wide ascii nocase
    $o1 = "__dtold" wide ascii nocase
    $o2 = "dword_410CA4" wide ascii nocase
  condition:
    3 of ($o*)
}