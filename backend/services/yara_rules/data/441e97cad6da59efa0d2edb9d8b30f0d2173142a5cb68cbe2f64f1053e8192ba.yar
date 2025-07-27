rule auto_rule_20250727000542_9084 {
  strings:
    $o0 = "dword_45CF18" wide ascii nocase
    $o1 = "Handler" wide ascii nocase
    $o2 = "__sbh_heap_init" wide ascii nocase
  condition:
    3 of ($o*)
}