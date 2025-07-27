rule auto_rule_20250726225650_7802 {
  strings:
    $o0 = "dword_44C080" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
  condition:
    all of them
}