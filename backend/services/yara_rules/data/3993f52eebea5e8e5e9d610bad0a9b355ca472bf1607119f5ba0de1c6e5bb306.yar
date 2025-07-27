rule auto_rule_20250726080956_3750 {
  strings:
    $o0 = "dword_426EC9" wide ascii nocase
    $o1 = "x7053u" wide ascii nocase
    $o2 = "x7801u" wide ascii nocase
  condition:
    3 of ($o*)
}