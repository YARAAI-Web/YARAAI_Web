rule auto_rule_20250726141323_2165 {
  strings:
    $o0 = "byte_4673C6" wide ascii nocase
    $o1 = "__sbh_heap_init" wide ascii nocase
  condition:
    all of them
}