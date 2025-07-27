rule auto_rule_20250727033831_0523 {
  strings:
    $o0 = "UnwindUp2_0" wide ascii nocase
    $o1 = "__sbh_heap_init" wide ascii nocase
    $o2 = "byte_445B70" wide ascii nocase
  condition:
    3 of ($o*)
}