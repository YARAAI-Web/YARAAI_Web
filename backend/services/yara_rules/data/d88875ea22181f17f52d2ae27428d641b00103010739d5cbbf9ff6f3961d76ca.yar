rule auto_rule_20250726070703_4349 {
  strings:
    $o0 = "__sbh_heap_init" wide ascii nocase
    $o1 = "dword_44A040" wide ascii nocase
    $o2 = "Handler" wide ascii nocase
  condition:
    3 of ($o*)
}