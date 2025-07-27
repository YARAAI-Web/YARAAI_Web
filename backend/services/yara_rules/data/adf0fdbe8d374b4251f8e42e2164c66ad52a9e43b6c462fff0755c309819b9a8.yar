rule auto_rule_20250726112815_5121 {
  strings:
    $o0 = "x73B3" wide ascii nocase
    $o1 = "aZ8nYck5" wide ascii nocase
    $o2 = "dword_413C1E" wide ascii nocase
  condition:
    3 of ($o*)
}