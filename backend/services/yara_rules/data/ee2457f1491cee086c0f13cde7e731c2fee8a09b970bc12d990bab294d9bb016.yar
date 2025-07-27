rule auto_rule_20250727015602_3309 {
  strings:
    $o0 = "__sbh_heap_check" wide ascii nocase
    $o1 = "x404751" wide ascii nocase
    $o2 = "dword_467CB4" wide ascii nocase
  condition:
    3 of ($o*)
}