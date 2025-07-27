rule auto_rule_20250726140130_9534 {
  strings:
    $o0 = "_heap_init" wide ascii nocase
    $o1 = "_aulldvrm" wide ascii nocase
    $o2 = "off_4764E8" wide ascii nocase
  condition:
    3 of ($o*)
}