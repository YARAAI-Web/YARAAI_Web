rule auto_rule_20250727034737_6458 {
  strings:
    $o0 = "pptDst" wide ascii nocase
    $o1 = "piconinfo" wide ascii nocase
    $o2 = "lpPathSpec" wide ascii nocase
  condition:
    3 of ($o*)
}