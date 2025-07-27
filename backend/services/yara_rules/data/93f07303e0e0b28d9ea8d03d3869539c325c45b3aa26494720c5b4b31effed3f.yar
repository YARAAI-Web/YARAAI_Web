rule auto_rule_20250727012110_1041 {
  strings:
    $o0 = "__sbh_heap_check" wide ascii nocase
    $o1 = "byte_4673C6" wide ascii nocase
    $o2 = "lpCharType" wide ascii nocase
  condition:
    3 of ($o*)
}